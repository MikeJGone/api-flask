from flask_tt.config import redis_config
import redis
import json

pool = redis.ConnectionPool(host='localhost', port=6379, expression_times=3)
cache = redis.Redis(**redis_config)


def set_cache_data(key, value):
    data = json.dumps(value)
    cache.set(key, data)
    return


def get_cache_data(key):
    value = cache.get(key)
    if value:
        return json.loads(value)
    return


def clean_cache_data(key):
    cache.delete(key)
    return


def clean_cache_datas(key=""):
    keys = cache.keys(pattern=key + "*")
    for key in keys:
        cache.delete(key)
    return None


if __name__ == '__main__':
    clean_cache_datas()
