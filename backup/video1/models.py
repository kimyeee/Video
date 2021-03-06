from django.db import models


# Create your models here.

class Video(models.Model):
    name = models.CharField('名称', max_length=64)
    cover = models.CharField('封面', max_length=128)
    actor = models.CharField('主演', max_length=32)
    type = models.CharField('类型', max_length=32)
    summarize = models.CharField('简介', max_length=1024)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'movie'
        ordering = ['-create_time']


class Tags(models.Model):
    name = models.CharField('', max_length=32)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'movie_tags'
        ordering = ['-create_time']
