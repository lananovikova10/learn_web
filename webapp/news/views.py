from flask import Flask, render_template, Blueprint, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

from webapp.news.models import News

from webapp.weather import weather_by_city

blueprint = Blueprint('news', __name__)

@blueprint.route('/')
def index():
    title = "Новости Python"
    weather = weather_by_city(current_app.config["WEATHER_DEFAULT_CITY"])
    weather_description = weather['lang_ru'][0]['value'].lower()
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template('news/index.html', page_title=title, weather=weather, weather_description = weather_description, news_list=news_list)
