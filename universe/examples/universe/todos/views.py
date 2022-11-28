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
from rest_framework.permissions import BasePermission, DjangoModelPermissions, IsAdminUser, IsAuthenticated, AllowAny, DjangoModelPermissionsOrAnonReadOnly
from universe.settings import SECRET_KEY
import logging
from rest_framework.decorators import permission_classes


logger = logging.getLogger(__name__)




class StaffOnly(BasePermission):
    def has_permission (self, request, view):
        return request.user.is_superuser


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectCustomViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Project.objects.all()
    logger.debug('YOYOOYOYO!!')
    serializer_class = ProjectModelSerialazer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination
    # permission_classes = [AllowAny]


class TodoCustomViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerialazer
    filterset_class = TodoFilter
    pagination_class = TodoLimitOffsetPagination
    permission_classes = [IsAuthenticated]

    def destroy(self, request, pk):
        instance = get_object_or_404(Todo, pk=pk)            
        instance.is_active = False        
        instance.save()
        todo = Todo.objects.all()       
        serialilzer_class = TodoModelSerialazer(todo, many=True, context={'request': request})
        return Response(serialilzer_class.data)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerialazer
    # permission_classes = [AllowAny]
    pagination_class = TodoLimitOffsetPagination


class UserCustomViewSet(mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerialazer
    pagination_class = TodoLimitOffsetPagination

    # @permission_classes([IsAuthenticated])
    # def list(self, request):
        
    #     if request.user and request.user.is_authenticated:
    #         # logger.debug('AUTHENTICATED!')
        

    #     # logger.debug('YOYOOYOYO!!')
    #         todo = User.objects.all()       
    #         serialilzer_class = UserModelSerialazer(todo, many=True, context={'request': request})
    #         return Response(serialilzer_class.data)
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # permission_classes = [AllowAny]






