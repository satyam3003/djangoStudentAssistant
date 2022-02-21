from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='course-home'),
    path('course/<str:course>', views.course_detail, name='course'),
    path('lecture/<int:lecture_id>', views.lecture, name = 'lecture')
]
