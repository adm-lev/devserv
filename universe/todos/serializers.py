from dataclasses import fields
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User, Project, Todo
import djangorestframework_camel_case

class UserModelSerialazer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ProjectModelSerialazer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerialazer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'