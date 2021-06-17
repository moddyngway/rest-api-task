from django.http import HttpResponse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Course
from .serializers import CoursesSerializer
import requests


class CourseDetailAPIView(APIView):
    def get(self, request, pk):
        course = get_object_or_404(Course.objects.all(), pk=pk)
        serializer = CoursesSerializer(course, many=False)
        return Response({"course": serializer.data})

    def delete(self, request, pk):
        article = get_object_or_404(Course.objects.all(), pk=pk)
        article.delete()
        return Response({
            "message": "Course with id `{}` has been deleted.".format(pk)
        }, status=204)


class CourseAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()

        serializer = CoursesSerializer(courses, many=True)
        return Response({"courses": serializer.data})

    def post(self, request):
        course = request.data.get('course')
        # Create an article from the above data
        serializer = CoursesSerializer(data=course)
        if serializer.is_valid(raise_exception=True):
            course_saved = serializer.save()
        return Response({"success": "Course '{}' created successfully".format(course_saved.title)})


def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')