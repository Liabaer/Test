# -*- coding: utf-8 -*-
import smtplib

import pytest

## fixture 参数  参数列表
# scope：可以理解成fixture的作用域，默认：function，还有class、module、package、session四个【常用】
# name：默认：装饰器的名称，同一模块的fixture相互调用建议写个不同的name

# 单独执行这个函数是不会执行的，因为他加fixture装饰器，所以pytest就不认为他是一个单元测试的函数所以强制执行会报错
# @pytest.fixture(scope='function',params=None,autouse=True,ids=None,name=None)
# def test():
#     print("fixture初始化的参数列表")
#     return True
#
# # # 这里的test,是上面的fixture构建的参数
# # def test_fixture(test):
# #     assert test != True
# #     print("使用fixture")




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






# fixture 的实例化顺序
# 较高 scope 范围的fixture（session）在较低 scope 范围的fixture（ function 、 class ）
# 之前实例化【session > package > module > class > function】
# 具有相同作用域的fixture遵循测试函数中声明的顺序，并遵循fixture之间的依赖关系
# 【在fixture_A里面依赖的fixture_B优先实例化，然后到fixture_A实例化】
# 自动使用（autouse=True）的fixture将在显式使用（传参或装饰器）的fixture之前实例化


# order = []
#
# @pytest.fixture(scope="session")
# def s1():
#     print('s1s1')
#     order.append('s1')
#
#
# @pytest.fixture(scope="module")
# def m1():
#     print("m1m1")
#     order.append("m1")
#
# @pytest.fixture
# def f1(f3,a1):
#     # 先实例化f3，再实例化a1，最后实例化f1
#     print(f3,'++++',a1,"------f1")
#     order.append("f1")
#     assert f3 == 123
#
#
# @pytest.fixture
# def f3():
#     order.append("f3")
#     a = 123
#     yield a
#
# @pytest.fixture
# def a1():
#     order.append("a1")
#
#
# @pytest.fixture
# def f2():
#     order.append("f2")
#
#
# def test_order(f1, m1, f2, s1):
#     # m1, s1在f1后，但因为scope 范围大，所以有会优先实例化
#     assert order == ["s1", "m1", "f3", "a1", "f1", "f2"]

# @pytest.fixture(scope="session")
# def o():
#     print("===打开浏览器===")
#     # a = True
#     # yield a
#     return True
#
# # 添加了 @pytest.fixture ，如果fixture还想依赖其他fixture，需要用函数传参的方式，
# # 不能用 @pytest.mark.usefixtures() 的方式，否则会不生效
# @pytest.fixture
# # @pytest.mark.usefixtures("open") #  不可取！！！不生效！！！
# def login(open):
#     # 方法级别前置操作setup
#     print(f"输入账号，密码先登录{open}")
#
#
# def test_login(o):
#     pass



# 用fixture实现teardown并不是一个独立的函数，而是用 yield 关键字来开启teardown操作

# @pytest.fixture(scope="session")
# def open():
#     # 会话前置操作setup
#     print("==打开浏览器==")
#     test = "测试变量是否返回"
#     yield test
#     # 会话后置操作teardown
#     print("==关闭浏览器==")
#
#
# @pytest.fixture
# def login(open):
#     print(f"输入账号，密码先登录{open}")
#     name = "==我是账号=="
#     pwd = "==我是密码=="
#     age = "==我是年龄=="
#     # 返回变量-返回的元组
#     yield name, pwd, age
#     # 方法级别后置操teardown
#     print("登录成功")
#
#
# def test_s1(login):
#     print("==用例1==")
#     # 返回的是一个元组
#     print(login)
#     # 分别赋值给不同变量
#     name, pwd, age = login
#     print(name, pwd, age)
#     assert "账号" in name
#     assert "密码" in pwd
#     assert "年龄" in age
#
#
# def test_s2(login):
#     print("==用例2==")
#     print(login)


# yield注意事项:
# 如果yield前面的代码，即setup部分已经抛出异常了，则不会执行yield后面的teardown内容
# 如果测试用例抛出异常，yield后面的teardown内容还是会正常执行



# yield+with的结合

# @pytest.fixture(scope="module")
# def smtp_connection():
#     with smtplib.SMTP("smtp.gamil.com", 587, timeout=5) as smtp_connection:
#         yield smtp_connection
# # 该 smtp_connection 连接将测试完成执行后已经关闭，因为 smtp_connection 对象自动关闭时，with 语句结束。



# addfinalizer 终结函数

@pytest.fixture(scope="module")
def test_addfinalizer(request):
    # 前置操作setup
    print("==再次打开浏览器==")
    test = "test_addfinalizer"

    def fin():
        # 后置操作teardown
        print("==再次关闭浏览器==")

    request.addfinalizer(fin)
    # 返回前置操作的变量
    return test


def test_anthor(test_addfinalizer):
    print("==最新用例==", test_addfinalizer)

# 注意事项
# 如果 request.addfinalizer() 前面的代码，即setup部分已经抛出异常了，
# 则不会执行 request.addfinalizer() 的teardown内容（和yield相似，应该是最近新版本改成一致了）
# 可以声明多个终结函数并调用