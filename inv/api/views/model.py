from rest_framework.viewsets import ModelViewSet
from inv.models import Model
from inv.api.serializers import ModelSerializer
from rest_framework.permissions import IsAuthenticated

class ModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ModelSerializer
    queryset = Model.objects.all()