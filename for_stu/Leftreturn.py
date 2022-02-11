# -*- coding: utf-8 -*-

# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
# 比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

a = 'abcdefg'
k = 2
b = ''
c = ''
for i in range(0, len(a)):
    if i <= k-1:
        b = b + a[i]
    else:
        c = c + a[i]
c = c + b
print(c)