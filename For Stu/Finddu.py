# -*- coding: utf-8 -*-
# 给定一个非空且只包含非负数的整数数组nums，数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是在 nums 中找到与nums拥有相同大小的度的最短连续子数组，返回其长度。
nums = [5, 1, 5, 2, 5, 3, 5, 4]
a = {}
c = 0
# 计算每个数字出现的字数放入字典
for b in range(0, len(nums)):
    if nums[b] not in a:
        a[nums[b]] = 1
    else:
        a[nums[b]] = a[nums[b]] + 1
print"每个数字出现的次数: " + str(a)
# 找出现最大的次数
for v in a:
    if a[v] >= c:
        c = a[v]
    else:
        continue
print "最大的度 : %s" % c
if c == 1:
    print 1
else:
    # 出现次数最多的数字取出来放数组里面
    d = []
    for v in a:
        if a[v] == c:
            d.append(v)
    print d
    #
    l = None
    r = None
    x = None
    for i in d:
        for j in range(0, len(nums)):
            if l == None:
                if i == nums[j]:
                    l = j
                    # print"l值 : %s" % l
            else:
                if i == nums[j]:
                    r = j
                    # print"r值 : %s" % r
        # print l, r
        if x == None:
            x = r - l
        # 当x不为None, 就要那x和这次的r-l比较大
        else:
            # 如果x 大于 （r - l) 就不管
            if x < (r - l):
                continue
            else:
                # 如果x小于 r - l就让x是小的
                x = r - l
            # print"x值 : %s" % x
        l = None
        r = None
    x = x + 1
    print"结果 : %s" % x



