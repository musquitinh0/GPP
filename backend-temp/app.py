from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://<username>:<password>@localhost/<database>'
db = SQLAlchemy(app)

from routes import user_routes
app.register_blueprint(user_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run()
