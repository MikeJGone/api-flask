from django.db import models
from django.core.exceptions import ValidationError


def valid_age(value: int):
    if not value >= 1 and value <= 100:
        raise ValidationError('年龄不能小于1大于100岁')


# Create your models here.
class User(models.Model):
    uid = models.AutoField('工号', db_column='uid', primary_key=True)
    name = models.CharField('姓名', db_column='name', max_length=30)
    sex = models.BooleanField('性别', db_column='sex', default=True)
    age = models.SmallIntegerField('年龄', db_column='age', validators=(valid_age,))
    telephone = models.IntegerField('电话', db_column='telephone')
    job_level = models.SmallIntegerField('职级id', db_column='level')
    department_ids = models.CharField('部门id', db_column='department_ids', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
