from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
      return f"{self.first_name} {self.last_name}"

