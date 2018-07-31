from django.db import models


# Create your models here.
class VideoClass(models.Model):
    video_class = models.CharField('视频类型', max_length=32)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'video_class'
        ordering = ['-create_time']


class Video(models.Model):
    v_class = models.ForeignKey(VideoClass)
    name = models.CharField('名称', max_length=128)
    cover = models.CharField('封面', max_length=128)
    online_time = models.DateField('上线时间',default="2018-08-01")
    actor = models.CharField('主演', max_length=64, default='暂无')
    video_url = models.CharField('视频地址', max_length=64,default=None)
    summarize = models.CharField('简介', max_length=1024)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'movie'
        ordering = ['-create_time']


class VideoType(models.Model):
    video_type = models.CharField('视频分类', max_length=32)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'video_type'
        ordering = ['-create_time']


class Video2Type(models.Model):
    video = models.ForeignKey(Video)
    type = models.ForeignKey(VideoType)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'video_2_type'
        ordering = ['-create_time']


class Tags(models.Model):
    name = models.CharField('', max_length=32)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'movie_tags'
        ordering = ['-create_time']
