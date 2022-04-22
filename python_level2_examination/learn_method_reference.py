# -*- coding: utf-8 -*-
# 函数中变量的传递


# a = 1
# def update_int(temp):
#     temp = 2
#     print(temp)
# update_int(a)
# # 不会修改结果，因为此时传入的a,相当于a 指向1， temp=a,也指向1的地址，所以temp=2的时候temp指向了2，a不会变
# print(a)

# a = [1, 2, 3]
# def update_list(temp):
#     temp = [2, 3, 4]
#     print(temp)
# update_list(a) # 和上面同理
# print(a)
#
# a = [1, 2, 3]
# def update_list2(temp):
#     temp[0] = 3
#     # 除了上述这种修改，类似append,insert都会修改地址中的元素
#     temp.append(4)
#     temp.insert(2, 100)
#     print(temp)
# update_list2(a) # 此时a和temp都指向的是[1,2,3]地址，temp修改[1,2,3]的地址为[3,2,3]，a的结果
# print(a)
# #
#
# 比较特殊的情况
def update_list3(temp=[]):
    temp.append(1)
    print(temp)
# temp会在内存中一直追加1，从[]修改为[1],[1,1]...
update_list3()
update_list3()
update_list3()