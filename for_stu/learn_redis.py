# -*- coding: utf-8 -*-
import json

import redis

# 链接redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True)
# 获取redis客户端
redis_client = redis.Redis(connection_pool=pool)
# 设置一个key
redis_client.set("courier_package_1", "test")
# 获取key 对应的值
print(redis_client.get("courier_package_1"))
# 设置一个key,过期时间是100秒,ex参数是过期时间秒数
redis_client.set("expire_time", "1", ex=100)
# 也可以单独设置过期时间 下面两行代码等于上面一行
# redis_client.set("expire_time", "1")
# redis_client.expire("expire_time", time=100)
# 获取key 对应的值
print(redis_client.get("expire_time"))
# 获取key多少秒过期时间
print(redis_client.ttl("expire_time"))
# 删除key
redis_client.delete("expire_time")
# 如何复杂的数据结构设置到redis中
courier_online_list = [
    {
        'id': 1,
        'name': "yanxu"
    },
    {
        'id': 2,
        'name': "liabaer"
    }
]
# 直接这样设置会报错
# redis_client.set("courier_online_list", courier_online_list)
# 需要将复杂的数据结构装为字符串插入
# json.dumps将复杂的数据结构转换为字符串
courier_online_str = json.dumps(courier_online_list)
print(courier_online_str)
redis_client.set("courier_online_list", courier_online_str, ex= 60 * 60 * 24)

# 获取复杂的数据结构,获取到的是一个字符串，需要把他变为复杂的数据结构，才可以进行操作
courier_cache_str = redis_client.get("courier_online_list")
# 会报错，因为courier_cache_str是一个字符串
# for x in courier_cache_str:
#     print(x['id'], x['name'])
# json.loads 将字符串转变为对应的数据结构，这里转为了数组，数组中是字典
courier_cache_data = json.loads(courier_cache_str)
for x in courier_cache_data:
    print(x['id'], x['name'])


# 上面讲的是key value的redis使用，一个key,对应一个value
# 下面讲的是如何让一个key 对应一个set，这个set就是去重的list数组
# sadd是在key对应的集合中添加元素，可以传入字符串或者int类型，都会转换为字符串
redis_client.sadd("courier_uncompleted_order", "123456")
redis_client.sadd("courier_uncompleted_order", "123456")
redis_client.sadd("courier_uncompleted_order", "56278")
redis_client.sadd("courier_uncompleted_order", "56279")
# smembers获取数据，返回一个set集合
courier_uncompleted_order = redis_client.smembers("courier_uncompleted_order")
print(courier_uncompleted_order)
print(type(courier_uncompleted_order))
# 移除这个key对应的集合中的某个元素
redis_client.srem("courier_uncompleted_order", "56279")
courier_uncompleted_order = redis_client.smembers("courier_uncompleted_order")
print(courier_uncompleted_order)

# 获取集合的长度
courier_uncompleted_order_len = redis_client.scard("courier_uncompleted_order")
print(courier_uncompleted_order_len)