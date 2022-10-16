# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
ls = []
ls.append(1)
ls.append(2)
ls.append(3)
# 由于ls里面是个int x表示的是int，不能用x[-1]会报错
# ls.sort(key=lambda x:x[-1], reverse=True)
# 一维数组直接排序就好了
ls.sort(reverse=True)
print(ls)

ls = []
ls.append('ab')
ls.append('ef')
ls.append('cd')
# 由于ls里面是个str, x表示的是str, 所以x[-1]表示字符串的最后一位，也就是'ab'就是按照b排序，这里表示按照字符串的最后一位排序
ls.sort(key=lambda x: x[-1], reverse=True)
print(ls)

ls = []
ls.append(['a', 3])
ls.append(['b', 10])
ls.append(['c', 9])
# 由于ls里面是个数组, x表示的是一维数组, 所以x[-1]表示数组的最后一位，也就是['a', 3] 就是按照3排序，这里表示按照里面数组的最后一位排序
ls.sort(key=lambda x: x[-1], reverse=True)
print(ls)

temp = ('80 90 100 110')
# 元祖内只有一个字符串，那么他的数据类型会变成字符串
print(temp)
temp = ('80 90 100 110', '80')
# 元祖内只有字符串个数大于1，那么他的数据类型还是元祖
print(temp)
