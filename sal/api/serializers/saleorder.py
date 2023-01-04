from rest_framework import serializers
from sal.models import SaleOrder

class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = '__all__'