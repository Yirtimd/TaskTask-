from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task


# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)  # получаем задачи связанные с данным пользователем

    # фильтрация задач по статусу
    status_filter = request.GET.get('статус')
    if status_filter:
        tasks = tasks.filter(status=status_filter)

    # фильтрация задач по приоритету
    priority_filter = request.GET.get('priority')
    if priority_filter:
        tasks = tasks.filter(priority=priority_filter)

    #  сортировка задач
    sort_by = request.GET.get('сортировать')
    if sort_by:
        tasks = tasks.order_by(sort_by)  # сортируем по выбраному параметру

    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # отображаем их на странице


@login_required
def task_create(request):
    if request.method == 'POST':  # если форма была отправлена
        form = TaskForm(request.POST)
        if form.is_valid():  # если форма валидна
            task = form.save(commit=False)  # не сохраняем в БД еще,а только создаем объект задачи
            task.user = request.user  # привязываем задачу к текущему пользователю
            task.save()  # сохраняем задачу в БД
            return redirect('tasks:task_list')  # перенаправляем на список задач
    else:
        form = TaskForm()  # если форма не была отправлена, создаем пустую форму

    return render(request, 'tasks/task_form.html', {'form': form})  # отображаем форму для создания задачи


@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # получаем задачу по первичному ключи (pk)
    if request.method == 'POST':  # если форма была отправлена
        form = TaskForm(request.POST, instance=task)  # заполняем форму существующими данными задачи
        if form.is_valid():  # если форма валидна
            form.save()  # сохраняем изменения задача
            return redirect('tasks:task_list')  # перенаправлянм на списк задач
    else:
        form = TaskForm(instance=task)  # если форма не была отпрвлена, создаем форму с данными задачами

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)  # Получаем задачу по pk
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')  # Перенаправляем на список задач после удаления
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})