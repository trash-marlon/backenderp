from rest_framework import serializers
from con.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = ['name', 'state', 'fc', 'fm', 'uc', 'um']