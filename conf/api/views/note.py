from rest_framework.viewsets import ModelViewSet
from conf.api.serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from conf.models import Note

class NoteViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer
    queryset = Note.objects.all()