from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Attendance, Course
from users.models import Student, Teacher
from django.contrib.auth.models import User
import datetime


@api_view(['GET', 'POST'])
def attendance_list(request):
    if request.method == 'POST':
        student_id = User.objects.get(username=request.data['student_id'].lower())
        student = Student.objects.get(user=student_id)
        teacher_id = User.objects.get(username=request.data['teacher_id'].lower())
        teacher = Teacher.objects.get(user=teacher_id)
        subject = request.data['subject']
        
        dataObj = Attendance.objects.filter(student=student, teacher=teacher, subject=subject, date=datetime.date.today())
        if len(dataObj) == 1:
            return Response("Already Marked")
        else:
            obj = Attendance()
            obj.student = Student.objects.get(user=student_id)
            obj.teacher = Teacher.objects.get(user=teacher_id)
            obj.subject = subject
            print("This Request is received")
            obj.save()
            return Response("Attendance is Marked")
        return Response("POST")

    elif request.method == 'GET':
        return Response("Send POST request please")
    

@api_view(['GET', 'POST'])
def enrolled_list(request):
    if request.method == 'GET':
        try :
            student_id = Student.objects.get(rfid_code=request.data['rfid_code'])
            print(student_id)
            subject = request.data['subject']
            try:
                obj = Course.objects.get(student = student_id, course_name=subject)
                return Response(student_id.user.username)
            except:
                return Response("NE")
        except:
            return Response("NS")
    else:
        return Response("Send GET request please")
    
