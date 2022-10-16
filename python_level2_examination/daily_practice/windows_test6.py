# import random
# random.seed(0)
# s = 0
# for i in range(5):
#    n = random.randint(1,97)  # 产生随机数
#    s = s + pow(n,2)
# print(s)

#
# scale = 0.0001  # 成就值增量
#
# def calv(base, day):
#    val = base * pow(1+scale,day*8)
#    return val
#
# print('5年后的成就值是{}'.format(int(calv(1, 5*365))))
#
# year = 1
# while calv(1, 365*year) < 100:
#    year += 1
#
# print('{}年后成就值是100'.format(year))
#
#
#
#
# s = input("请输入一组数据: ")
# ls = s.split(',')
# lt = []
# for i in ls:
#    lt.append(i)
# print(max(lt))
#


# import turtle as t
# ls = [69, 292, 33, 131, 61, 254]
# X_len = 400
# Y_len = 300
# x0 = -200
# y0 = -100
#
# t.penup()
# t.goto(x0, y0)
# t.pendown()
#
# t.fd(X_len)
# t.fd(-X_len)
# t.seth(90)
# t.fd(Y_len)
#
# t.pencolor('red')
# t.pensize(5)
# for i in range(len(ls)):
#    t.penup()
#    t.goto(x0 + (i+1)*50, y0)
#    t.seth(90)
#    t.pendown()
#    t.fd(ls[i])
# t.done()


# import random
# random.seed(2)
#
# pdict= {'Alice':['123456789'],
#        'Bob':['234567891'],
#        'Lily':['345678912'],
#        'Jane':['456789123']}
#
# name = input('请输入一个人名:')
#
# if name in pdict:
#    n = random.randint(1000,9999)
#    a = ''.join(pdict[name])
#    print('{} {} {}'.format(name,a,n))
# else:
#    print("对不起，您输入的用户信息不存在")


# f_data = open('C:\\Users\\dayday\\Desktop\\data-student.txt', 'r', encoding="utf-8")
# f_studs = open('studs.txt', 'w', encoding="utf-8")
# f = f_data.readlines()
# d = {}
# for i in f:
#    i = i.strip()
#    name = i.split(':')[0]
#    score = i.split(':')[1].split(',')[-1]
#    d[name] = score
# for i in d:
#    f_studs.write('{}:{}\n'.format(i,d[i]))
# f_data.close()
# f_studs.close()


#
# f_data = open('C:\\Users\\dayday\\Desktop\\data-student.txt', 'r', encoding="utf-8")
#
# f = f_data.readlines()
# d = {}
# for i in f:
#    i = i.strip()
#    name = i.split(':')[0]
#    score = i.split(':')[1].split(',')[-1]
#    d[name] = score
# ld = list(d.items())
# ld.sort(key=lambda x:x[-1],reverse=True)
# print('{}:{}'.format(ld[0][0],ld[0][1]))
#
# f_data.close()
#


# f_data = open('C:\\Users\\dayday\\Desktop\\data-student.txt', 'r', encoding="utf-8")
# d = {}
# students = f_data.readlines()
# for student in students:
#    i = student.strip()
#    cls = i.split(':')[1].split(',')[0]
#    sc = i.split(':')[1].split(',')[-1]
#    d[cls] = d.get(cls,(0,0)) + (int(sc),1)
# for i in d:
#    n = 0
#    s = 0
###    print(d[i])
#    for j in d[i]:
#        if j ==1:
#            n += 1
#        else:
#            s += j
#    print('{}:{:.2f}'.format(i,s/n))
# f_data.close()
