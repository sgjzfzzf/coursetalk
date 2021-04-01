from django.urls import path

from . import views

urlpatterns = [
    path('course/<str:course_id>', views.getCoursePage, name="course_page"),
    path('getTeacherCoursePage/<str:course_id>/<str:teacher_name>',
         views.getTeacherCoursePage, name="get_teacher_course_page"),
]
