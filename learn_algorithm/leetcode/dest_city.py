# -*- coding: utf-8 -*-
# 给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。
# 请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
# 题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。

import collections

# Define the paths between cities
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

# 使用列表的默认值创建词典
outdegree = collections.defaultdict(int)

# 遍历路径并将第一个城市的出度数加1
for a, b in paths:
    outdegree[a] += 1
# 遍历路径并检查第二个城市的outdenee是否为0，如果是，则打印城市
# 下划线“_”用作变量的占位符，可以不用管他的值，这里是paths元素的索引
for _, b in paths:
    print(_, b)
    if outdegree[b] == 0:
        print(b)