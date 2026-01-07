from rest_framework import serializers
from .models import item

class itemserializer(serializers.ModelSerializer):
    class Meta:
        model = item
        fields = '__all__'