# -*- coding: utf-8 -*-
# csv文件处理
import csv

# 读取csv文件
f = open('data.csv', 'r')
csv_f = csv.reader(f)
for i in csv_f:
    # i是每一列csv的数组
    print(i)
f.close()

# 新增csv文件
f = open('out.csv', 'w')
csv_write = csv.writer(f)
# 单行写入
csv_write.writerow(['name', 'class', 'sex'])
i = 0
row_list = [
    ['dayday', '2022', 'man'],
    ['tulian', '2022', 'wuman'],
    ['yanxu', '2022', 'wuman'],
    ['liabaer', '2022', 'man']
]
# 循环写入
while i < 4:
    csv_write.writerow(row_list[i])
    i = i + 1
f.close()