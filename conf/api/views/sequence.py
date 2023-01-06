from rest_framework.viewsets import ModelViewSet
from conf.api.serializers import SequenceSerializer
from rest_framework.permissions import IsAuthenticated
from conf.models import Sequence

class SequenceViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SequenceSerializer
    queryset = Sequence.objects.all()