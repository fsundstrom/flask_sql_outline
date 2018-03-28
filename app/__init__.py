from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('config')
# use database test
db = SQLAlchemy(test)

# import flask views and database models
from app import views, models

