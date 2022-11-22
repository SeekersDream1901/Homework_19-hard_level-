
from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, director_id):
        return self.dao.get_one(director_id)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        director_id = data.get("id")
        director = self.get_one(director_id)

        director.name = data.get("name")

        self.dao.update(director)

    def delete(self, director_id):
        return self.dao.delete(director_id)
