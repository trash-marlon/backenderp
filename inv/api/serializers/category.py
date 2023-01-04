from rest_framework import serializers
from inv.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ['name', 'state', 'fc', 'fm', 'uc', 'um']