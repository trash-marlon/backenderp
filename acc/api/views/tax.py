from rest_framework.viewsets import ModelViewSet
from acc.models import Tax
from acc.api.serializers import TaxSerializer
from rest_framework.permissions import IsAuthenticated

class TaxViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaxSerializer
    queryset = Tax.objects.all()