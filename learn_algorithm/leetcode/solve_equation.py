# -*- coding: utf-8 -*-
# 求解一个给定的方程，将x以字符串 "x=#value"的形式返回。该方程仅包含 '+' ， '-' 操作，变量x和其对应系数。
#
# 如果方程没有解，请返回"No solution"。如果方程有无限解，则返回 “Infinite solutions” 。
#
# 如果方程中只有一个解，要保证返回值 'x'是一个整数。
# a = '12x'
# print(a[:-1]) 移除temp的最后一位
def calc_num(flag, temp, num, num_x):
    """

    :param flag: 使用flag判断符号
    :param temp: 中间变量存储非符号字符
    :param num: 常数
    :param num_x: x的系数
    :return: 返回常数和x的系数
    """
    # 首先flag = true, 遇见了加号，temp = x, 根据flag，我们知道 a要加1，同时遇见的也是加号，设置下一次做加法 flag = true ,temp初始化
    # 遇见了加号，temp = 3,根据上一步的flag = false 我们知道 b要减3，同事遇见的是加号，设置下一次是做加法 flag = true, temp 初始化
    # print(temp)
    # flag为True，就加法
    if flag:
        # 这里判断是x还是常数
        if 'x' not in temp:
            num = num + int(temp)
        else:
            # 这里要注意x的系数为1，l_temp[:-1]会为空
            if temp[:-1] == '':
                num_x = num_x + 1
            else:
                num_x = num_x + int(temp[:-1])
    # flag为False，执行减法，
    else:
        # 这里判断是x还是常数
        if 'x' not in temp:
            num = num - int(temp)
        else:
            if temp[:-1] == '':
                num_x = num_x - 1
            else:
                num_x = num_x - int(temp[:-1])
    return num, num_x


def calc_coefficient(equ):
    """
    :param equ: 要计算的字符串
    :return: 返回常数和x的数量
    """
    temp = ''
    num_x = 0
    num = 0
    i = 0
    # 要初始化flag，flag一开始的值取决于字符串第一位的符号
    if equ[0] == '-':
        flag = False
        # 遇见负号，让flag为False，，并且让i=1，直接取值
        i = 1
    else:
        flag = True

    # 首先根据s[0]有没有符号，是不是可以判断flag，下一次是做系数的加法，还是减法
    # a为x系数， b为常数的系数，这个测试用例，我们肯定是a = 2 b = 2
    while i < len(equ):
        # 如果temp有x的系数,那么根据上一次的fLag更新a #temp没有x的系数,那么根据上一次的f1ag更新b
        if equ[i] == '+':
            # 首先flag = true, 遇见了加号，temp = x, 根据flag，我们知道 a要加1，同时遇见的也是加号，设置下一次做加法 flag = true ,temp初始化
            # 遇见了加号，temp = 3,根据上一步的flag = false 我们知道 b要减3，同事遇见的是加号，设置下一次是做加法 flag = true, temp 初始化
            print(temp)
            # flag为True，就加法
            num, num_x = calc_num(flag, temp, num, num_x)
            flag = True
            temp = ''
        # 遇见了减号，temp = 5, 根据上一步的flag = true 我们知道 b要加5，同时遇见的是减号，设置下一次是做减法， flag = false，temp 初始化
        elif equ[i] == '-':
            print(temp)
            num, num_x = calc_num(flag, temp, num, num_x)
            flag = False
            temp = ''
        else:
            temp = temp + equ[i]
        i = i + 1
    # 最后一个l_temp没有遇到符号，所以要单独特殊处理
    if temp != '':
        num, num_x = calc_num(flag, temp, num, num_x)
    return num, num_x


equation = "x+5-3+x=6+x-2"
l_equation = ''
r_equation = ''
i = 0
flag = True
while i < len(equation):
    if equation[i] == '=':
        flag = False
        i = i + 1
        continue
    if flag:
        l_equation = l_equation + equation[i]
    else:
        r_equation = r_equation + equation[i]
    i = i + 1
print(l_equation)
# print(r_equation)


# 等号左边计算
l_num, l_num_x = calc_coefficient(l_equation)
# 等号右边计算
r_num, r_num_x = calc_coefficient(r_equation)
print('左边常数', l_num)
print('左边x', l_num_x)
print('右边常数', r_num)
print('右边x', r_num_x)

res = ''
# 如果常数为0，无解
if l_num != r_num and l_num_x - r_num_x == 0:
    res = "No solution"
    # 常数不为0，但x相同，为无限解
if l_num_x == r_num_x and l_num_x - r_num_x == 0:
    res = "Infinite solutions"
else:
    res = int((r_num - l_num) / (l_num_x - r_num_x))
print(res)
