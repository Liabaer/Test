# -*- coding: utf-8 -*-
x = 10
# 二进制输出
print(bin(x))
print('{:#b}'.format(x))
# 不输出前缀
print('{:b}'.format(x))
# 十六进制
# 因为是16进制，0-9 a b c d e f是一轮 -->  10进制的10对应的就是16进制的a
print(hex(x))
print('{:#x}'.format(x))
print('{:x}'.format(x))
# 八进制
print(oct(x))
print('{:#o}'.format(x))
print('{:o}'.format(x))



