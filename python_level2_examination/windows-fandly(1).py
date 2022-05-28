# 001
# num = input().split(',')
# for i in num:
#    print('{: >10}'.format(i),end='')


# 002
# s = input("请输入5个小写字母：")
# s = s.upper()
# print(','.join(s[::-1]))


# 003
# import random
# n = eval(input())
# random.seed(100)
# for i in range(1,11):
#    if i<10:
#        print(random.randint(1,n),end=',')
#    else:
#        print(random.randint(1,n),end='')


# 004
# import turtle
# n = 4
# for j in range(n):
#    turtle.pendown()
#    for i in range(4):
#        turtle.fd(40)
#        turtle.right(90)
#    turtle.penup()
#    turtle.fd(80)
# turtle.done()


###005
# img = [0.69,0.292,0.33,0.131,0.61,0.254]
# filter = [0.1, 0.8, 0.1]
# res = []
# for i in range(len(img) - 2):
#   k = 0  # 有多个和，所以每次赋初始值0
#   for j in range(3):  # 求3次累计和
#      k += img[i+j]*filter[j]  # 求3次累计和
#      print('k={:.3f} ,filter[{}]={:.3f},img[{}+{}]={:.3f}'.format(k, j, filter[j], i, j, img[i + j]))
#   res.append(k)
# for r in res:
#   print('{:.3f}'.format(r), end=' ')


##006-1
# # 读取文件内容到列表ls中
# with open('C:\\Users\\dayday\\Desktop\\webpage-data.txt', 'r', encoding='utf-8') as f:
#    ls = f.readlines()
#
# ##统计url个数
# num= 0  #统计个数的初始值为0
# ####
# for i in ls:
#    i = i.strip()
#    # if i[0:4] == '<img':
#    if '.JPG' in i:
#        num+=1
#
# ###
# print(num)  #输出个数

# 006-2

# 读取文件内容到列表ls中
# with open('C:\\Users\\dayday\\Desktop\\webpage-data.txt', 'r',encoding="utf-8") as f:
#    ls = f.readlines()
##
## 请在此作答
##
# f = open("images.txt","w")
##
# for i in ls:
#    i = i.strip()
#    if i[0:4] == '<img':
#        temp = i.split('src=')[1].split(' ')[0][1:-1]
#        f.write('{}\n'.format(temp))
# f.close()


# 007-1

# s = input()
# print("{:\"^30}".format(hex(eval(s))))
#
#
###007-2
# n = input('请输入一个正整数:')                    #请输入一个正整数:
# for i in range(eval(n)):
#     # print('{0:>2} {1}'.format(i, '<'*i))
#     print('{0:>2} {1}'.format(i+1,'<'*(i+1)))
#    # print('{1} {:=>0}'.format(i + 1, i if i < 10 else '0'+ i))


# 007-3
# s = input("请输入一个小数: ")
# s = s[::-1]
# cs = 0
# for c in s:
#    if c == '.':
#        break
#    cs += eval(c)
# print('{:*>10}'.format(cs))


# 007-4

# n = eval(input("请输入一个整数："))
# for i in range(1,n):
#    for j in range(1,n):
#        if j >= i:
#            print(j,end='')
#    print()


# 007-5
# ntxt = input("请输入4个数字(空格分隔):")
# nls = ntxt.split(' ')
# x0 = eval(nls[0])
# y0 = eval(nls[1])
# x1 = eval(nls[2])
# y1 = eval(nls[3])
# r = pow(pow(x1-x0, 2) + pow(y1-y0, 2), 0.5)
# print("{:.2f}".format(r))


# 007-6
# s = input("请输入中文和字母的组合: ")
# count = 0
# for c in s:
#    if c.isalnum == False:
#        count += 1
# print(count)

s = input("请输入中文和字母的组合: ")
count = 0
for c in s:
   if ((ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord('c') <= ord('Z'))) == False:
       count += 1
print(count)


# 007-7


#
# def func(n):
#    s = 0
#    if n%2 != 0:
#        for i in range(1, n + 1, 2):
#            s += 1 / i
#    else:
#        for i in range(2, n + 1, 2):
#            s += 1 / i
#    return s
#
#
# number = int(input())
# print(round(func(number),2))


# 007-8 C:\\Users\\dayday\\Desktop\\data-school.txt
# fr = open("C:\\Users\\dayday\\Desktop\\data-school.txt",'r',encoding = 'utf-8')  # 此处可多行
# r = fr.readlines()
# fr.close()
# f = open("univ.txt", "w")
# for i in r: # 此处可多行
#    i = i.strip()
#    if i[0:4] == '<img':
#        temp = i.split(' ')
#        for j in temp:
#            if j[0:4] == 'alt=':
#                f.write('{}\n'.format(j[5:-1]))
# f.close()

#
# n = 0
#
# f = open("univ.txt", "r")
#
# fr = f.readlines()  # 此处可多行
# n = 0
# s = 0
# for i in fr:
#     if i.find('大学') == -1 and i.find("学院") != -1:
#         s += 1
#     elif i.find('大学生') == -1 and i.find("大学") != -1:
#         print(i)
#         n += 1
#
# f.close()
# print("包含大学的名称数量是{}".format(n))
# print("包含学院的名称数量是{}".format(s))
