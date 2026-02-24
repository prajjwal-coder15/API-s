from extensions import mongo, bcrypt
from bson.objectid import ObjectId


class UserModel:

    @staticmethod
    def create_user(username, password):
        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")

        user = {
            "username": username,
            "password": hashed_pw
        }

        result = mongo.db.users.insert_one(user) # type: ignore
        return str(result.inserted_id)

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({"username": username}) # type: ignore

    @staticmethod
    def find_by_id(user_id):
        return mongo.db.users.find_one({"_id": ObjectId(user_id)}) # type: ignore

    @staticmethod
    def verify_password(stored_password, provided_password):
        return bcrypt.check_password_hash(stored_password, provided_password)