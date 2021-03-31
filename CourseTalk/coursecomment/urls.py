from django.urls import path

from . import views

urlpatterns = [
    path('course/<str:courseId>', views.getCoursePage, name="course_page"),
]
