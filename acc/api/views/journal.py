from rest_framework.viewsets import ModelViewSet
from acc.models import Journal
from acc.api.serializers import JournalSerializer
from rest_framework.permissions import IsAuthenticated

class JournalViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()