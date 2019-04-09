from redis import StrictRedis, ConnectionPool

# 两种不同的连接方式
# redis = StrictRedis(host='localhost', port=6379, db=0, password=123)
url = 'redis://:123@localhost:6379/0'
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.set('name_1', 'suofeiya')
print(redis.get('name'))
