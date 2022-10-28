from email.policy import default
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models


# class Note(models.Model):
#     title = models.CharField(max_length=64, help_text="Note title")
#     note_text = models.TextField(help_text="Note text")
#     created = models.DateTimeField(help_text="Date created")
#     updated = models.DateTimeField(help_text="Date updated")
#     done = models.BooleanField(default='false', help_text="Note title")
#     author = models.ForeignKey()


class User(models.Model):
    user_name = models.CharField(max_length=64, unique=True, help_text="Username")
    first_name = models.CharField(max_length=64, help_text="Firs tname")
    last_name = models.CharField(max_length=64, help_text="Last name")
    email = models.EmailField(max_length=64, blank=True, unique=True, help_text="User Email")

    def __str__(self) -> str:
        return f'{self.user_name} - ({self.last_name} {self.first_name})'
    