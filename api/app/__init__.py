import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from app import models
from app.models import User

u = User.query.get(1)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/user')
def get_first_user():
    return {'user': u.username}

