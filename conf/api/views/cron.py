from rest_framework.viewsets import ModelViewSet
from conf.api.serializers import CronSerializer
from rest_framework.permissions import IsAuthenticated
from conf.models import Cron

class CronViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CronSerializer
    queryset = Cron.objects.all()