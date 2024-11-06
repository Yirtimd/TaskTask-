from django.db import models
from django.conf import settings


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)  # название задачи максимальная длина 200 символов
    description = models.TextField(blank=True)  # Описание задачи
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # дата последнего обновления
    is_completed = models.BooleanField(default=False)  # статус задачи (выполнена или нет)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # связь с пользователем

    def __str__(self):
        return self.title  # возвращаем название задачи при вызове str()