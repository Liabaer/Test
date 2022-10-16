# -*- coding: utf-8 -*-
# 文件未学习的相关知识
# w模式 write表示以写权限打开文件
# f = open("name.txt", 'w', encoding='utf-8')
# # 注意此时输出的是一个文件类型 <_io.TextIOWrapper> 不是具体的值
# print(f)
# a = ["dayday", "liabaer"]
# b = ["yanxu", "tulian"]
# # 读取一个数组 将a数组拼成一行写入文件 等价于 f.write(''.join(a))  --》写入文件内的内容为：yanxutulian
# f.writelines(a)
# # 读取一个字符串
# f.write('\n')
# # # 等价writelines写法
# f.write(''.join(b))
# f.close()
# #
# # read模式 读权限打开文件
# f = open("name.txt", "r")
# # 读取文件中所有行的内容，按照每行组装成数组
# print(f.readlines())
# f.close()
# #
# # 之所以要重新打开是因为上面读完文件了
# f = open("name.txt", "r")
# # 读取一行
# print(f.readline())
# f.close()
#
# f = open("name.txt", "r")
# # 只读取前n位字符，不填读取所有
# print(f.read(12))
# f.close()
# #
f = open("../data/name.txt", "r")
# 指定从第3位开始读文件(read前声明）,不然默认是从头开始读取文件
f.seek(3)
print(f.read())
f.close()

# 使用with关键字可以自动调用close方法
with open("../data/name.txt", "r") as f:
    print(f.read())

# 文件打开权限

# r前缀的权限

# r 只读，文件不存在报错
# rb 二进制只读，文件不存在报错  （二进制指的是0101的模式去读取文件）
# r+ 读写，文件不存在报错
# rb+ 二进制读写，文件不存在报错

# w前缀的权限

# w只写，文件不存在，新建一个文件，存在文件，则覆盖文件内容
# wb 二进制只写， 文件不存在，新建一个文件，存在文件，则覆盖文件内容
# w+ 读写，文件不存在，新建一个文件，存在文件，则覆盖文件内容
# wb+ 二进制读写，文件不存在，新建一个文件，存在文件，则覆盖文件内容

# a前缀的权限

# a追加，文件存在，则在文件末尾追加元素，文件不存在则新建文件
# ab二进制追加，文件存在，则在文件末尾追加元素，文件不存在则新建文件
# a+追加且可读，文件存在，则在文件末尾追加元素，文件不存在则新建文件
# ab+ 二进制追加可读，文件存在，则在文件末尾追加元素，文件不存在则新建文件
