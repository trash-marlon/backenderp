from rest_framework.viewsets import ModelViewSet
from inv.models import Brand
from inv.api.serializers import BrandSerializer
from rest_framework.permissions import IsAuthenticated

class BrandViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()