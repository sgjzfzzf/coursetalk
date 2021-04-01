from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import *
import json

# Create your views here.


@require_http_methods(['GET'])
def getCoursePage(request, course_id):
    try:
        course = Course.objects.filter(course_id=course_id)[0]
        course.teacher = None
    except IndexError:
        return render(request, 'coursecomment/CourseNotFoundPage.html')
    else:
        comments = Comment.objects.filter(course__course_id=course_id)
        teachers = [course.teacher for course in Course.objects.filter(
            course_id=course_id)]
        return render(request, 'coursecomment/CoursePage.html', {"course": course, "teachers": teachers, "comments": comments})


@require_http_methods(['GET'])
def getTeacherCoursePage(request, course_id, teacher_name):
    if teacher_name == "None":
        try:
            course = Course.objects.filter(course_id=course_id)[0]
            course.teacher = None
        except IndexError:
            return HttpResponse("")
        else:
            comments = Comment.objects.filter(course__course_id=course_id)
    else:
        try:
            course = Course.objects.get(
                course_id=course_id, teacher__teacher_name=teacher_name)
        except Course.DoesNotExist:
            return HttpResponse("")
        else:
            comments = Comment.objects.filter(course=course)
    return render(request, 'coursecomment/CommentsTemplate.html', {"course": course, "comments": comments})
