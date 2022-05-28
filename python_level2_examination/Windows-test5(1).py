# y = input()  # 宽度
# n = input()  # 整数
# print('{0:->{1},d}'.format(y,int(n))) # 把整数按照指定y的宽度右对齐显示，并且带千分位分隔符

#
# import jieba
# txt = input("请输入一段中文文本:")
# ls = jieba.lcut(txt)
# for i in ls[::-1]:
#    print(i,end='')


import jieba
txt = input("请输入一段中文文本:")
t = jieba.lcut(txt)
# print('{:.1f}'.format(len(txt)/len(t)))
print(round(len(txt)/len(t), 1))


#import turtle
#for i in range(4):
#    turtle.fd(100)
#    turtle.fd(-100)
#    turtle.seth((i+1)*90)



# 问题1：请统计有效票张数。参考程序框架文件，补充代码完成程序。
# 请在......处使用多行代码替换
#f = open("C:\\Users\\dayday\\Desktop\\班级人员.txt",'r')
#names = f.readlines()
#print(names)
#f.close()
#f = open("C:\\Users\\dayday\\Desktop\\投票数据.txt",'r')
#votes = f.readlines()
#f.close()
#d = {}
#print(votes)
#ls = []
#for i in names:
#    i = i .strip()
#    ls.append(i)
#for i in votes:
#    i = i.strip()
#    temp = i.split(' ')
#    if len(temp) > 1 or i not in ls:
#        continue
#    else:
#        d[i] = d.get(i,0)+1
#print(d)
#n = 0
#for i in d:
#        n += d[i]
#print("有效票{}张".format(n))

#
##问题2：请统计当选班长及其票数。参考程序框架文件，补充代码完成程序。
##请在......处使用多行代码替换
#f = open("C:\\Users\\dayday\\Desktop\\班级人员.txt",'r')
#names = f.readlines()
#print(names)
#f.close()
#f = open("C:\\Users\\dayday\\Desktop\\投票数据.txt",'r')
#votes = f.readlines()
#f.close()
#d = {}
#print(votes)
#ls = []
#for i in names:
#    i = i .strip()
#    ls.append(i)
#for i in votes:
#    i = i.strip()
#    temp = i.split(' ')
#    if len(temp) > 1 or i not in ls:
#        continue
#    else:
#        d[i] = d.get(i,0)+1
#print(d)
#n = 0
#dl = list(d.items())
#dl.sort(key=lambda x:x[-1],reverse = True)
#print(dl)
#name = dl[0][0]
#score = dl[0][1]
#print("当选班长同学为：{}，票数为：{}".format(name,score))




#import jieba
#def become(test):
#    d = {}
#    for i in test:
#        t = jieba.lcut(i)
#        for j in t:
#            if len(j) < 2:
#                continue
#            else:
#              d[j] = d.get(j,0) + 1
#    return d
#
#f1 = open("C:\\Users\\dayday\\Desktop\\政府工作报告2018 (1).txt",'r',encoding = 'utf-8')
#txt1 = f1.readlines()
#f1.close()
#f2 = open("C:\\Users\\dayday\\Desktop\\政府工作报告2019.txt",'r',encoding = 'utf-8')
#txt2 = f2.readlines()
#f2.close()
#d = {}
#d = become(txt1)
#d1 = become(txt2)
#
#lt = list(d.items())
#lt.sort(key = lambda x:x[1],reverse = True)
#l = list(d1.items())
#l.sort(key = lambda x:x[1],reverse = True)
#ls1 = []
#for i in lt[0:10]:
#    s = i[0]+':'+ str(i[1])
#    ls1.append(s)
#print(ls1)
#ls2 = []
#for i in l[0:10]:
#    s = i[0]+':'+ str(i[1])
#    ls2.append(s)
#print('2019:'+ ','.join(ls1))
#print('2018:'+ ','.join(ls2))


#
#import jieba
#
#f1 = open("C:\\Users\\dayday\\Desktop\\政府工作报告2018 (1).txt",'r',encoding = 'utf-8')
#txt1 = f1.readlines()
#f1.close()
#f2 = open("C:\\Users\\dayday\\Desktop\\政府工作报告2019.txt",'r',encoding = 'utf-8')
#txt2 = f2.readlines()
#f2.close()
#comm = {}
#for i in txt1:
#    i = i.strip()
#    l1 = jieba.lcut(i)
###print(l1)
#for i in txt2:
#    i = i.strip()
#    l2 = jieba.lcut(i)
#for i in l1:
#    if i in l2:
#        comm[i] = comm.get(i,0) + 1
#t2019 = {}
#for i in l2:
#    if i not in l1:
#        t2019[i] = t2019.get(i,0) + 1
#tpcs2 = {}
#for i in l1:
#    if i not in l2:
#        tpcs2[i] = tpcs2.get(i,0) + 1
#
#print('共有词语:', end='')
#print(','.join(list(comm.keys())))
#print('2019特有:', end='')
#print(','.join(list(t2019.keys())))
#print('2018特有:', end='')
#print(','.join(list(tpcs2.keys())))

































































