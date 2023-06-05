from rest_framework import serializers

from notes.models import Note


class NoteModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "comment", "created_at"]


class Serializer:
    pass
