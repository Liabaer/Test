# -*- coding: utf-8 -*-

import pytest

## fixture 参数  参数列表
# scope：可以理解成fixture的作用域，默认：function，还有class、module、package、session四个【常用】
# name：默认：装饰器的名称，同一模块的fixture相互调用建议写个不同的name

# 单独执行这个函数是不会执行的，因为他加fixture装饰器，所以pytest就不认为他是一个单元测试的函数所以强制执行会报错
@pytest.fixture(scope='function',params=None,autouse=True,ids=None,name=None)
def test():
    print("fixture初始化的参数列表")
    return True

# # 这里的test,是上面的fixture构建的参数
# def test_fixture(test):
#     assert test != True
#     print("使用fixture")




# 测试用例调用fixture
# 如果fixture有返回值，用 @pytest.mark.usefixtures() 是无法获取到返回值的，必须用传参的方式（方式一）


# # 调用方式一 将fixture名称作为测试用例函数的输入参数
# @pytest.fixture
# def login():
#     print("输入账号，密码先登录")
#
#
# def test_s1(login):
#     print("用例 1：登录之后其它动作 111")
#
#
# def test_s2():  # 不传 login
#     print("用例 2：不需要登录，操作 222")
#
# #
# # # 调用方式二 测试用例加上装饰器：@pytest.mark.usefixtures(fixture_name)
# @pytest.fixture
# def login2():
#     print("please输入账号，密码先登录")
#
#
# @pytest.mark.usefixtures("login2", "login")
# def test_s11():
#     print("用例 11：登录之后其它动作 111")
#
# #
# # # 调用方式三 fixture设置autouse=True
# # # autouse：默认：False，需要用例手动调用该fixture；如果是True，所有作用域内的测试用例都会自动调用该fixture
# @pytest.fixture(autouse=True)
# def login3():
#     print("====auto===")
#
#
# # 不是test开头，加了装饰器也不会执行fixture
# @pytest.mark.usefixtures("login2")
# def loginss():
#     print(123)


# 在类声明上面加 @pytest.mark.usefixtures() ，代表这个类里面所有测试用例都会调用该fixture
# 可以叠加多个 @pytest.mark.usefixtures() ，先执行的放底层，后执行的放上层
# 可以传多个fixture参数，先执行的放前面，后执行的放后面
