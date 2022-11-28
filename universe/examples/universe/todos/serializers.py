from dataclasses import fields
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import User, Project, Todo
import djangorestframework_camel_case

class UserModelSerialazer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectModelSerialazer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerialazer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'