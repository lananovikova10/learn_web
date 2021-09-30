from flask import Flask, render_template
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city
from webapp.db import db_session
from webapp.model import News

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    #db_session.init_app(app)
    
    @app.route('/')
    def index():
        title = "Новости Python"
        weather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        weather_description = weather['lang_ru'][0]['value'].lower()
        news_list = News.query.order_by(News.publish_date.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, weather_description = weather_description, news_list=news_list)
    return app

if __name__=="__main__":
    app.run(debug=True)