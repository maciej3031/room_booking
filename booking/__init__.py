# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)
app.config.from_object('config')

# DB connection setup
db = SQLAlchemy(app)

# Automap DB scheme to SQL ORM
Base = automap_base()
Base.prepare(db.engine, reflect=True)

from booking import views
