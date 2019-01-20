import pytest
import string
import random
from app import app
from app.mod_auth.models import User


@pytest.fixture
def client(request):
    test_client = app.test_client()

    return test_client


def test_login_view(client):
    """
    GIVEN a Flask test client
    WHEN the '/auth/login' page is requested (GET)
    THEN check the status code is valid
    """
    response = client.get('/auth/login')
    assert response.status_code == 200
