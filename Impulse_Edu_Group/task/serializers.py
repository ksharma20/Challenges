from rest_framework import serializers
from task.models import UData

#Serializers
class UDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UData
        fields = ['id', 'name', 'description', 'email', 'createdAt']