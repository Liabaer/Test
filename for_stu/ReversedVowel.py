# -*- coding: utf-8 -*-
# 反转字符串中的元音字母
s = "Never a foot too far, even."

# 最优解：dayday想到的最优解
a = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
y = list(s)
x = len(y) - 1
for i in range(0, len(y)):
    flag = False
    cnt = 0
    for j in range(x, -1, -1):
        if y[i] in a and y[j] in a:
            flag = True
            c = y[i]
            y[i] = y[j]
            y[j] = c
            x = j - 1
            break
        elif y[i] not in a and y[j] in a:
            x = j
            break
        elif y[i] in a and y[j] not in a:
            continue
    # print(y)
    if flag == False and y[i] in a:
        break
    if x == 0:
        break
    if i >= x:
        break
o = ''.join(y)
# for k in y:
#     o = o + k
print(o)
# 优化的方法嘞
# a = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# y = []
# for z in s:
#     y.append(z)
# x = len(y) - 1
# for i in range(0, len(y)):
#     for j in range(x, -1, -1):
#         if y[i] in a and y[j] in a:
#             c = y[i]
#             y[i] = y[j]
#             y[j] = c
#             x = j - 1
#             break
#         elif y[i] not in a and y[j] in a:
#             x = j
#             break
#         elif y[i] in a and y[j] not in a:
#             continue
#     if i >= x:
#         break
# o = ''
# for k in y:
#     o = o + k
# print(o)
# 这个方法可行，但是执行时间太长
# y = list(s)
# print(y)
# # for z in s:
# #     y.append(z)
# a = ['a', 'e', 'i', 'o', 'u','A' ,'E', 'I', 'O', 'U']
# b = []
# x = len(y)-1
# for i in range(0, len(y)):
#     for j in range(x, -1, -1):
#         if y[i] in a and y[j] in a:
#             print(y[i], y[j],i,j)
#             c = y[i]
#             y[i] = y[j]
#             y[j] = c
#             x = j - 1
#             break
#     print(y)
#     if i >= x:
#         break
# o = ''
# o = ''.join(y)
# # for k in y:
# #     o = o + k
# print(o)
# "leotcede"
# "Never a foot too far, even."
# "euston saw I was not SuE."

a = list(s)
vowel = ['a', 'e', 'i', 'o', 'u','A' ,'E', 'I', 'O', 'U']
left = 0
right = len(a)-1
while left < right:
    if a[left] in vowel and a[right] in vowel:
        new = a[left]
        a[left] = a[right]
        a[right] = new
        left = left + 1
        right = right - 1
    elif a[left] in vowel and a[right] not in vowel:
        right = right - 1
    elif a[left] not in vowel and a[right] in vowel:
        left = left + 1
    else:
        left = left + 1
        right = right - 1
b = ''
a = b.join(a)
print(a)
