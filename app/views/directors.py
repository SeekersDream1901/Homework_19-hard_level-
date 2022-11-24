from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.models.director import DirectorSchema
from decorators import auth_required, admin_required


directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@directors_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        request_json = request.json

        director_service.create(request_json)

        return "New director successfully added.", 201


@directors_ns.route('/<int:id>')
class DirectorView(Resource):
    @auth_required
    def get(self, id):
        director = director_service.get_one(id)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, id):
        request_json = request.json
        request_json["id"] = id

        director_service.update(request_json)

        return "Director updated successfully.", 204

    @admin_required
    def delete(self, id):
        director_service.delete(id)

        return "The director's data has been successfully deleted.", 204
