from flask import request
from flask_restx import Resource, Namespace

from app.container import user_service
from app.dao.models.user import UserSchema


user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        request_json = request.json

        user = user_service.create(request_json)

        return "New user successfully added.", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:id>')
class UserView(Resource):
    def get(self, id):
        user = user_service.get_one(id)
        return user_schema.dump(user), 200

    def put(self, id):
        request_json = request.json

        if "id" not in request_json:
            request_json["id"] = id

        user_service.update(request_json)

        return "User updated successfully.", 204

    def delete(self, id):
        user_service.delete(id)

        return "The user's data has been successfully deleted.", 204
