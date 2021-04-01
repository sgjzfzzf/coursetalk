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


class Teacher(models.Model):
    # 授课老师的信息储存
    teacher_name = models.CharField(max_length=20, primary_key=True)  # 授课教师姓名
    teacher_contact = models.EmailField()  # 授课教师联系方式

    def __str__(self):
        return self.teacher_name


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.CharField(max_length=20)  # 课程号
    course_name = models.CharField(max_length=20)  # 课程名
    course_colleage = models.CharField(max_length=20)  # 开课学院
    course_credit = models.IntegerField()  # 课程学分

    class Meta:
        unique_together = (('course_id', 'teacher',),)

    def __str__(self):
        return str(self.course_id)

    def comment_mark(self):
        # 返回对一门课程的平均评分
        courses = Course.objects.filter(
            course_id=self.course_id)
        mark = 0
        comment_num = 0
        for course in courses:
            for comment in course.comment_set.all():
                mark += comment.course_mark
                comment_num += 1
        if comment_num == 0:
            return "No comments now."
        else:
            return mark / comment_num

    def teacher_comment_mark(self):
        # 返回对某一位老师一门课程的平均评分
        comments = self.comment_set.all()
        if len(comments) == 0:
            return 'No comments now.'
        else:
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
        if comment == 0:
            return "No comments now."
        else:
            return score / comment_num

    def teacher_average_score(self):
        # 返回某一位老师教授某一门课程的平均成绩
        comments = self.comment_set.all()
        if len(comments) == 0:
            return "No comments now."
        else:
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
    comment_time = models.DateTimeField(auto_now_add=True)  # 评论时间，已设置自动添加

    def __str__(self):
        return str(self.comment_text)

    def total_likes(self):
        # 返回一条评论的所有点赞数
        likes = self.like_set.all()
        return len(likes)


class Like(models.Model):
    # 赞的对象，引入这个对象是为了防止一条评论多个用户点赞的情况出现
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('user', 'comment',),)
