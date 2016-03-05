from app import db
from models import BlogPost

#create database and the db tables
db.create_all()  #creates databases we import from models

#insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Flask", "discoverflask.com"))
db.session.add(BlogPost("postgres", "we set up a local postgres instance."))

#commit changes
db.session.commit()


