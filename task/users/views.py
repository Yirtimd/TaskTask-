from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, CustomUserChangeForm


def home(request):
    return render(request, 'home.html')  # Отображает шаблон главной страницы


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Проверка пользователя
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Успешный вход!")
            return redirect('profile')  # Или куда нужно перенаправить
        else:
            messages.error(request, "Неверное имя пользователя или пароль")

    return render(request, 'users/login.html')


#  это представление будет выводить профиль пользователя
@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') # перенаправляем на страницу профиля после сохранения
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {'form': form})












# def profile_view(request):
#     return render(request, 'users/profile.html') # отображаем страницу профиля


