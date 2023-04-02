import pytest as pytest
from rest_framework.test import APIClient
from notes.models import Note


@pytest.mark.django_db
class TestNoteApi:
    def setup_method(self):
        self.client = APIClient()

    def test_note(self):
        response = self.client.get("/api/notes/")
        assert response.status_code == 200
        assert len(response.json()) == 0

        response = self.client.post("/api/notes/", data={"title": "title", "comment": "comment"})
        assert response.status_code == 201
        assert Note.objects.exists()

    def test_del_note(self):
        notes = Note.objects.create(title="title", comment="comment")

        response = self.client.get(f"/api/notes/{notes.id}/")
        assert response.status_code == 200
        assert response.json()["title"] == "title"

        response = self.client.delete(f"/api/notes/{notes.id}/")
        assert response.status_code == 204
        assert not Note.objects.exists()