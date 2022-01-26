# -*- coding: utf-8 -*-
# 写一个RecentCounter类来计算特定时间范围内最近的请求。
#
# 请你实现 RecentCounter 类：
#
# RecentCounter() 初始化计数器，请求数为 0 。
# int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 [t-3000, t] 内发生的请求数。
# 保证 每次对 ping 的调用都使用比之前更大的 t 值。


# 定义一个类名
from collections import deque

a = ["RecentCounter", "ping", "ping", "ping", "ping"]
b = [[], [1], [100], [3001], [3002]]


class RecentCounter(object):

    def __init__(self):
        # 初始化函数
        self.queue = deque()

    def ping(self, t):
        self. queue.append(t)
        #将第t秒入队这样队列里的就是[a,b,C,t],其中a<b<c<t,因为现在是t秒添加的新请求,之前肯定小于现在时间
        # #那么「t-3000,t」以外的元素就要出队,也就是要判断上面的abc是否在这个区间内,如果在区间外就要让他出队,他就是不是时间范围内的请求了
        # #检查队列里是否有不在这个范围的元素,遍历队列的方法,队列是先进先出,所以访问顺序肯定是abct,只要不在就出队,继续判断下一个元素
        while(True):
            x = self.queue[0]
            if x< t-3000 or x > t:
                self.queue.popleft()
            else:
                break
        return len(self.queue)


