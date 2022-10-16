# -*- coding: utf-8 -*-
import pymysql

# 连接数据库获取connection对象
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='', db='learn_database')
# 获取操作数据库的对象
db = connection.cursor(pymysql.cursors.DictCursor)

# 执行查询
db.execute("select * from t_order")
# 获取执行sql的全部结果 （因为我们没有limit)
# result = db.fetchall()
# # 结果是一个字典数组
# # print(result)
# db.execute("select * from t_order")
# # 获取执行sql的第一条结果
# result = db.fetchone()
# db.fetchone()这个是获取一条结果， db.fetchall()这个是获取查出来的所有结果。
# # 结果是一个字典
# print(result)
# #
# # 执行增删改sql
#
# # 我们执行一条插入的sql，%s表示需要传入的值，后面的元祖的顺序就是他传入的值
# db.execute("insert into t_order(id, order_price) values (%s, %s)", ('142234', 100))
# # 凡事执行insert delete update语句都需要提交事务，才会修改数据库的状态
# connection.commit()
# # 打印新插入的这条的id
# print(db.lastrowid)
# 执行sql
db.execute("select * from t_order")
# 获取执行sql的结果
result = db.fetchall()
print(result)
#
# 执行更新sql
db.execute("update t_order set shop_location = %s where id = %s", ('3.2,101.22', '142234'))
print(result)
connection.commit()
