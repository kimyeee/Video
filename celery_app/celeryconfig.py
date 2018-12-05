from datetime import timedelta

from celery.schedules import crontab

BROKER_URL = "amqp://kim:kim@127.0.0.1:5672//"  # 指定 Broker
CELERY_RESULT_BACKEND = "redis://localhost:6379"  # 指定 Backend

CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'

CELERY_IMPORTS = (  # 指定导入的任务模块
    'celery_app.task1',
    'celery_app.task2'
)
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'celery_app.task1.add',
        'schedule': timedelta(seconds=3),  # 每 30 秒执行一次
        'args': (5, 8)  # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app.task2.multiply',
        'schedule': crontab(hour=9, minute=50),  # 每天早上 9 点 50 分执行一次
        'args': (3, 7)  # 任务函数参数
    }
}
