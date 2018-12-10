# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class LagouSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipeline(object):
    def __init__(self):
        pass

    def process_item(self, item, spider):
        return item

# class MySQLPipeline(object):
#     def __init__(self):
#         # 连接数据库
#         self.connect = pymysql.connect(
#             host='127.0.0.1',  # 数据库地址
#             port=3306,  # 数据库端口
#             db='test',  # 数据库名
#             user='root',  # 数据库用户名
#             passwd='root',  # 数据库密码
#             charset='utf8',  # 编码方式
#             use_unicode=True
#         )
#         # 通过cursor执行增删查改
#         self.cursor = self.connect.cursor()
#
#     def process_item(self, item, spider):
#         self.cursor.execute(
#             """insert into lagou(isbn, price,title)
#             VALUES (%s, %s,%s)""",  # 纯属python操作mysql知识，不熟悉请恶补
#             (item.get('isbn'),  # item里面定义的字段和表字段对应
#              item.get('price'),
#              item.get('title'),
#              ))
#         # 提交sql语句
#         ret = self.connect.commit()
#         return item  # 必须实现返回
#
#     def close_spider(self, spider):
#         # 关闭游标和连接
#         self.cursor.close()
#         self.connect.close()
