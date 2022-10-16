# -*- coding: utf-8 -*-
# 给你一个字符串 date ，按 YYYY-MM-DD 格式表示一个 现行公元纪年法 日期。返回该日期是当年的第几天。

date = "1900-05-02"

day_31 = [1, 3, 5, 7, 8, 10, 12]
day_30 = [4, 6, 9, 11]

i = 0
new_date = []
temp = ''
while i < len(date):

    if date[i] != '-':
        temp = temp + date[i]
    if date[i] == '-' and temp != ' ':
        new_date.append(temp)
        temp = ''
    i = i + 1
if temp != '':
    new_date.append(temp)
print(new_date)
num = 0
for i in range(1, int(new_date[1])):
    if i == 2:
        if int(new_date[0]) % 400 == 0 or (int(new_date[0]) % 4 == 0 and int(new_date[0]) % 100 != 0):
            num = num + 29
        else:
            num = num + 28
    if i in day_30:
        num += 30
    if i in day_31:
        num += 31
num += int(new_date[2])
print(num)
