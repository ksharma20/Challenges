from rest_framework import serializers
from .models import User, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['user', 'pk', 'name',
                  'description', 'created_at', 'completed']
