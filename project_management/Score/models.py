from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def valid_point(val):
    if not val in [num for num in range(101)]:
        raise ValidationError('评分范围错误')


class Score(models.Model):
    user_id = models.IntegerField('user_id', db_column='user_id', max_length=10)
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
