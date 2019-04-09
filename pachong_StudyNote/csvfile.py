import csv

with open('./Other/user.csv', 'r') as fp:
    # reader 是一个迭代器
    reader = csv.reader(fp)
    # next 从第二行开始遍历
    next(reader)
    for x in reader:
        print('name: ' + x[0])
        print('age: ' + x[1])

print('=' * 50)
with open('./Other/user.csv', 'r') as fp:
    reader = csv.DictReader(fp)
    for x in reader:
        # DictReader 可以通过key值来读取csv文件
        value = {'name': x['name'], 'age': x['age']}
        print(value)

# 写入csv文件
headers = ['name', 'age', 'num']
values = [
    ('suofeiya001', 21, 1),
    ('suofeiya002', 22, 2),
    ('suofeiya003', 21, 3)
]

with open('./Other/csvfile_1.csv', 'w', encoding='UTF-8') as fp:
    # 传入文件指针fp
    writer = csv.writer(fp)
    # 写入headers
    writer.writerow(headers)
    # 写入值
    writer.writerows(values)

with open('./Other/csvfile_2.csv', 'w', encoding='UTF-8') as fp:
    writer = csv.DictWriter(fp, headers)
    # 写入表头数据时需要使用writeheader()方法
    writer.writeheader()
    writer.writerows(values)
