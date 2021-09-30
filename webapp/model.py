from sqlalchemy import Column, Integer, String, DateTime, Text
from webapp.db import Base, engine

class News(Base):
        __tablename__ = 'news'
        id = Column(Integer, primary_key=True)
        title = Column(String, nullable=False)
        url = Column(String, unique=True, nullable=False)
        publish_date = Column(DateTime, nullable=False)
        text = Column(Text, nullable=True)
    
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

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)