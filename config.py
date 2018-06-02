# -*- coding: utf-8 -*-
import os
import urllib.parse

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'verysecretvalue'

SITE_NAME = 'Room Booking System'

# DB connection string
connStr = "Driver=ODBC Driver 17 for SQL Server;Server=tcp:databaseproject777.database.windows.net;port=1433;" \
          "uid=Marcin;pwd=projekt.BD2.1;database=test_database;"

SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect={}".format(urllib.parse.quote(connStr))
SQLALCHEMY_TRACK_MODIFICATIONS = False
