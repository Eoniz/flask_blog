import pytest
import string
import random
from app import app
from app.mod_auth.models import User


@pytest.fixture
def client(request):
    test_client = app.test_client()

    return test_client


def id_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def test_login_view(client):
    """
    GIVEN a Flask test client
    WHEN the '/auth/login' page is requested (GET)
    THEN check the status code is valid
    """
    response = client.get('/auth/login')
    assert response.status_code == 200


def test_add_user():
    """
    GIVEN a User Model
    WHEN a new User is created
    THEN check fields are defined correctly
    """

    id = id_generator()
    user = User(f"Eoniz{id}", f"nathan.artisien{id}@gmail.com", "password123")
    user.save()

    email = f"nathan.artisien{id}@gmail.com".lower()
    added_user = User.query.filter_by(email=email)\
        .first()

    assert added_user.id == user.id
    assert added_user.email == user.email
    assert added_user.name == user.name
    assert added_user.password == user.password

    added_user.remove()


def test_remove_user():
    """
    GIVEN a User Model
    WHEN a new User is removed
    THEN check user is not in the db
    """

    user = User("Removable", "Removable.Removable@gmail.com", "password123")
    user.save()
    user.remove()

    removed_user = User.query.filter_by(email="Removable.Removable@gmail.com")\
        .first()

    assert removed_user is None
