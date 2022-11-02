import imp
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, Project, Todo
from .serializers import UserModelSerialazer, ProjectModelSerialazer, TodoModelSerialazer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerialazer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerialazer


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerialazer
