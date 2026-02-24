from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.task_model import TaskModel

task_bp = Blueprint("tasks", __name__)


@task_bp.route("/", methods=["POST"])
@jwt_required()
def create_task():
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data or not data.get("title"):
        return jsonify({"msg": "Task title required"}), 400

    task_id = TaskModel.create_task(user_id, data["title"])

    return jsonify({"msg": "Task created", "task_id": task_id}), 201


@task_bp.route("/", methods=["GET"])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()

    tasks = TaskModel.get_tasks_by_user(user_id)

    return jsonify(tasks), 200


@task_bp.route("/<task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    user_id = get_jwt_identity()
    data = request.get_json()

    result = TaskModel.update_task(task_id, user_id, data)

    if result.matched_count == 0:
        return jsonify({"msg": "Task not found"}), 404

    return jsonify({"msg": "Task updated"}), 200


@task_bp.route("/<task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    user_id = get_jwt_identity()

    result = TaskModel.delete_task(task_id, user_id)

    if result.deleted_count == 0:
        return jsonify({"msg": "Task not found"}), 404

    return jsonify({"msg": "Task deleted"}), 200