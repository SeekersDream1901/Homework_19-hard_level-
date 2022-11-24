from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.models.movie import MovieSchema
from decorators import auth_required, admin_required


movies_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movies_ns.route("/")
class MoviesView(Resource):
    # @auth_required
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    @admin_required
    def post(self):
        request_json = request.json

        movie_service.create(request_json)

        return "New movie has been added", 201


@movies_ns.route('/<int:id>')
class MovieView(Resource):
    # @auth_required
    def get(self, id):
        movie = movie_service.get_one(id)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, id):
        request_json = request.json
        request_json["id"] = id

        movie_service.update(request_json)

        return "Movie data updated successfully.", 204

    @admin_required
    def delete(self, id):
        movie_service.delete(id)

        return "Movie data deleted.", 204
