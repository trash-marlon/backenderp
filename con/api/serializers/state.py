from rest_framework import serializers
from con.models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'