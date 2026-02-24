from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user_model import UserModel
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return jsonify({"msg": "Username and password required"}), 400

    if UserModel.find_by_username(data["username"]):
        return jsonify({"msg": "User already exists"}), 400

    user_id = UserModel.create_user(
        data["username"],
        data["password"]
    )

    return jsonify({"msg": "User created", "user_id": user_id}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = UserModel.find_by_username(data["username"])

    if not user:
        return jsonify({"msg": "User not found"}), 404

    if not UserModel.verify_password(user["password"], data["password"]):
        return jsonify({"msg": "Invalid credentials"}), 401

    access_token = create_access_token(identity=str(user["_id"]))

    return jsonify({
        "access_token": access_token
    }), 200