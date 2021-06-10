from rest_framework import routers
from django.urls import path
from .views import CourseAPIView, CourseDetailAPIView


urlpatterns = [
    path('course/', CourseAPIView.as_view()),
    path('course/<int:pk>', CourseDetailAPIView.as_view()),
]
