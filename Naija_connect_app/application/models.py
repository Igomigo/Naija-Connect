""" This module contains the database models """

from datetime import datetime, timedelta
import jwt
from application import db, login_manager
from flask_login import UserMixin
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """ The user class that holds user data """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    bio = db.Column(db.String(1000), default='Bio')
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(60), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        """ Method that gets a reset password token from jwt and uses it to
            send an encrypted email to the corresponding user requesting for
            password reset.
        """
        payload = {
            'user_id': self.id,
            'exp': datetime.utcnow() + timedelta(expires_sec)
        }
        return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_token(token):
        """ This method verifies and ensures that the token generated is what
            is returned in the request sent by the user via the reset link sent
            through the email by the app.
        """
        try:
            decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = decoded_token['user_id']
            return User.query.get(user_id)
        except:
            return None

    def __repr__(self):
        """ Returns a string representation of the class """
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.state}')"
    

class Post(db.Model):
    """ Post class for all user posts """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """ Returns a string representation of the class """
        return f"Post('{self.title}, '{self.date_posted}')"