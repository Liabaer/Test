# -*- coding: utf-8 -*-
# 常用断言
# pytest 里面断言实际上就是 python 里面的 assert 断言方法，常用的有以下几种
# assert xx ：判断 xx 为真
# assert not xx ：判断 xx 不为真
# assert a in b ：判断 b 包含 a
# assert a == b ：判断 a 等于 b
# assert a != b ：判断 a 不等于 b

# def f():
#     return 3
#
# def test_function():
#     a = f()
#     assert a % 2 == 0,"判断 a 为偶数，当前 a 的值为：%s" % a


# 断言异常
import pytest

# 断言场景：断言它抛的异常是不是预期想要的
# 代码执行：1/0
# 预期结果：抛的异常是ZeroDivisionError: division by zero
# 如何断言：通常是断言异常的 type 和 value 值了
# 具体方式：这里 1/0 的异常类型是 ZeroDivisionError，异常的 value 值是 divisionby zero

#
# def test_zero_division():
#     # with pytest.raises(ZeroDivisionError) as excinfo:
#     # 1 / 0
#     # with pytest.raises() 就是将下面运行的代码可能会抛出的ZeroDivisionError捕获
#     with pytest.raises(ZeroDivisionError) as excinfo:
#         1 / 0

    # 断言异常类型 type
    # assert excinfo.type == ZeroDivisionError
    # 断言异常 value 值
    # assert "division by zero" in str(excinfo.value)

    # excinfo ：是一个异常信息实例
    # 主要属性： .type 、  .value 、 .traceback
    # 注意：断言 type 的时候，异常类型是不需要加引号的，断言 value值的时候需转 str


# 拓展：match  只能匹配value，不能匹配type
# 可以将match关键字参数传递给 上下文管理器，以测试正则表达式 与 异常字符串 表示形式 是否匹配

# # 自定义消息 value：division by zero  type：ZeroDivisionError
# def test_zero_division_long():
#     with pytest.raises(ZeroDivisionError, match=".*zero.*") as excinfo:
#         1/0
#     # assert excinfo.type == ZeroDivisionError
#
#
#
# def test_zero_division_long2():
#     #  pytest.raises(ZeroDivisionError, match="zero")这个是捕获异常，然后as是将前面捕获的异常给后面的变量
#     with pytest.raises(ZeroDivisionError, match="zero") as excinfo:
#         1/0
#     # assert excinfo.type == ZeroDivisionError
#


# 拓展 检查断言装饰器

# 相当于一个检查异常装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
# 本来这个函数要抛出异常，但是他将要抛出的异常与装饰器里面的raises指定的异常type是一致的，所以不会报错
#
def test_f():
    1/0


# with pytest.raise(ZeroDivisionError)  对于故意测试异常代码的情况，使用可能会更好
# 而@pytest.mark.xfail(raises=ZeroDivisionError) 对于检查未修复的错误（即，可能会发生异常），使用检查断言可能会更好



