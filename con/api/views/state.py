from rest_framework.viewsets import ModelViewSet
from con.models import State
from con.api.serializers import StateSerializer
from rest_framework.permissions import IsAuthenticated

class StateViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = StateSerializer
    queryset = State.objects.all()