from extensions import mongo
from bson.objectid import ObjectId
from flask_pymongo.wrappers import Database

class TaskModel:

    @staticmethod
    def create_task(user_id, title):
        task = {
            "user_id": ObjectId(user_id),
            "title": title,
            "completed": False
        }

        result = mongo.db.tasks.insert_one(task)  # type: ignore
        return str(result.inserted_id)

    @staticmethod
    def get_tasks_by_user(user_id):
        tasks = mongo.db.tasks.find({"user_id": ObjectId(user_id)})  # type: ignore

        return [
            {
                "id": str(task["_id"]),
                "title": task["title"],
                "completed": task["completed"]
            }
            for task in tasks
        ]

    @staticmethod
    def update_task(task_id, user_id, data):
        return mongo.db.tasks.update_one(  # type: ignore
            {
                "_id": ObjectId(task_id),
                "user_id": ObjectId(user_id)
            },
            {
                "$set": {
                    "title": data.get("title"),
                    "completed": data.get("completed", False)
                }
            }
        )

    @staticmethod
    def delete_task(task_id, user_id):
        return mongo.db.tasks.delete_one( # type: ignore
            {
                "_id": ObjectId(task_id),
                "user_id": ObjectId(user_id)
            }
        )