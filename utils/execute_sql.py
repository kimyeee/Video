# coding: utf-8
from django.db import connection


def dict_fetchall(sql):
    cursor = connection.cursor()
    """将游标返回的结果保存到一个字典对象中"""
    cursor.execute(sql, None)
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()
    ]
