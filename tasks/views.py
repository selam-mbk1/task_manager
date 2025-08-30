from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from .forms import TaskForm



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk, owner=request.user)
        task.completed = True
        task.save()
        return Response({'status': 'task marked as complete'})

    @action(detail=True, methods=['post'])
    def incomplete(self, request, pk=None):
        task = get_object_or_404(Task, pk=pk, owner=request.user)
        task.completed = False
        task.save()
        return Response({'status': 'task marked as incomplete'})


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after signup
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'tasks/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'tasks/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def task_list_view(request):
    tasks = Task.objects.filter(owner=request.user)
    form = TaskForm()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})


@login_required
def task_toggle_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")
@login_required
def task_create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
def task_complete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.completed = True
    task.save()
    return redirect('task_list')


@login_required
def task_incomplete_view(request, pk):
    task = get_object_or_404(Task, pk=pk, owner=request.user)
    task.completed = False
    task.save()
    return redirect('task_list')
