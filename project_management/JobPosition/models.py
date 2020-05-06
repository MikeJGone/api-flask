from django.db import models
from django.core.exceptions import ValidationError


def valid_level(value: int):
    if not value in [x for x in range(1, 5)]:
        raise ValidationError('年龄不能小于1大于100岁')


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
