from unittest.mock import MagicMock

import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    film_1 = Movie(id=1, title="pypy", description="vot tyt to i nachalas zavarushka",
                   trailer="ssilka", rating=2.1, genre_id=1, director_id=1)
    film_2 = Movie(id=2, title="Синяки в Огайо", description="Заходят два синяка в бар, а бармен их спрашивает...",
                   trailer="ssilka1", year=2002, rating=5.1, genre_id=1, director_id=1)
    film_3 = Movie(id=3, title="Рыбин Гуд", description="Он воровал селедку, но попался на сельдерей!",
                   trailer="ssilka3", year=2012, rating=3.1, genre_id=1, director_id=2)

    movie_dao.get_one = MagicMock(return_value=film_1)
    movie_dao.get_all = MagicMock(return_value=[film_1, film_2, film_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movie = self.movie_service.get_all()

        assert len(movie) > 0

    def test_create(self):
        movie_t = {
            "title": "Shisha",
            "description": "fifififif",
        }

        movie = self.movie_service.create(movie_t)

        assert movie.id is not None

    def test_update(self):
        movie_t = {
            "id": 1,
            "title": "Shisha",
            "description": "fifififif",
        }

        self.movie_service.update(movie_t)

    def test_delete(self):
        self.movie_service.delete(1)


