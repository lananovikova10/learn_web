from flask import Flask, render_template
from weather import weather_by_city
from python_org_news import get_python_news

app = Flask(__name__)

#link function-handler to path / - main page. @app.route is a decorator
@app.route("/")
def hello():
    title = 'Новостной сайт'
    weather = weather_by_city('Veher-de-la-Frontera')
    weather_description = weather['lang_ru'][0]['value']
    news_list = get_python_news()
    return render_template('index.html', weather = weather, page_title = title, weather_description = weather_description, news_list = news_list)

#if this file run directly
if __name__=="__main__":
    app.run(debug=True)