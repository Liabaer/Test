# -*- coding: utf-8 -*-
# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
# 例如，在字符串 s = "abbxxxxzyy"中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。
# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。

s = "abcdddeeeeaabbbcd"

# 自己啰嗦版本
# start = 0
# end = 0
# num = 0
# str_num = ''
# temp = []
# res = []
# i = 0
# while i < len(s):
#     if i + 1 < len(s):
#         if s[i] == s[i+1]:
#             num = num + 1
#             # 当通过第一个num超过3的时候，str_num等于空，str_num 要加上 s[i]，否则会缺失一个s[i]
#             if str_num == '':
#                 str_num = s[i] + s[i+1]
#             else:
#                 str_num = str_num + s[i+1]
#         else:
#             if num >= 2:
#                 print(str_num)
#                 # 计算连续相邻的字母统计出现的个数，并通过i -长度+1计算开始下标
#                 start = i - len(str_num) + 1
#                 end = i
#                 temp.append(start)
#                 temp.append(end)
#                 start = 0
#                 end = 0
#                 num = 0
#                 str_num = ''
#             else:
#                 # 当num<2也要记得初始化
#                 start = 0
#                 end = 0
#                 num = 0
#                 str_num = ''
#     if len(temp) != 0:
#         res.append(temp)
#         temp = []
#     i = i + 1
# if num >= 2:
#     print(str_num)
#     # 计算连续相邻的字母统计出现的个数，并通过i -长度+1计算开始下标
#     start = i - len(str_num)
#     end = i - 1
#     temp.append(start)
#     temp.append(end)
#     start = 0
#     end = 0
#     num = 0
#     str_num = ''
# if len(temp) != 0:
#     res.append(temp)
#     temp = []
# print(res)


# 简化不啰嗦版本
start = 0
end = 0
num = 0
str_num = ''
temp = []
res = []
i = 0
while i < len(s):
    if i + 1 < len(s):
        if s[i] == s[i + 1]:
            num = num + 1
            # 当通过第一个num超过3的时候，str_num等于空，str_num 要加上 s[i]，否则会缺失一个s[i]
            if str_num == '':
                str_num = s[i] + s[i + 1]
            else:
                str_num = str_num + s[i + 1]
        else:
            if num >= 2:
                print(str_num)
                # 计算连续相邻的字母统计出现的个数，并通过i -长度+1计算开始下标
                temp.append([i - len(str_num) + 1, i])
            num = 0
            str_num = ''
    i = i + 1
if num >= 2:
    print(str_num)
    # 计算连续相邻的字母统计出现的个数，并通过i -长度+1计算开始下标
    temp.append([i - len(str_num), i - 1])
print(temp)
