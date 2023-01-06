from rest_framework.viewsets import ModelViewSet
from inv.models import Location
from inv.api.serializers import LocationSerializer
from rest_framework.permissions import IsAuthenticated

class LocationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LocationSerializer
    queryset = Location.objects.all()