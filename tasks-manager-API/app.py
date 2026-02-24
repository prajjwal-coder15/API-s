from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
from bson.objectid import ObjectId
import os

load_dotenv()

app = Flask(__name__)

# Config
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

mongo = PyMongo(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# --------------------
# REGISTER
# --------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if mongo.db.user.find_one({"username": data["username"]}): # type: ignore
        return jsonify({"msg": "User already exists"}), 400

    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    mongo.db.users.insert_one({ # type: ignore
        "username": data["username"],
        "password": hashed_pw
    })

    return jsonify({"msg": "User registered"}), 201

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Task Manager API!"

# --------------------
# LOGIN
# --------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = mongo.db.users.find_one({"username": data["username"]}) # type: ignore

    if not user or not bcrypt.check_password_hash(user["password"], data["password"]):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user["_id"]))
    return jsonify(access_token=access_token)


# --------------------
# CREATE TASK
# --------------------
@app.route("/tasks", methods=["POST"])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()

    mongo.db.tasks.insert_one({ # type: ignore
        "user_id": ObjectId(user_id),
        "title": data["title"],
        "completed": False
    })

    return jsonify({"msg": "Task created"}), 201


# --------------------
# GET USER TASKS
# --------------------
@app.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()

    tasks = []
    for task in mongo.db.tasks.find({"user_id": ObjectId(user_id)}): # type: ignore
        tasks.append({
            "id": str(task["_id"]),
            "title": task["title"],
            "completed": task["completed"]
        })

    return jsonify(tasks)
# --------------------
# complete USER TASKS
# --------------------
@app.route("/tasks/<task_id>/complete", methods=["PUT"])
@jwt_required()
def complete_task(task_id):
    user_id = get_jwt_identity()

    result = mongo.db.tasks.update_one( # type: ignore
        {"_id": ObjectId(task_id), "user_id": ObjectId(user_id)},
        {"$set": {"completed": True}}
    )

    if result.matched_count == 0:
        return jsonify({"msg": "Task not found or not owned by user"}), 404

    return jsonify({"msg": "Task completed"}), 200

if __name__ == "__main__":
    app.run(debug=True)