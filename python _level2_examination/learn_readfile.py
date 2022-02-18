# -*- coding: utf-8 -*-
# 读写文件

# 使用open函数打开一个文件对象
# 第一个参数是文件的路径，在一个目录直接文件名，否则就/Users/xxx/xxx/test.txt
# 第二个参数r表示使用可读的权限打开文件（如果文件不存在会报错）, w表示生成新的文件，如果存在文件，则覆盖文件 , a表示在已有的文件修改
# 第三个参数表示解析的编码格式
f = open("/Users/Tu/text.txt", "r", encoding="utf-8")
# 通过read()方法可以一次性读取文件的全部内容
print(f.read())
# 调用close()方法关闭文件
f.close()
# #
# # 上面的写法等价为下面,会自动调用close()方法，没有其他作用了
# with open('/Users/Tu/text.txt', "r", encoding="utf-8") as f:
#     print(f.read())
#
# f = open("/Users/Tu/text.txt", "r", encoding="utf-8")
#
#
# num = 0
# # readlines()按行读取，可以使用x.strip()去掉结尾的回车符，可以看到下面输出，x默认打印了个空行
# for x in f.readlines():
#     print("第" + str(num) + '行是:' + x)
#     num = num + 1
# f.close()
#
# # 写文件 覆盖文件text.txt, 不存在文件名会创建，存在则覆盖原来的内容
# f = open("/Users/Tu/text.txt", "w", encoding="utf-8")
# f.write("我是代码写入的1\n")
# f.write("我是代码写入的2\n")
# f.close()
#
# # 写文件 不存在文件名会创建，存在就在已有的文件上追加内容
# f = open("/Users/Tu/text.txt", "a", encoding="utf-8")
# f.write("我是追加代码写入的1\n")
# f.write("我是追加代码写入的2\n")
# f.close()