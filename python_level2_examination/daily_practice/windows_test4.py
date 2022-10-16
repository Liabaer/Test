s = input()
print('{:=^15}'.format(s if len(s) <= 1 else s[:15]))
print('{:=^15}'.format(s))

import time

timestr = "2020-10-10 10:10:10"
t = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
print(time.strftime("%Y年-%m年-%d日 %H时:%M分:%S秒", t))
# 解析t是时间类型的变量，使用strftime转换成对应格式，%y %m是获取t里面的年月日等。


# import random
# brandlist = ['华为','苹果','诺基亚','OPPO','小米']
# random.seed(0)
# name = random.choice(brandlist)
# print(name)
#
#
# import turtle as t
# t.right(-30)
# for i in range(2):
#    t.fd(200)
#    t.right(60*(i+1))
# for i in range(2):
#    t.fd(200)
#    t.right(60*(i+1))
#
#
#
# txt = input("请输入类型序列：")
# t = txt.split(' ')
# d = {}
# for i in t:
#    d[i] = d.get(i,0)+1
# ls = list(d.items())
# ls.sort(key=lambda x:x[1], reverse=True)
# for k in ls:
#    print("{}:{}".format(k[0], k[1]))
#
#
#
# import random
# s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
# random.seed(0x1010)
# ls = []
# for i in range(10):
#    sr = ''
#    for j in range(10):
#        sr += random.choice(s)
#    if i+1 < 10 and sr[i][0] != s[i+1][0]:
#        ls.append(sr)
# print(ls)
# with open("随机密码.txt",'w',encoding = 'utf-8') as f:
#    for i in ls:
#        f.write('{}\n'.format(i))
#
