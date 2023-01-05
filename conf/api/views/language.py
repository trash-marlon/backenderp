from rest_framework.viewsets import ModelViewSet
from conf.api.serializers import LanguageSerializer
from rest_framework.permissions import IsAuthenticated
from conf.models import Language

class LanguageViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()