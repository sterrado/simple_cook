from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
import os
from .db import db

from .controllers.auth_controller import auth_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', None)
    jwt = JWTManager(app)

    # app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI", None)
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # db.init_app(app)

    
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    
    return app

application = create_app()
