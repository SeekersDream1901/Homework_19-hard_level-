from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.models.movie import MovieSchema


movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        request_json = request.json

        movie_service.create(request_json)

        return "New movie has been added", 201


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    def get(self, id):
        movie = movie_service.get_one(id)
        return movie_schema.dump(movie), 200

    def put(self, id):
        request_json = request.json
        request_json["id"] = id

        movie_service.update(request_json)

        return "Movie data updated successfully.", 204

    def delete(self, id):
        movie_service.delete(id)

        return "Movie data deleted.", 204
