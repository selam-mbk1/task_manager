from rest_framework import viewsets, permissions
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
