# -*- coding: utf-8 -*-
# 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。
# a = "the sky is blue"
# x = ''
# y = []
# for i in range(0, len(a)):
#     # 如果遇见的不是空格，就说明一直是个单词，存进x里面，x表示一个单词
#     if a[i] != ' ':
#         x = x + a[i]
#     else:
#         # 如果遇见空格 说明 x是一个完整的单词了，就把x放进y里面，并且让x又从空字符开始成为单词
#         print x
#         y.append(x)
#         x = ''
# # 循环结束后如果x不是空字符串的话就放进y里面，比如ccc，因为他最后没有空格了，所以执行不到上面那个else就放到这里来
# y.append(x)
# print y
# # 把y数组倒着循环，然后用c变量加起来就是 倒着的答案了
# c = ''
# for i in range(len(y) - 1, -1, -1):
#     c = c + ' ' + y[i]
#     print c
# print c


a = "a good   example"
b = ''
j = 0
flag = False
while j <= len(a) - 1:
    if a[j] != ' ':
        # 遇见字母了
        flag = True
        b = b + a[j]
        j = j + 1
    elif flag == True:
        # 遇见字母的空格要离着
        b = b + a[j]
        j = j + 1
        continue
    else:
        j = j + 1
        continue
print 'b=' + b
# b就是去掉了开头空格的
# 然后把b倒过来，继续去除开头的空格，相当于结尾的空格也去掉了
# b = "the sky is blue   "

c = ''
k = len(b)-1
flag = False
while k >= 0:
    if b[k] == ' ':
        k = k - 1
        continue
    else:
        break
for m in range(0, k+1):
    c = c + b[m]
print 'c=' + c

x = ''
y = []
flag = False
for i in range(0, len(c)):
    if c[i] != ' ':
        flag = False
        x = x + c[i]
    else:
        if flag == False:
            y.append(x)
            flag = True
        x = ''
y.append(x)
print y
z = ''
for l in range(len(y)-1, -1, -1):
    if l == len(y) - 1:
        z = y[l]
    else:
        z = z + ' ' + y[l]
    print z
print z










