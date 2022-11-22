import jwt
from flask import request
from flask_restx import abort

from constants import JWT_SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        pass