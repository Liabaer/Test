# -*- coding: utf-8 -*-
# 给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
# 由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。
# 返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。

names = ["wano","wano","wano","wano"]
# name = []
res = []
res_dict = {}
# j = 0
# 先处理一下数组中的（num） ------ 人家根本不需要处理这个，想太多，好多草
# while j < len(names):
#     k = 0
#     new_name = ''
#     while k < len(names[j]):
#         if names[j][k] != '(':
#             new_name = new_name + names[j][k]
#         else:
#             k = k + 1
#             break
#         k = k + 1
#     name.append(new_name)
#     j = j + 1
# # print(name)

j = 0
while j < len(names):
    if names[j] not in res_dict:
        res_dict[names[j]] = 1
        res.append(names[j])
    else:
        # num = 1
        # 然后从num次开始循环
        num = res_dict[names[j]]
        # 一定要记得处理。超出时间限制
        res_dict[names[j]] = res_dict[names[j]] + 1
        # 先写死循环，寻找num的次数
        while True:
            res_dict[names[j]] = res_dict[names[j]] + 1
            # 如果出现在res中，就让num+1
            if names[j] + '(' + str(num) + ')' in res_dict:
                num = num + 1
            else:
                res_dict[names[j] + '(' + str(num) + ')'] = 1
                # 没出现在res中，就放进答案，并且结束循环
                res.append(names[j] + '(' + str(num) + ')')
                break
    j = j + 1
print(res)
