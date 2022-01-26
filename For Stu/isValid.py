# -*- coding: utf-8 -*-
# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
s = "(){}}{"
m = []
i = 0
j = ''
flag = False
while i < len(s):
    # print s[i]
    if s[i] == '{' or s[i] == '[' or s[i] == '(':
        m.append(s[i])
        print m
    if s[i] == '}' or s[i] == ']' or s[i] == ')':
        if len(m) <= 0:
            flag = False
            break
        j = m.pop()
        if '{' == j and s[i] == '}':
            flag = True
        elif '[' == j and s[i] == ']':
            flag = True
        elif '(' == j and s[i] == ')':
            flag = True
        else:
            flag = False
            break
    i = i + 1
if len(m) > 0:
    flag = False
print flag

# while i < len(s):
#     # print s[i]
#     if s[i] == '{' or s[i] == '[' or s[i] == '(':
#         m.append(s[i])
#         # print m
#
#     if s[i] == '}':
#         if len(m) <= 0:
#             flag = False
#             break
#         j = m.pop()
#         if '{' == j:
#             flag = True
#         else:
#             flag = False
#             break
#     if s[i] == ']':
#         if len(m) <= 0:
#             flag = False
#             break
#         j = m.pop()
#         if '[' == j:
#             flag = True
#         else:
#             flag = False
#             break
#     if s[i] == ')':
#         if len(m) <= 0:
#             flag = False
#             break
#         j = m.pop()
#         if '(' == j:
#             flag = True
#         else:
#             flag = False
#             break
#     i = i + 1
# if len(m) > 0:
#     flag = False
# print flag
