from rest_framework.viewsets import ModelViewSet
from conf.api.serializers import ParameterSerializer
from rest_framework.permissions import IsAuthenticated
from conf.models import Parameter

class ParameterViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ParameterSerializer
    queryset = Parameter.objects.all()