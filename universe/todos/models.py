from email.policy import default
from statistics import mode
from datetime import datetime as date
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=64, unique=True, help_text="Username")
    first_name = models.CharField(max_length=64, help_text="Firs tname")
    last_name = models.CharField(max_length=64, help_text="Last name")
    email = models.EmailField(max_length=64, blank=True, unique=True, help_text="User Email")

    def __str__(self) -> str:
        return f'{self.user_name} - ({self.last_name} {self.first_name})'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Project(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False, help_text='Project name')
    users = models.ManyToManyField(User, help_text='Project users')
    project_url = models.CharField(max_length=128, blank=True, help_text='Repo URL')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'



class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, help_text='Project')
    text = models.TextField(max_length=1000, blank=True, help_text='Note')
    date_created = models.DateTimeField(auto_now_add=True, help_text='Date created')
    date_updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, help_text='Date updated')
    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='Author')
    is_active = models.BooleanField(default=True, help_text='Is active')
    
    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
    # def __str__(self) -> str:
    #     return f'{self.user}'

    