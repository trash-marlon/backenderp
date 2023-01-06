from rest_framework.viewsets import ModelViewSet
from inv.models import Warehouse
from inv.api.serializers import WarehouseSerializer
from rest_framework.permissions import IsAuthenticated

class WarehouseViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WarehouseSerializer
    queryset = Warehouse.objects.all()