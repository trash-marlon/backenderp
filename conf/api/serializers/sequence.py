from rest_framework import serializers
from conf.models import Sequence

class SequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sequence
        fields = '__all__'