from flask import Flask
from flask_cors import CORS
from api.view import users
def create_app():
    app=Flask(__name__)
    app.register_blueprint(users)
    CORS(app,origins="*")
    return app
