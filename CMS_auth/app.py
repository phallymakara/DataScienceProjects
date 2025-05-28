import os
import logging
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('flask_debug.log')
    ]
)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix
from config import Config

# Create a base class for declarative models
class Base(DeclarativeBase):
    pass

# Initialize SQLAlchemy with base class
db = SQLAlchemy(model_class=Base)

# Create the app
app = Flask(__name__)
app.config.from_object(Config)
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)  # needed for url_for to generate with https

# Initialize database
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

# Import user model for login manager
with app.app_context():
    from models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Create all database tables
    db.create_all()
    logging.info("Database tables created")

# Import routes
from routes import *
