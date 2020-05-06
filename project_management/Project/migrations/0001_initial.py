# Generated by Django 3.0.6 on 2020-05-06 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=100, unique=True, verbose_name='项目名称')),
                ('start_time', models.DateField(auto_now=True, verbose_name='创建时间')),
                ('end_time', models.DateField(blank=True)),
                ('department_ids', models.CharField(db_column='department_ids', max_length=200, verbose_name='部门id')),
                ('person_ids', models.CharField(db_column='person_ids', max_length=200, verbose_name='员工id')),
                ('is_done', models.BooleanField(db_column='is_done', default=False, verbose_name='是否结束')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 'project',
            },
        ),
    ]