# -*- coding: utf-8 -*-
# 异常处理知识
try:
    # 因为不能除以0所以会报错
    print("开始执行代码")
    x = 1 / 0
    print('报错了这里执行不到')
# 使用Exception类捕获一次  Exception 是类 使用as 生成对象 exception
except Exception as exception:
    # 打印报错日志
    print(exception)
# 不管程序是否报错 都会执行finally里面的语句
finally:
    print('就算报错了，把最后也会执行我')
