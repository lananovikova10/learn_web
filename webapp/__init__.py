from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from webapp.forms import LoginForm

from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city
from webapp.model import News

from webapp import model

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
    
@app.route('/')
def index():
    title = "Новости Python"
    weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
    weather_description = weather['lang_ru'][0]['value'].lower()
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template('index.html', page_title=title, weather=weather, weather_description = weather_description, news_list=news_list)

@app.route('/login')
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template('login.html', page_title=title, form=login_form)

if __name__=="__main__":
    app.run(debug=True)