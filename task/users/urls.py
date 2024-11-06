from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Убедитесь, что этот маршрут существует
    path('login/', views.login_view, name='login'),  # маршрут для входа
    path('profile/', views.profile, name='profile'),  # маршрут для профиля
    path('logout/', LogoutView.as_view(), name='logout'),  # маршрут для выхода
    path('profile/edit/', views.edit_profile, name='edit_profile')
]


