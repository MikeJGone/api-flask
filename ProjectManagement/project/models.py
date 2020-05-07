from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
class Project(models.Model):
    name = models.CharField('项目名称', db_column='name', max_length=100, unique=True)
    start_time = models.DateField('创建时间', auto_now=True)
    end_time = models.DateField(blank=True)
    department_ids = models.CharField('部门id', db_column='department_ids', max_length=200)
    person_ids = models.CharField('员工id', db_column='person_ids', max_length=200)
    is_done = models.BooleanField('是否结束', db_column='is_done', default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "project"
        verbose_name = "项目"
        verbose_name_plural = verbose_name


class Comment(models.Model):
    report_id = models.IntegerField('汇报id', db_column='report_id')
    message = models.CharField('吐槽', db_column='message', max_length=500)
    comment_uid = models.IntegerField("评论人id", db_column='comment_uid')
    comment_name = models.CharField("评论人名", db_column='comment_name', max_length=100)

    def __str__(self):
        return self.report_id

    class Meta:
        db_table = "comment"
        verbose_name = "评论"
        verbose_name_plural = verbose_name


class Report(models.Model):
    message = models.CharField('汇报信息', db_column='message', max_length=1000)
    image_url = models.CharField('图片地址', db_column='image_url', blank=True, max_length=100)
    video_url = models.CharField('视频地址', db_column='video_url', blank=True, max_length=100)
    project_id = models.IntegerField('项目id', db_column='project_id')
    creater = models.IntegerField('汇报人id', db_column='creater')
    create_time = models.DateField('创建时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "report"
        verbose_name = "汇报"
        verbose_name_plural = verbose_name


def valid_point(val):
    if not val in [num for num in range(101)]:
        raise ValidationError('评分范围错误')


class Score(models.Model):
    user_id = models.IntegerField('user_id', db_column='user_id')
    point = models.SmallIntegerField(validators=(valid_point,))
    project_id = models.IntegerField('项目id', db_column='project_id')
    create_time = models.DateField(auto_now=True)
    creater = models.IntegerField("评分人id", db_column='creater')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "score"
        verbose_name = "得分"
        verbose_name_plural = verbose_name
