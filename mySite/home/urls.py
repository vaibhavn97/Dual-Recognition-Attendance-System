from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='hom'),
    path('student-portal', views.student_view, name='student-portal'),
    path('teacher-portal', views.teacher_view, name='teacher-portal'),
]