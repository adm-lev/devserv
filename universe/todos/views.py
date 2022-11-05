from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import User, Project, Todo
from .serializers import UserModelSerialazer, ProjectModelSerialazer, TodoModelSerialazer
from .filters import TodoFilter, ProjectFilter
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectCustomViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerialazer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination


class TodoCustomViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerialazer
    filterset_class = TodoFilter
    pagination_class = TodoLimitOffsetPagination

    def destroy(self, request, pk):
        instance = get_object_or_404(Todo, pk=pk)            
        instance.is_active = False        
        instance.save()
        todo = Todo.objects.all()       
        serialilzer_class = TodoModelSerialazer(todo, many=True, context={'request': request})
        return Response(serialilzer_class.data)


class UserCustomViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerialazer
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


