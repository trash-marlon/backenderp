from rest_framework.viewsets import ModelViewSet
from con.models import Country
from con.api.serializers import CountrySerializer
from rest_framework.permissions import IsAuthenticated

class CountryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CountrySerializer
    queryset = Country.objects.all()