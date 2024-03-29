# -*- coding: utf-8 -*-
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 例如，121 是回文，而 123 不是。

# ok 又是我的笨方法
# x = -121
# new_x = str(x)[::-1]
# print(new_x)
# if str(x) == new_x:
#     print(True)
# else:
#     print(False)


x = 121
print(x//10)
# 如果是负数肯定不是回文数，如果最后一位是0且第一位也是0才是回文数，只有0满足，所以排除这俩情况先
if x < 0 or (x % 10 == 0 and x != 0):
    print(False)

# 反转数字来比较，一个正数的位数可能是奇书或者偶数，拿一个中间变量存反转后的数字
temp = 0
# 当x 大于这个变量时进入循环，当x 小于或者等于temp时，证明已经处理了一半位数的数字了
while x > temp:
    # 将x的最后一位添加到temp中，并且乘以10保证位数相同
    temp = temp * 10 + x % 10
    # 让x本身不断除以10
    x //= 10
    # 判断x（x是偶数的情况）是不是和temp相等或者x（x是奇数的情况）是不是等于temp除以10，这理注意要循环完了再判断哦
print(x == temp or x == temp // 10)
