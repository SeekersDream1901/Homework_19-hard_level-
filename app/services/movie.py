
from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, movie_id):
        return self.dao.get_one(movie_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        movie_id = data.get("id")
        movie = self.get_one(movie_id)

        movie.trailer = data.get("trailer")
        movie.rating = data.get("rating")
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.year = data.get("year")
        movie.director_id = data.get("director_id")
        movie.genre_id = data.get("genre_id")
        movie.id = data.get("id")

        self.dao.update(movie)

    def delete(self, movie_id):
        return self.dao.delete(movie_id)
