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


def test_new_article_instance():
    """
    GIVEN a Blog Model
    WHEN a new Blog is created
    THEN check the title and description are defined correctly
    """

    blog = Blog("New Article", "Article's description")
    assert blog.title == "New Article"
    assert blog.body == "Article's description"


def test_adding_article_db():
    """
    Given a Blog Model
    WHEN a new blog is added to the db
    THEN check the title and description are defined correctly from the DB
    """
    added_blog = Blog("New Article", "Article's description").save()
    
    blog = Blog.query.filter_by(title="New Article").first()

    assert added_blog.id == blog.id
    assert added_blog.title == blog.title
    assert added_blog.body == blog.body
    assert added_blog.date_created == blog.date_created
    assert added_blog.date_modified == blog.date_modified

