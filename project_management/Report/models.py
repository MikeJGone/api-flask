from django.db import models


# Create your models here.
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
