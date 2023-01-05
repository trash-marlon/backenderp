from rest_framework.viewsets import ModelViewSet
from conf.api.serializers import LogSerializer
from rest_framework.permissions import IsAuthenticated
from conf.models import Log

class LogViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LogSerializer
    queryset = Log.objects.all()