from rest_framework.viewsets import ModelViewSet
from pur.models import PurchaseOrder
from pur.api.serializers import PurchaseOrderSerializer
from rest_framework.permissions import IsAuthenticated

class PurchaseOrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()