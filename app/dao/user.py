
from app.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, user_id):
        return self.session.query(User).get(user_id)

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))

        user.username = user_d.get("username")
        user.password = user_d.get("password")

        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, user_id):
        user = self.get_one(user_id)

        self.session.delete(user)
        self.session.commit()
