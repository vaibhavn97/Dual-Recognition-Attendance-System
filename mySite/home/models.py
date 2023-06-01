from django.db import models
from users.models import Student, Teacher
import datetime

# Create your models here.
class Attendance(models.Model):
    date = models.DateField(default=datetime.date.today)
    subject = models.CharField(max_length=97)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='student')
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, related_name='teacher')

    def __str__(self):
        return f'{self.student.user.username}  {self.subject} {self.date}'

class Course(models.Model):
    course_name = models.CharField(max_length=97)
    semester = models.IntegerField(default=1)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='student_name')
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE, related_name='teacher_name')

    def __str__(self):
        return f'{self.student.user.username} is enroll for {self.course_name} taken by {self.teacher}'
