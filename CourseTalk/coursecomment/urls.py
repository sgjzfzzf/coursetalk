from django.urls import path

from . import views

urlpatterns = [
    path('course/<str:course_id>', views.getCoursePage,
         name="course_page"),  # 用于访问目标课程的URL，参数为课程号
    path('getTeacherCoursePage/<str:course_id>/<str:teacher_name>',
         views.getTeacherCoursePage, name="get_teacher_course_page"),  # 用于Ajax刷新教师有关信息的URL
    path('comment/<str:course_id>', views.submitComment, name="submit_comment"),
    path('addLike/<int:comment_id>', views.addLike, name="add_like"),
]
