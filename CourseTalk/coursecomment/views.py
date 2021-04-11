from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import *
import json

# Create your views here.


@require_http_methods(['GET'])
def getCoursePage(request, course_id):
    # 初始化课程界面
    try:
        course = Course.objects.filter(course_id=course_id)[0]
        course.teacher = None
    except IndexError:
        return render(request, 'coursecomment/ErrorPage.html')
    else:
        comments = Comment.objects.filter(course__course_id=course_id)
        teachers = [course.teacher for course in Course.objects.filter(
            course_id=course_id)]
        return render(request, 'coursecomment/CoursePage.html', {"course": course, "teachers": teachers, "comments": comments})


@require_http_methods(['GET'])
def getTeacherCoursePage(request, course_id, teacher_name):
    # 实现选择教师后课程界面的刷新
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
    # 返回渲染完成后的评论区HTML代码到JavaScript文件中
    return render(request, 'coursecomment/CommentsTemplate.html', {"course": course, "comments": comments})


@require_http_methods(['POST'])
def submitComment(request, course_id):
    comment_text = request.POST.get("comment_text")
    course_time = request.POST.get("course_time")
    course_score = request.POST.get("course_score")
    course_mark = request.POST.get("course_mark")
    comment = Comment.objetcs.create(
        user=request.user, course=Course.objects.get(course_id=course_id), course_time=course_time, course_score=course_score, course_mark=course_mark, comment_text=comment_text)
    comment.save()
    return getCoursePage(request, course_id)  # 待会儿重写


@require_http_methods(['GET'])
def addLike(request, comment_id):
    like = Like.objects.create(user=request.user, comment__id=comment_id)
    like.save()
