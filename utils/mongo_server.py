# coding: utf-8
from pymongo import MongoClient
from CpBackend.settings import MONGODB_CONFIG
import logging

logger = logging.getLogger('Django')


class MongoDBClient:

    @property
    def mongo_client(self):
        client = MongoClient(host=MONGODB_CONFIG['host'], port=MONGODB_CONFIG['port'])
        db = client['cp_location']
        db['place'].ensure_index([('location', '2d')])
        return db['place']

    def insert(self, data):
        mongo_db = self.mongo_client
        try:
            res = mongo_db.insert(data)
        except Exception as e:
            logger.exception(e)
            res = 'MongoDB 异常'
        return res

    def update(self, old_data, new_data):
        mongo_db = self.mongo_client
        try:
            res = mongo_db.update(old_data, new_data)
        except Exception as e:
            logger.exception(e)
            res = 'MongoDB 异常'
        return res

    def find_all(self, condition=None, max_length=100):
        mongo_db = self.mongo_client
        try:
            res = mongo_db.find(condition).limit(max_length)
        except Exception as e:
            logger.exception(e)
            res = 'MongoDB 异常'
        return res

    def delete(self, data):
        mongo_db = self.mongo_client
        try:
            res = mongo_db.remove(data)
        except Exception as e:
            logger.exception(e)
            res = 'MongoDB 异常'
        return res


mongo_client = MongoDBClient()
