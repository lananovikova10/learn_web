from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

from flask_login import LoginManager, login_user, logout_user, current_user, login_required

from webapp.forms import LoginForm
from webapp.weather import weather_by_city


db = SQLAlchemy()

app = Flask(__name__)
app.config.from_pyfile('config.py')
migrate = Migrate()
db.init_app(app)
migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
    
@app.route('/')
def index():
    title = "Новости Python"
    weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
    weather_description = weather['lang_ru'][0]['value'].lower()
    news_list = model.News.query.order_by(model.News.published.desc()).all()
    return render_template('index.html', page_title=title, weather=weather, weather_description = weather_description, news_list=news_list)

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)

@app.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = model.User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_index():
    if current_user.is_admin:
        return 'Привет админ'
    else:
        return 'Ты не админ!' 

from webapp.python_org_news import get_python_news
from webapp import model
from webapp.model import db, News, User

#if __name__=="__main__":
#    app.run(debug=True)
