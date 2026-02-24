from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from typing import Optional

mongo: PyMongo = PyMongo()
jwt: JWTManager = JWTManager()
bcrypt: Bcrypt = Bcrypt()