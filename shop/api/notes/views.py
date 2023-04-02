from rest_framework import viewsets


from api.notes.serializers import NoteModelSerializer
from notes.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed.
    """

    queryset = Note.objects.all().order_by("-title")
    serializer_class = NoteModelSerializer
    permission_classes = []
