"""Регистрация моделей в административной панели Django."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Настройки отображения задач в админке."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
