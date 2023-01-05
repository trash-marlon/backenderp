from rest_framework import serializers
from acc.models import Tax

class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'