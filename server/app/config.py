




def get_config():
    return {
        'DEBUG': True,
        # PRODUCTION WARNING: make sure to set this important information to a .env file
        # openssl rand -hex 32
        'SECRET_KEY': 'secret',
        'PORT': 8080,


        # PRODUCTION WARNING: make sure to set this important information to a .env file
        # MySQL: mysql+pymysql://username:password@hostname:port/database_name
        # PostgreSQL: postgresql+psycopg2://username:password@hostname:port/database_name
        # SQLite: sqlite:///database_name.db
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///app.db',
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    }