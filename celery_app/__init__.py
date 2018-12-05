#!/usr/bin/evn python
# coding=utf-8

from celery import Celery

app = Celery('demo')  # 创建 Celery 实例
app.config_from_object('celery_app.celeryconfig')
