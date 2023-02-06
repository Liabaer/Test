# -*- coding: utf-8 -*-
import csv


f = open('item.csv', 'r', encoding='utf-8')
fr = csv.reader(f)
for i in fr:
    print(i)
f.close()
#
# f.close()
# csv_write = csv.writer(f)
# # 单行写入
# csv_write.writerow(['name', 'class', 'sex'])