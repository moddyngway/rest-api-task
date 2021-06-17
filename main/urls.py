from rest_framework import routers
from django.urls import path
from .views import CourseAPIView, CourseDetailAPIView, index


urlpatterns = [
    path('', index),
    path('course/', CourseAPIView.as_view()),
    path('course/<int:pk>', CourseDetailAPIView.as_view()),
]
