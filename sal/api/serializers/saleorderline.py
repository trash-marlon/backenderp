from rest_framework import serializers
from sal.models import SaleOrderLine

class SaleOrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderLine
        fields = '__all__'