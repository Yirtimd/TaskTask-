from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.task_list, name='task_list'),  # список задач
    path('create/', views.task_create, name='task_create'),  # создание задачи
    path('<int:pk>/edit/', views.task_edit, name='task_edit'),  # редактирование задачи
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),  # удаление задачи
]