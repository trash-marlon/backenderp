from rest_framework.viewsets import ModelViewSet
from con.models import Contact
from con.api.serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated

class ContactViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()