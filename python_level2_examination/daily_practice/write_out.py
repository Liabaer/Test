# -*- coding: utf-8 -*-
# 其中第1列是操作的名字，第2列是操作所花费的时 间，单位是秒，第3列是操作时间占全部过程的百 分比，字段之间用逗号，隔开。
# 读取out.txt文件里的内容，统计所有操作所花费的 时间总和，并输出操作时间百分比最多的三个操作 所占百分比的值，及其对应的操作名称，显示在屏 幕上，
# 在...上补充一行或者多行代码
# 在——————上补充一行代码

sumtime = 0
ts = {}
with open('../data/out.txt', 'r') as f:
    f = f.readlines()
    for i in f:
        sumtime += float(i.split(',')[1])
        key = i.split(',')[0]
        ts[key] = float(i.split(',')[2])
print('the total execute time is ', sumtime)
print(ts)
tns = list(ts.items())

# 对tns数组排序 key参数表排序规则 x[1]表示对二维数组的第二维排序
# 举例 tns是二维数组[['a', 1], ['b', 2]] x代表tns中的['a', 1]  x[1]表示对1和2这维排序，不是对a和b这维排序
# reverse = True 降序， reverse = False 升序（默认）。
tns.sort(key=lambda x: x[1], reverse=True)
for i in range(3):
    print('the top {} percentage time is {}, spent in "{}" operation'.format(i, tns[i][1], tns[i][0]))
