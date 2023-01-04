from rest_framework import serializers
from inv.models import Uom

class UomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uom
        fields = '__all__'