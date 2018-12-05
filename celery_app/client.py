import datetime
from datetime import timedelta

from celery_app import task1
from celery_app import task2

task1.add.apply_async(args=[2, 8])  # 也可用 task1.add.delay(2, 8)
task2.multiply.apply_async(args=[3, 7])  # 也可用 task2.multiply.delay(3, 7)
print('hello world')

# countdown：指定多少秒后执行任务
task1.add.apply_async(args=(2, 23), countdown=5)  # 5 秒后执行任务
task1.add.apply_async(args=[6, 7], expires=10)  # 10 秒后过期

# 当前 UTC 时间再加 10 秒后执行任务
# task1.add.multiply.apply_async(args=[8, 7], eta=datetime.utcnow() + timedelta(seconds=10))
# task1.add.apply_async(args=[8, 7], eta=datetime.utcnow() + timedelta(seconds=10))
# expires：任务过期时间，参数类型可以是 int，也可以是 datetime
# task1.add.multiply.apply_async(args=[6, 7], expires=10)  # 10 秒后过期
# task1.add.apply_async(args=[6, 7], expires=10)  # 10 秒后过期
