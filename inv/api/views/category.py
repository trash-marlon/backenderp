from rest_framework.viewsets import ModelViewSet
from inv.models import Category
from inv.api.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated

class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()