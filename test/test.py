import pytest
import peewee
from db.user import User
from app import app


@pytest.fixture
def client():
    app.config["TEST"] = True
    db = peewee.SqliteDatabase(":memory")
    db.create_tables([User], safe=True)

    with app.test_client() as client:
        yield client


def test_new_user():
    user = User()
    user.id = 20
    user.name = "scratch_user@scratch.com"

    assert user.email == "scratch_user@scratch.com"
    assert user.id == 20


def test_create_user():
    response = client.post("/users", data={
        "id": 10,
        "name": "10th user"
    })

    assert response.status == 200


def test_get_user():
    response = client.get("/users/10")

    body: dict = response.json

    assert response.status == 200
    assert body["name"] == "10th user"


def test_get_all_users():
    response = client.get("/users")

    body: dict = response.json

    assert response.status == 200

    assert len(dict) == 1