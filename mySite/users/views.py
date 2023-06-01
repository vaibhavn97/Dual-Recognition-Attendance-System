from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Student, Teacher


# Student Login
def student_login(request):
    # On Submiting Account Data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # Make sure user exist
        if user is not None :
            # Make Sure User is Student
            profile = Student.objects.filter(user=user)
            if len(profile)!=0 and profile[0] is not None and profile[0].isTeacher ==  False:
                login(request, user)
                return redirect('student-portal')
   
            else : return HttpResponse('You are not Student')

        else : return HttpResponse('Invalid Credentials')
    return render(request, 'users/login_s.html')


# Teacher Login
def teacher_login(request):
    # On Submitting Data
    if request.method == 'POST':
        username = request.POST['username']
        # Make Sure User exist
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None :
            # Make sure User is Teacher
            profile = Teacher.objects.filter(user=user)
            if len(profile)!=0 and profile[0] is not None and profile[0].isTeacher ==  True:
                login(request, user)
                return redirect('teacher-portal')
        
            else : return HttpResponse('You are not Teacher')
        
        else : return HttpResponse('Invalid Credentials')
    return render(request, 'users/login_t.html')

def logout_view(request):
    logout(request)
    return redirect("/")
