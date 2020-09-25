from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from api.config import config_factory


db = SQLAlchemy()

def create_app(environ='default'):
    """Flask Application creation method used to hot load a new app with different environments

    Args:
        environ (str, optional): Environment indicator used to help set config. Defaults to 'default'.
    """
    config_object = config_factory.get(environ) or config_factory['default']
    app = Flask(__name__)
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return jsonify({'success': True, 'message': 'hello world!'})

    db.init_app(app)

    return app
