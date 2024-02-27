from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt          #For hashing passwords
from flask_login import LoginManager     #To handle log ins and manage user sessions
from flask_mail import Mail
from application.config import Config


# Extensions instances
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

# Login manager
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'  #To better style the login redirect message

mail = Mail()


def create_app(config_class=Config):
    # Create the flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from application.users.routes import users
    from application.posts.routes import posts
    from application.main.routes import main
    from application.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app