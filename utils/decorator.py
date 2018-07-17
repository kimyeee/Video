# coding: utf-8
import datetime
import functools
import logging

logger = logging.getLogger('django')


def compute_run_time(func):
    """
    计算函数执行时间装饰器
    :param func:
    :return:
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        func(*args, **kwargs)
        over_time = datetime.datetime.now()
        total_time = (over_time - start_time).total_seconds()
        logger.info('-' * 60)
        logger.info('函数' + func.__name__ + '运行共计 %s 秒' % total_time)
        logger.info('-' * 60)
    return wrapper
