# -*- coding: utf-8 -*-
import pytest


#
#
# class Test_ABC:
#     def setup_class(self):
#         print("------->setup_class")
#
#     def teardown_class(self):
#         print("------->teardown_class")
#
#     def test_a(self):
#         print("------->test_a")
#         assert 1
#
#     def test_b(self):
#         print("------->test_b")
#         assert 0  # 断言失败```


# 运行方式：
# 1.
# 修改Test_App / pytest.ini文件，添加报告参数，即：addopts = -s - -html =./ report.html
# # -s:输出程序运行信息
# # --html=./report.html 在当前目录下生成report.html文件
# ️
# 若要生成xml文件，可将 - -html =./ report.html
# 改成 - -html =./ report.xml
# 2.
# 命令行进入Test_App目录
# 3.
# 执行命令： pytest
# 执行结果：
# 1.
# 在当前目录会生成assets文件夹和report.html文件

#
# class Test_ABC:
#     @pytest.fixture()
#     def before(self):
#         print("------>before")
#
#     def test_a(self, before):
#         print("----->test_a")
#         assert 1
#
#
# if __name__ == '__main__':
#     pytest.main(["-s test_a.py"])


# @pytest.fixture(scope='class', autouse=True)
# def before():
#     print("----->before")
#
#
# # @pytest.mark.usefixtures("before")
# class Test_ABC:
#     def setup(self):
#         print("------>setup")
#
#     def test_a(self):
#         print("------>test_a")
#         assert 1
#
#     def test_b(self):
#         print("------>test_b")
#         assert 1
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_a.py'])



# @pytest.fixture(params=[1, 2, 3])
# def need_data(request):
#     return request.param
#
# class Test_ABC:
#
#     def test_a(self, need_data):
#         print("----->test_a")
#         assert need_data != 3
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_a.py'])



# class Test_ABC:
#     def setup_class(self):
#         print("------->setup_class")
#
#     def teardown_class(self):
#         print("------>teardown_class")
#
#
#     def test_a(self):
#         print("------>test_a")
#         assert 1
#
#     @pytest.mark.skipif(condition=2>1,reason="跳过介个函数")
#     def test_b(self):
#         print("------>test_b")
#         assert 0
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_a.py'])



# class Test_ABC:
#     def setup_class(self):
#         print("------->setup_class")
#
#     def teardown_class(self):
#         print("------>teardown_class")
#
#
#     def test_a(self):
#         print("------>test_a")
#         assert 1
#
#     @pytest.mark.xfail(2 > 1, reason="标记为预期失败")
#     def test_b(self):
#         print("------>test_b")
#         assert 0
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_a.py'])



#
# class Test_ABC:
#     def setup_class(self):
#         print("------->setup_class")
#
#     def teardown_class(self):
#         print("------>teardown_class")
#
#
#     @pytest.mark.parametrize("a,b", [(1,2),(0,3)])
#     def test_a(self, a,b):
#         print("test data:a=%d,b=%d"%(a,b))
#         assert a + b == 3
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', 'test_a.py'])



import pytest
def return_test_data():
    return [(1, 2), (0, 3)]
class Test_ABC:
    def setup_class(self):
        print("------->setup_class")
    def teardown_class(self):
            print("------->teardown_class")

    @pytest.mark.parametrize("a,b", return_test_data())
    def test_a(self, a,b):
        print("test data:a=%d,b=%d"%(a,b))
        assert a + b == 3


if __name__ == '__main__':
    pytest.main(['-s', 'test_a.py'])














