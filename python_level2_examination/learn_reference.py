# -*- coding: utf-8 -*-
# a = 1
# # 此时b的指针指向的是1的地址
# b = a
# print(b)
# # # 此时让a指向了2的地址，所以b还是指向1的地址b不会变
# a = 2
# print(b)
# #
a = [1, 2, 3]
# 此时b的指针指向的是[1,2,3]的地址
b = a
print(b)
# # 该操作将[1,2,3]地址上的值修改为了[5,2,3],由于b还指向这个地址，所以b也变成了[5,2,3]
a[0] = 5
print(b)
# # 当是如果将a整体重新指向[7,8,9]
# # 这个时候b和a不是指向一个地址了，修改a地址里的元素就不会影响b了
a = [7, 8, 9]
print(a)
a[0] = 9
print(b)