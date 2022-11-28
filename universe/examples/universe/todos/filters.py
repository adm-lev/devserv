from django_filters import rest_framework as filters
from .models import Project, Todo


class ProjectFilter(filters.FilterSet):
    # name = filters.CharFilter(lookup_expr='contains')
    
    class Meta:
        model = Project
        fields = {
            'name': ['icontains']
        }


class TodoFilter(filters.FilterSet):
    # project__name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Todo
        fields = {
            'project__name': ['icontains']
        }
