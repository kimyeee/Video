# coding: utf-8
import redis
from lagou.settings import REDIS_CONFIG

redis_valid_time = 60 * 60


class RedisClient:

    @property
    def redis_client(self):
        client = redis.Redis(host=REDIS_CONFIG['host'], port=REDIS_CONFIG['port'])
        return client

    def get_instance(self, key, delete_cache=False):
        redis_instance = self.redis_client.get(key)
        if not redis_instance:
            return None
        try:
            res = eval(redis_instance)
        except:
            res = str(redis_instance, encoding='utf-8')
        if delete_cache:
            self.redis_client.delete(key)
        return res

    def set_instance(self, key, value, default_valid_time=redis_valid_time):
        self.redis_client.set(key, value, default_valid_time)
        return

    def delete(self, key):
        self.redis_client.delete(key)
        return

    def incr_instance(self, key, amount=1):
        self.redis_client.incr(key, amount)
        return

    def decr_instance(self, key, amount=1):
        self.redis_client.decr(key, amount)
        return

    def sadd(self, name, *value):
        """根据key添加数据到集合set（set类型数据操作）"""
        self.redis_client.sadd(name, *value)
        return

    def sismember(self, name, value):
        """判断集合name中是否存在value元素（set类型数据操作）"""
        return self.redis_client.sismember(name, value)


redis_client = RedisClient()
