# -*- coding: utf-8 -*-
n = 5
m = 0
l = []
flag = True
# while n != 0:
#     if n/2 != 1:
#         m = n % 2
#         n = n/2
#         print(n)
#         l.append(m)
#     else:
#         m = n % 2
#         n = n/2
#         l.append(m)
#         if n == 1:
#             m = n
#             l.append(m)
#         break
# 反转后为二进制
# l.reverse()
# print(l)
# for i in range(0,len(l)-1):
#     if l[i] == l[i+1]:
#         flag = False
#         break
# print(flag)
while n != 0:
    m = n % 2
    n = n / 2
    l.append(m)
print(l)
for i in range(0, len(l) - 1):
    if l[i] == l[i + 1]:
        flag = False
print(flag)
