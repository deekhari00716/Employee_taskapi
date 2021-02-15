from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()


    class Meta:
        model = Task
        fields = ['id', 'title', 'memo', 'created', 'datecompleted']

class TaskCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id']
        read_only_fields = ['title', 'memo', 'created', 'datecompleted']
