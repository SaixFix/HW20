from unittest.mock import MagicMock
import pytest

from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name="Bob")
    director_2 = Director(id=2, name="Ted")
    director_3 = Director(id=3, name="Fedor")

    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.create = MagicMock(return_value=Director(id=1))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        director = self.director_service.get_all()

        assert len(director) > 0

    def test_create(self):
        director_t = {
            "name": "Vasia",
        }

        director = self.director_service.create(director_t)

        assert director.id is not None

    def test_update(self):
        director_t = {
            "id": 1,
            "name": "Vasia",
        }

        self.director_service.update(director_t)

    def test_delete(self):
        self.director_service.delete(1)
