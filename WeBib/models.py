from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(User):
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Visit(models.Model):
    count = models.PositiveIntegerField(default=0)
