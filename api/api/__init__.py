from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from api.config import config_factory


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

from api.todos.models import Todo
from api.todos.routes import todo_bp


def create_app(environ='default'):
    """Flask Application creation method used to hot load a new app with different environments

    Args:
        environ (str, optional): Environment indicator used to help set config. Defaults to 'default'.
    """
    config_object = config_factory.get(environ) or config_factory['default']
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Help class late intialization due to app factory pattern 
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # Blue print registration
    app.register_blueprint(todo_bp)

    return app
