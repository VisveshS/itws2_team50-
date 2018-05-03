from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./database/songs.db'
db=SQLAlchemy(app)
class song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80), unique=False, nullable=True)
    name = db.Column(db.String(80), unique=False, nullable=True)
    image = db.Column(db.String(80), unique=False, nullable=True)
    priv = db.Column(db.String(200) ,unique=False, nullable=True)
    pub = db.Column(db.String(200) ,unique=False, nullable=True)    
# def funct():
#     db.create_all()
#     s1=song(name='abc')
#     db.session.add(s1)
#     db.session.commit()
