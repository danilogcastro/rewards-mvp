from flask import Flask
from config import Config
from flask_smorest import Api
from flask_migrate import Migrate
from flask_cors import CORS

import models

from db import db
from resources.transaction import blp as TransactionBlueprint
from resources.points import blp as PointsBlueprint

def create_app(db_url=None):
  app = Flask(__name__)
  CORS(app)

  app.config.from_object(Config)
  app.config.from_envvar('APPLICATION_SETTINGS')

  db.init_app(app)

  migrate = Migrate(app, db)
  api = Api(app)

  api.register_blueprint(TransactionBlueprint)
  api.register_blueprint(PointsBlueprint)

  return app