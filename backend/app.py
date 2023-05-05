import os
import urllib.parse as up
import psycopg2

from flask import Flask
from db import DatabaseManager
from config import DATABASE_URL

app = Flask(__name__)
url = up.urlparse(DATABASE_URL)
up.uses_netloc.append("postgres")
default_port = '5432'
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{url.username}:{url.password}@{url.hostname}:{default_port}/{url.path[1:]}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = DatabaseManager.get_db()
db.init_app(app)

if __name__ == '__main__':
    from routes import user_routes
    app.register_blueprint(user_routes, url_prefix='/api')

    app.run()