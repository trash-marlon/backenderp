from rest_framework.viewsets import ModelViewSet
from crm.models import Lead
from crm.api.serializers import LeadSerializer
from rest_framework.permissions import IsAuthenticated

class LeadViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()