from app import create_app
from app.config import get_config

app = create_app()
config = get_config()



if __name__ == '__main__':
    app.run(debug=config['DEBUG'], port=config['PORT'])