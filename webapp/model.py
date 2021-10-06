from sqlalchemy import Column, Integer, String, DateTime, Text

from webapp import db
class News(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        published = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<News {} {}>'.format(self.title, self.url)


#class User(Base):
#    __tablename__ = 'users'
#    id = Column(Integer, primary_key=True)
#    name = Column(String)
#    email = Column(String(120), unique=True)

#called when we type user instance in the command line
#    def __repr__(self):
#        return f'<User {self.name} {self.email}>'

#if __name__ == "__main__":
#    Base.metadata.create_all(bind=engine)