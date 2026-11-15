"""Сериализаторы приложения api."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор модели задачи."""

    class Meta:
        """Метаданные сериализатора задачи."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
