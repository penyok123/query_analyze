# coding=utf-8

data = open("file.txt", 'r')
print(data)

for item in data.readlines():
    print(item.split(")"))
