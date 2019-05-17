from rest_framework import serializers
from HallNews.models import HallNew

#Lead serializer

class HallNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HallNew
        fields = '__all__'