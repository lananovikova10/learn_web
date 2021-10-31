from sqlalchemy import Column, Integer, String, DateTime, Text

#from werkzeug.security import generate_password_hash, check_password_hash

from webapp import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)