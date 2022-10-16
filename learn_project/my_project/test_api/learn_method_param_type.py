# -*- coding: utf-8 -*-
def test_a(a: str = "", b: int = 0) -> str:
    """
    (这个函数定义了2个选填参数，使用: str的方法，告诉他是一个字符串类型的变量。最后那个-> str，是告诉这个函数的返回值也是字符串变量)
    定义一个函数 a必须传入str，且默认值是空 b必须传入int，且默认值是0 返回值必须是字符串
    :param a:
    :param b:
    :return:
    """
    return a + str(b)


# 会黄色警告，告诉你第一个参数应该是字符串
# test_a(a=1, b=2)
test_a(a='1', b=2)
