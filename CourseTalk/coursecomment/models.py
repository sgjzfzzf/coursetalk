from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# 函数内容的具体在之后的开发工作总逐步完成


class UserInfo(models.Model):
    # Django自带的User类不方便修改，因此选择用一个UserInfo类储存我们额外需要的用户信息
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    mark_weight = models.FloatField()  # 用户评论的权重

    def get_mark_weight(self):
        # 计算用户对课程评价的权重分
        return


class Course(models.Model):
    course_id = models.CharField(max_length=20)  # 课程号
    course_name = models.CharField(max_length=20)  # 课程名
    course_teacher_name = models.CharField(max_length=8)  # 授课教师
    course_teacher_contact = models.EmailField()  # 授课教师联系方式
    course_colleage = models.CharField(max_length=20)  # 开课学院
    course_credit = models.IntegerField()  # 课程学分

    class Meta:
        unique_together = (('course_id', 'course_teacher_name',),)

    def __str__(self):
        return str(self.course_id)

    def liked_comment_number(self):
        # 返回对一门课程的平均评分
        courses = Course.objects.filter(
            course_id=self.course_id)
        mark = 0
        comment_num = 0
        for course in courses:
            for comment in course.comment_set.all():
                mark += comment.course_mark
                comment_num += 1
        return mark / comment_num

    def liked_teacher_comment_number(self):
        # 返回对某一位老师一门课程的平均评分
        comments = self.comment_set.all()
        mark = 0
        for comment in comments:
            mark += comment.course_mark
        return mark / len(comments)

    def average_score(self):
        # 返回某一门课程的平均成绩
        courses = Course.objects.filter(
            course_id=self.course_id)
        score = 0
        comment_num = 0
        for course in courses:
            for comment in course.comment_set.all():
                score += comment.course_score
                comment_num += 1
        return score / comment_num

    def teacher_average_score(self):
        # 返回某一位老师教授某一门课程的平均成绩
        comments = self.comment_set.all()
        score = 0
        for comment in comments:
            score += comment.course_score
        return score / len(comments)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_time = models.DateField()  # 授课时间
    course_score = models.FloatField()  # 课程最终得分，指评论用户的得分
    course_mark = models.FloatField()  # 对课程的评分
    comment_text = models.TextField()  # 对课程的文字评价
    comment_likes = models.IntegerField()  # 对评论的点赞数
    comment_time = models.DateTimeField(auto_now_add=True)  # 评论时间，已设置自动添加

    def __str__(self):
        return str(self.comment_text)
