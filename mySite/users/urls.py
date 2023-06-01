from django.urls import path
from . import views


urlpatterns = [
    path('student-login/', views.student_login, name='s-login'),
    path('teacher-login/', views.teacher_login, name='t-login'),
    path('logout/',views.logout_view,name='logout')
]
