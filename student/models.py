from django.db import models
import os


def student_directory_name(instance, filename):
   
    return os.path.join('student/media/',instance.name, filename)

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
   
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=15)
    password = models.CharField(max_length=10)
    checkbox = models.BooleanField(default=False)
    photo = models.ImageField(upload_to= student_directory_name, blank=True, null=True, default=None)
    
    def __str__(self):
        return f"{self.name}"
