# -*- coding: utf-8 -*-
# 在...上补充一行或者多行代码
# 在——————上补充一行代码
# 在横线处填写代码，完成如下功能。
# 接收用户输入的一个大于10小于10的8次方十进 制正整数，输出这个正整数各字符的和，以25为 宽度，居中显示，采用等号=填充。
# 第一题
# s = input("请输入一个正整数: ")
# cs = 0
# for c in s:
#     cs += int(c)
# print('{:=^25}'.format(cs))

# 第二题
# 在横线处填写代码，完成如下功能。
# 接收用户输入的数据，该数据仅由字母和中文混 合构成，无其他类型字符，统计并输出中文字符 出现的个数，

# 在...上补充一行或者多行代码
# 在——————上补充一行代码

# s = input("请输入中文和字母的组合: ")
# count = 0
# for c in s:
#     # print(c)
#     if not (65 <= ord(c) <= 90 or 97 <= ord(c) <= 122):
#         count += 1
# print(count)
#

# 第三题
# 在横线处填写代码，完成如下功能。
# 接收用户输入的以英文逗号分隔的一组数据，其中，每个数据都是整数或浮点数，打印输出这组 数据中的最大值。
# 在...上补充一行或者多行代码
# 在——————上补充一行代码

# s = input("请输入一组数据：")
# ls = s.split(',')
# # print(ls)
# lt = []
# for i in ls:
#     # 加上eval函数，将字符串转换成对应格式，整形或者浮点型
#     lt.append(eval(i))
# # max求数组里的最大值 min求数组里的最小值
# print(max(lt))


# 第四题
# 描述
# 请写代码替换横线，不修改其他代码，实现以下功能：
# a和b是两个列表变量，列表a为[3,6,9]已给定，键盘输入列表b,计算a中元素与b中 对应元素乘积的累加和。
# 例如：键盘输入列表b为[1,2,3]，累加和为13+26+3*9=42，因此，屏幕输出计算结果 为42

# a = [3, 6, 9]
# b = eval(input()) #例如：[1,2,3]
# s = 0
# for i in range(3):
#     s += a[i]*b[i]
# print(s)

# 第五题
# 请编写代码替换横线，可修改其他代码，实现下面功能：
# 获得用户输入的一个整数n,输出一个n-1行的数字三角形阵列。
# 该阵列每行包含的 整数序列为从该行序号开始到n-1,例如第1行包含1到n-1的整数，第i行包含从到n- 1的整数；数字之间用英文空格分隔。
# 示例如下（其中数据仅用于示意）：

# 在...上补充一行或者多行代码
# 在——————上补充一行代码

n = eval(input("请输入一个整数："))
for i in range(1, n):
    for j in range(1, n):
        if j <= n-i:
            # 先打印出j来看，end去掉空格，就比较好看了
            print(j, end=' ')
    print()