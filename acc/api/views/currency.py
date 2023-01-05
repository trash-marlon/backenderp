from rest_framework.viewsets import ModelViewSet
from acc.models import Currency
from acc.api.serializers import CurrencySerializer
from rest_framework.permissions import IsAuthenticated

class CurrencyViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()