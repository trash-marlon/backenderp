from rest_framework.viewsets import ModelViewSet
from inv.models import Uom
from inv.api.serializers import UomSerializer
from rest_framework.permissions import IsAuthenticated

class UomViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UomSerializer
    queryset = Uom.objects.all()