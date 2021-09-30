import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.db import db_session
from webapp.model import News

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_python_news():
    html = get_html('https://www.python.org/blogs/')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
        result_news = []
        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            publish_date = news.find('time').text
            try:
                publish_date = datetime.strptime(publish_date, '%Y-%m-%d')
            except(ValueError):
                publish_date = datetime.now()
        save_news(title=title, url=url, publish_date=publish_date)
    return False 

def save_news(title, url, publish_date):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, publish_date=publish_date)
        db_session.add(new_news)
        db_session.commit()