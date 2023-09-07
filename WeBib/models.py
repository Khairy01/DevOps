from django.db import models

# Create your models here.
class Utilisateur(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  username = models.CharField(max_length=50)
  email = models.CharField(max_length=200,unique = True)

  def __str__(self) -> str:
      return f"{self.first_name} {self.last_name}"