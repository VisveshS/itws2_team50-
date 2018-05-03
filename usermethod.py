from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///./database/users.db'
db=SQLAlchemy(app)
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80) ,unique=False, nullable=False)
    private=db.Column(db.String(80),unique=False,nullable=False)
    public=db.Column(db.String(800),unique=False,nullable=False)
    following=db.Column(db.String(80),unique=False,nullable=False)
    followedBy=db.Column(db.String(80),unique=False,nullable=False)
