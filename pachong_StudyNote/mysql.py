import pymysql

conn = pymysql.connect(host='localhost', user='suofeiya', password='123', database='test', port=3306)
cursor = conn.cursor()
cursor.execute('select * from user')
result = cursor.fetchall()
# print(result)
for x in result:
    print(x)

# cursor.execute("""
# insert into user(username, email, password) values('eclipse','2440911975@qq.com','23')

# """)
sql = """
insert into user(username, email, password) values(%s,%s,%s)
"""

sql1 = """
insert into user(username, email, password) values(%s,%s,%s)
"""
username = 'pycharm1'
email = 'ictw@qq.com'
password = 789

cursor.execute(sql, (username, email, password))
cursor.execute(sql1, ("test", "2440911975@qq.com", "244"))
conn.commit()
conn.close()
