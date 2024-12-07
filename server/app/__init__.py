from flask import ( Flask,Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask_migrate import ( Migrate, )
from flask_sqlalchemy import ( SQLAlchemy, )
from app.config import get_config



# Initialize SQLAlchemy and Flask-Migrate globally
db = SQLAlchemy()
migrate = Migrate()

def create_app(config=get_config()):
    app = Flask(__name__)
    app.secret_key = config['SECRET_KEY']

    # Initialize Extensions
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route('/')
    def index():
        return 'Hello World!'

    return app