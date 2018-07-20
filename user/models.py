# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    ROLE = (
        ('ADMIN', '管理员'),
        ('SALES', '销售部'),
        ('VIP', '销售部'),
        ('MEMBER', '销售部'),
    )
    name = models.CharField('姓名', max_length=100, null=True)
    username = models.CharField('用户名', max_length=50, unique=True)
    password = models.CharField(max_length=128, null=True)
    is_active = models.BooleanField('是否启用', default=True)
    role = models.CharField(choices=ROLE, max_length=30)
    channel_id = models.IntegerField(verbose_name='用户渠道信息', null=True)
    recommend_user = models.ForeignKey('self', verbose_name='推荐的用户', null=True)

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'user'
