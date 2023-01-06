from rest_framework.viewsets import ModelViewSet
from sal.models import SaleOrderLine
from sal.api.serializers import SaleOrderLineSerializer
from rest_framework.permissions import IsAuthenticated

class SaleOrderLineViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SaleOrderLineSerializer
    queryset = SaleOrderLine.objects.all()