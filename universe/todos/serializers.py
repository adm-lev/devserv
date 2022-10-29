from dataclasses import fields
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User

class UserModelSerialazer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'