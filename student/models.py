from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
   
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=15)
    password = models.CharField(max_length=10)
    checkbox = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"
