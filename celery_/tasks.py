import time
from celery import Celery

app = Celery('tasks', backend='amqp://guest@localhost', broker='amqp://guest@localhost//')


@app.task
def add(x, y):
    time.sleep(3)
    # print(x, y)
    # open(r'D:\project\Video\celery_\test.txt', 'w').write('test')
    return x + y


if __name__ == '__main__':
    result = add.delay(30, 42)
    print(result)
