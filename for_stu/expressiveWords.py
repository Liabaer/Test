# -*- coding: utf-8 -*-
# 有时候人们会用重复写一些字母来表示额外的感受，比如 "hello" -> "heeellooo", "hi" -> "hiii"。我们将相邻字母都相同的一串字符定义为相同字母组，例如："h", "eee", "ll", "ooo"。
#
# 对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，我们将这个单词定义为可扩张的（stretchy）。
# 扩张操作定义如下：选择一个字母组（包含字母c），然后往其中添加相同的字母c使其长度达到 3 或以上。
#
# 例如，以"hello" 为例，我们可以对字母组"o" 扩张得到 "hellooo"，但是无法以同样的方法得到 "helloo" 因为字母组 "oo" 长度小于3。
# 此外，我们可以进行另一种扩张 "ll" -> "lllll" 以获得"helllllooo"。
# 如果S = "helllllooo"，那么查询词"hello" 是可扩张的，因为可以对它执行这两种扩张操作使得query = "hello" -> "hellooo" ->"helllllooo" = S。
#
# 输入一组查询单词，输出其中可扩张的单词数量。
s = "abcd"

words = ["abc"]


def calc_num(l, temp):
    """
    :param l: 计算字符串的第几位数
    :param temp: 计算的字符串
    :return: 返回当前第l位连续出现了几次
    """
    num = 1
    while l < len(temp):
        if l + 1 < len(temp) and temp[l] == temp[l + 1]:
            num = num + 1
        else:
            break
        l = l + 1
    return num


res = 0
k = 0
while k < len(words):
    i = 0
    j = 0
    temp = words[k]
    flag = True
    while i < len(s) and j < len(temp):
        # print(s[i], temp[j])
        # 如果字符本身不相等，不用判断数量，直接break并跳出循环
        if s[i] != temp[j]:
            print('===')
            flag = False
            break
        else:
            a = calc_num(i, s)
            # 比较完相同的字符，将下标重新赋值到下一位将要比较的字符
            i = i + a
            b = calc_num(j, temp)
            j = j + b
            if a < b:
                print('-----')
                flag = False
                break
            elif a == 2 and b == 1:
                print('+++++')
                flag = False
                break
    # 计算s 和 temp 循环完之后 所有字符是否都比较完
    if i != len(s) or j != len(temp):
        flag = False
    print(flag)
    if flag:
        print(words[k])
        res = res + 1
    k = k + 1
print(res)
