from django.urls import path
from . import views

urlpatterns = [
    path('get/', views.attendance_list),
    path('is_enroll/', views.enrolled_list)
]
