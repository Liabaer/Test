# -*- coding: utf-8 -*-
import redis


class RedisClient(object):
    host = '127.0.0.1'
    port = 6379

    @staticmethod
    def create_redis_client():
        pool = redis.ConnectionPool(host=RedisClient.host, port=RedisClient.port, decode_responses=True)
        redis_client = redis.Redis(connection_pool=pool)
        return redis_client
