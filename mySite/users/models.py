from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    isTeacher = models.BooleanField(default=False)
    rfid_code = models.CharField(max_length=20, default="XXXXXXXX")
    def __str__(self):
        return f'{self.user.username} is a Student'

class Teacher(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    department = models.CharField(max_length=47)
    isTeacher = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.user.username} is a teacher'

