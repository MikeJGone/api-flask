from django.db import models
from django.core.exceptions import ValidationError


def valid_age(value: int):
    if not value >= 1 and value <= 100:
        raise ValidationError('年龄不能小于1大于100岁')


def valid_level(value: int):
    if value not in [x for x in range(1, 5)]:
        raise ValidationError('年龄不能小于1大于100岁')


# Create your models here.
class User(models.Model):
    uid = models.AutoField('工号', db_column='uid', primary_key=True)
    name = models.CharField('姓名', db_column='name', max_length=30)
    sex = models.BooleanField('性别', db_column='sex', default=True)
    age = models.SmallIntegerField('年龄', db_column='age', validators=(valid_age,))
    telephone = models.IntegerField('电话', db_column='telephone')
    job_level = models.SmallIntegerField('职级id', db_column='level', default=1)
    department_ids = models.CharField('部门id', db_column='department_ids', max_length=200, default='')
    password = models.CharField('密码', db_column='password', max_length=100, blank=True)
    is_work = models.BooleanField('是否在职',db_column='is_work',default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class JobPosition(models.Model):
    job_title = models.CharField('头衔', db_column='job_title', max_length=200)
    level = models.SmallIntegerField('级别', db_column='level', validators=(valid_level,))
    is_delete = models.BooleanField('删除标识', db_column='is_delete', default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "job_position"
        verbose_name = "职级"
        verbose_name_plural = verbose_name


class Department(models.Model):
    name = models.CharField('部门名称', db_column='name', max_length=100)
    admin_id = models.IntegerField("管理员id", db_column='admin_id')
    staff_ids = models.CharField('员工id', db_column='staff_ids', max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "department"
        verbose_name = "部门"
        verbose_name_plural = verbose_name
