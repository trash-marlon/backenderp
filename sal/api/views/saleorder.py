from rest_framework.viewsets import ModelViewSet
from sal.models import SaleOrder
from sal.api.serializers import SaleOrderSerializer
from rest_framework.permissions import IsAuthenticated

class SaleOrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SaleOrderSerializer
    queryset = SaleOrder.objects.all()