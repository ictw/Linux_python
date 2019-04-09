import json

# 使用dump将数据写入到json文件当中去.
# dumps用于将数据转换为json对象

json_test = [
    {
        'name': 'suofeiya',
        'age': 21,
        'num': 1024
    },
    {
        'name': 'python',
        'age': 23,
        'num': 1023
    }
]

json_str = json.dumps(json_test)
print(json_str)
with open('./Other/persons', 'w', encoding='UTF-8') as fp:
    json.dump(json_test, fp, ensure_ascii=False)

with open('./Other/persons', 'r', encoding='UTF-8') as fp:
    json_str = json.load(fp)
    for x in json_str:
        print(x)
