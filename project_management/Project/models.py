from django.db import models


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
