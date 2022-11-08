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
from rest_framework.permissions import BasePermission, DjangoModelPermissions, IsAdminUser, IsAuthenticated
from universe.settings import SECRET_KEY




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
    serializer_class = ProjectModelSerialazer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination
    permission_classes = [IsAdminUser]


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


class UserCustomViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
    mixins.RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerialazer
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    # permission_classes = DjangoModelPermissions


# def authenticate_user(request):
 
#     email = request.data['email']
    
#     password = request.data['password']    
 
    
#     user = User.objects.get(email=email, password=password)
    
#     if user:
    
#         payload = jwt_payload_handler(user)
    
#         token = jwt.encode(payload, SECRET_KEY)
    
#         user_details = {}
    
#         user_details['name'] = "%s %s" % ( user.first_name, user.last_name)
    
#         user_details['token'] = token
    
#         user_logged_in.send(sender=user.__class__,request=request, user=user)
    
#     return Response(user_details, status=status.HTTP_200_OK)



