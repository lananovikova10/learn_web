from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_login import LoginManager


from webapp.user.forms import LoginForm
from webapp.weather import weather_by_city


db = SQLAlchemy()

app = Flask(__name__)
app.config.from_pyfile('config.py')
migrate = Migrate()
db.init_app(app)
migrate.init_app(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from webapp.user.models import User
from webapp.news.models import News
#from webapp.python_org_news import get_python_news
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.news.views import blueprint as  news_blueprint


app.register_blueprint(user_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(news_blueprint)

#if __name__=="__main__":
#    app.run(debug=True)
