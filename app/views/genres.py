from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.models.genre import GenreSchema


genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    def post(self):
        request_json = request.json

        genre_service.create(request_json)

        return "New genre successfully added.", 201


@genres_ns.route('/<int:id>')
class GenreView(Resource):
    def get(self, id):
        genre = genre_service.get_one(id)
        return genre_schema.dump(genre), 200

    def put(self, id):
        request_json = request.json
        request_json["id"] = id

        genre_service.update(request_json)

        return "Genre updated successfully.", 204

    def delete(self, id):
        genre_service.delete(id)

        return "Genre deleted successfully", 204
