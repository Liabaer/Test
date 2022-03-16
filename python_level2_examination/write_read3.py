# -*- coding: utf-8 -*-
# 计算每个班级的平均分,打印输出班级和平均分,平均分小数点后保留2位,中间用英文冒号隔开, 示例如下:
# f_data = open('data.txt', 'r', encoding='UTF-8')
# print(f_data)
# 方法1
# subject = ''
# score = 0
# score_avg = 0
# sub_dict = {}
# score_dict = {}
# for i in f_data.readlines():
#     i = i.strip()
#     temp = i.split(':')[1]
#     subject = temp.split('，')[0]
#     score = temp.split('，')[1]
#     score = int(score)
#     if subject not in sub_dict:
#         sub_dict[subject] = 1
#     else:
#         sub_dict[subject] = sub_dict[subject] + 1
#     if subject not in score_dict:
#         score_dict[subject] = score
#     else:
#         score_dict[subject] = score_dict[subject] + score
# for k, v in score_dict.items():
#     score_avg = v/sub_dict[k]
#     print(k, ':', score_avg)
# #
# #     print(subject)
# #     print(score)
# print(sub_dict)
# print(score_dict)
# f_data.close()

# 在...补全代码块

# 方法二，使用一个字典存储学科和分数
f_data = open("data.txt", "r")
dict_subject = {}
for i in f_data.readlines():
    i = i .strip()
    temp = i.split(":")[1]
    subject = temp.split("，")[0]
    score = temp.split("，")[1]
    if subject in dict_subject:
        value = dict_subject[subject]
        # print(value)
        dict_subject[subject] = [value[0] + int(score), value[1] + 1]
        # print(dict_subject[subject])
    else:
        dict_subject[subject] = [int(score), 1]
print(dict_subject)