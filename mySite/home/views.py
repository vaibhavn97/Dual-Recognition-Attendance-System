from django.shortcuts import render
from .models import Attendance
from users.models import Student
from django.db.models import Count

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def student_view(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        attendance = Attendance.objects.filter(subject=subject, student=Student.objects.get(user=request.user))
        total_lecture = len(Attendance.objects.values('date').filter(subject=subject).annotate(total=Count('date')))
        if total_lecture == 0: total_lecture = 1
        print(attendance)
        return render(request, 'home/attendance_s.html',  {
            'attendance' : attendance,
            'subject' : subject,
            'total_attend' : len(attendance),
            'total_lecture':total_lecture,
            'percentage': round((len(attendance)/total_lecture)*100, 2)
        })
    return render(request, 'home/attendance_s.html')

def teacher_view(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        date = request.POST['date']
        obj = Attendance.objects.filter(subject=subject, date=date)
        
        return render(request, 'home/attendance_t.html',  {
            'attendance' : obj
        })

    return render(request, 'home/attendance_t.html')