""" This module contains all configuration settings """

import os

class Config:
    # security key against CSRF(cross site request forgery)
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Database setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_DATABASE_URI')
    
    # Mail service setup
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "igomigofatai@gmail.com"
    MAIL_PASSWORD = os.environ.get('APP_EMAIL_PASSWORD')