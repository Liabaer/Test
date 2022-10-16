# -*- coding: utf-8 -*-
# 丑数就是只包含质因数2、3和5的正整数。
# 给你一个整数n,请你判断n是否为丑数。如果是，返回true;否则，返回false。
# n = 6
# # if n == 0:
# #     print(False)
# # else:
# #     temp = [2, 3, 5]
# #     for i in temp:
# #         while n % i == 0:
# #             n = n / i
# #     print(n == 1)
#
# while n > 1:
#     if n % 2 == 0:
#         n = n / 2
#     elif n % 3 == 0:
#         n = n / 3
#     elif n % 5 == 0:
#         n = n / 5
# print(n == 1)


x = 3
y = 4
points = [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]
minxy = pow(10, 4)
min_temp = pow(10, 4)
for i in range(0, len(points)):
    temp = abs(points[i][0] - x) + abs(points[i][1] - y)
    if points[i][0] == x or points[i][1] == y:
        if temp < min_temp:
            min_temp = temp
            minxy = i
        elif min_temp == temp:
            if minxy > i:
                minxy = i
        else:
            continue
        # print(min_temp)
if minxy == pow(10, 4) + 1:
    minxy = -1
print(minxy, end=' ')
