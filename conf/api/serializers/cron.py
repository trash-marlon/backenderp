from rest_framework import serializers
from conf.models import Cron

class CronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cron
        fields = '__all__'