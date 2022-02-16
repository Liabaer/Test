# -*- coding: utf-8 -*-
# 中文分词函数库
import jieba
# 解决Building prefix dict from the default dictionary ...
# Loading model from cache /tmp/jieba.cache
# Loading model cost 0.128 seconds.
# Prefix dict has been built succesfully.
jieba.setLogLevel(20)


# 精确模式
# a = jieba.lcut('全国计算机等级考试')
# print(a)
# # # 搜索引擎模式 （将句子中可能的词语都分出来）
# b = jieba.lcut_for_search("全国计算机等级考试")
# print(b)
# # # 全模式 （在精确模式的基础上，将长词语，再分成短词语)
# c = jieba.lcut('全国计算机等级考试', cut_all=True)
# print(c)
# # 添加新的词语 让jieba认为他是一个词语，需要保证添加的新的词语在分词操作中不会被分开
# jieba.add_word("等级考试")
# a = jieba.lcut('全国计算机等级考试')
# print(a)
#
#
#
# print 知识点
#
# # print 默认是打印字符，结尾是一个换行符
# print("1")
# print("2")
#
# # 使用end参数可以指定以什么字符结尾  上面的写法其实等价于print("1", end="\n")
print("1", end=",")
print("2", end="\n")
#
# # print打印 左对齐 右对齐居中对齐
# # 第一个表示参数，第二个表示格式应该填充什么符号 print("aaa".ljust(20)) 省略第二个表示填充空格
print("aaa".center(20))
print("aaa".ljust(20, "*"))
print("aaa".rjust(20, "*"))
#
# # print里面可以使用format 表示填充第一个{} 和第一个{}的参数 等价 print(a + " " + b)
print("{} {}".format("a", "b"))