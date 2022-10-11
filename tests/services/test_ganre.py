from unittest.mock import MagicMock
import pytest

from dao.model.genre import Genre
from dao.genre import GenreDAO
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="horror")
    genre_2 = Genre(id=2, name="comedy")
    genre_3 = Genre(id=3, name="thriller")

    genre_dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.create = MagicMock(return_value=Genre(id=1))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()

        assert len(genre) > 0

    def test_create(self):
        genre_t = {
            "name": "Shisha",
        }

        genre = self.genre_service.create(genre_t)

        assert genre.id is not None

    def test_update(self):
        genre_t = {
            "id": 1,
            "name": "Shisha",
        }

        self.genre_service.update(genre_t)

    def test_delete(self):
        self.genre_service.delete(1)
