from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.movie import MovieDAO
from app.dao.user import UserDAO
from app.database import db
from app.services.auth import AuthService
from app.services.director import DirectorService
from app.services.genre import GenreService
from app.services.movie import MovieService
from app.services.user import UserService


movie_DAO = MovieDAO(db.session)
movie_service = MovieService(movie_DAO)

director_DAO = DirectorDAO(db.session)
director_service = DirectorService(director_DAO)

genre_DAO = GenreDAO(db.session)
genre_service = GenreService(genre_DAO)

user_DAO = UserDAO(db.session)
user_service = UserService(user_DAO)

auth_service = AuthService(user_service=user_service)
