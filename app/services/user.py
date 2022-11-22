import hashlib
import base64
import hmac

from app.dao.user import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, user_id):
        return self.dao.get_one(user_id)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        user_id = data.get("id")
        user = self.get_one(user_id)

        user.name = data.get("name")

        self.dao.update(user)

    def delete(self, user_id):
        return self.dao.delete(user_id)

    def get_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_password(self, password_hash, request_password):
        return hmac.compare_digest(
            base64.b64decode(password_hash),
            hashlib.pbkdf2_hmac('sha256',
                                request_password.encode('utf-8'),
                                PWD_HASH_SALT,
                                PWD_HASH_ITERATIONS)
        )
