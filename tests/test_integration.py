import pytest
from httpx import Client


@pytest.fixture
def client():
    with Client(base_url="http://localhost:9000/") as ac:
        yield ac


def test_create_and_get_book(client):
    response = client.post(
        "/api/v1/books/",
        json={"title": "ML", "description": "Machine Learning"},
        headers={"X-API-Key": "2BEAC7CEF6B23CCA1F4BB7A938CF1"},
    )

    assert response.status_code == 201
    book = response.json()
    assert book["title"] == "ML"
    book_id = book["id"]

    response = client.get(
        f"/api/v1/books/{book_id}",
        headers={"X-API-Key": "2BEAC7CEF6B23CCA1F4BB7A938CF1"},
    )
    assert response.status_code == 200
    book = response.json()
    assert book["id"] == book_id
    assert book["title"] == "ML"


def test_create(client):
    response = client.post(
        "/api/v1/books/",
        json={"title": "Data Science", "description": "Prediction Bussiness"},
        headers={"X-API-Key": "2BEAC7CEF6B23CCA1F4BB7A938CF1"},
    )

    assert response.status_code == 201
    book = response.json()
    assert book["title"] == "Data Science"
