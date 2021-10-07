from webapp import app, db
from webapp.python_org_news import get_python_news

with app.app_context():
    get_python_news()