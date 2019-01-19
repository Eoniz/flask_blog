from app.mod_blog.models import Blog
import pytest
from app import app


@pytest.fixture
def client(request):
    test_client = app.test_client()

    return test_client


def test_index(client):
    """
    GIVEN a Flask test client
    WHEN the '/' page is requested (GET)
    THEN check the status code is valid
    """
    response = client.get('/')
    assert response.status_code == 200


def test_new_article():
    """
    GIVEN a Blog Model
    WHEN a new Blog is created
    THEN check the title and description are defined correctly
    """

    blog = Blog("New Article", "Article's description")
    assert blog.title == "New Article"
    assert blog.body == "Article's description"