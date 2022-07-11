from json import loads

from rest_framework import serializers

from django_celery_results.models import TaskResult

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = (
            'created_at',
            'updated_at',
        )


class TaskResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskResult
        fields = (
            'task_id',
            'status',
            'result',
            'date_done',
            'date_created',
        )
