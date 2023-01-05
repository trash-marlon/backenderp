from rest_framework.viewsets import ModelViewSet
from conf.models import Configuration
from conf.api.serializers import ConfigurationSerializer
from rest_framework.permissions import IsAuthenticated

class ConfigurationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()