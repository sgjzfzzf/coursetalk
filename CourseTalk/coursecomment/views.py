from django.shortcuts import render

from .models import *

# Create your views here.


def getCoursePage(request, courseId):
    courses = Course.objects.filter(course_id=courseId)
    if len(courses) == 0:
        return render(request, 'coursecomment/CourseNotFoundPage.html')
    else:
        teachers = [teacher_name
                    for teacher_name in Course.objects.values_list("course_teacher_name", flat=True)]
        comments = Comment.objects.filter(
            course__course_id=courseId).order_by('-comment_likes')
        return render(request, 'coursecomment/CoursePage.html', {"courses": courses, "teachers": teachers, "comments": comments})
