from rest_framework.viewsets import ModelViewSet
from inv.models import Product
from inv.api.serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()