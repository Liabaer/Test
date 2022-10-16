# -*- coding: utf-8 -*-

# 1. 类：用于定义私有函数，公有函数，私有属性，共有属性
# 2. 对象：由类生成的，可以调用类的函数和属性
# 3. 私有函数/属性：只能由对象调用
# 4. 公有函数/属性：可以由对象或者类名同时调用
# 5. 私有函数定义： 函数第一个参数必须是self，同时函数里面的内容必须使用了self变量
# 6. 公有函数定义：函数中不能使用self变量，同时函数名上一行必须有@staticmethod语句指明是公有函数
# 7. 私有属性定义：定义在__init__函数中，最好指定选填参数
# 8. 公有属性定义： 定义在类中，函数之外即可。

class User(object):
    """
    定义一个用户类，User是类名 括号object可以省略不写，这里表示User是集成Object类的，
    所有类都是继承object类的，所以也可以不写直接class User:就好了，后面讲继承再具体讲解（因为Python的继承会很少用）
    下面所有的静态 全局字眼，可以理解成公开权限的意思
    """

    # 全局属性 可以直接用类名点的方法调用，也可以通过对象调用，不同对象直接值也是一样的
    static_name = "test_name"

    # # 如果我们有时想传参数有时不想传参数怎么办呢 todo 使用选填参数，测试一下看看
    # self 参数是对类的当前实例的引用，用于访问属于该类的变量。
    # 它不必被命名为 self，您可以随意调用它，但它必须是类中任意函数的首个参数：
    # 使用 __init__() 函数为 name 和 age 赋值
    def __init__(self, email="", password=""):
        # def __init__(self, email, password):
        """
        定义初始化类的方法(可以省略） ，这里表示该类有2个属性email和password（不同对象值是不一样的）
        :param email:
        :param password:
        """
        self.email = email
        self.password = password

    def print_user_info(self, s):
        """
        定义类的私有函数（需要通过new 一个对象 通过对象来调用），注意，如果函数中使用到了属性，就需要加self,在一个参数，如果没有使用属性，就不用加self
        :param s: 这个参数之所以加进来，是想说明这个函数可以传参数的
        :return:
        """
        print("email = {} password = {} s = {}".format(self.email, self.password, s))

    @staticmethod
    def print_user_info_static(s):
        """
        定义类的全局函数（可以直接用类名点的方法调用，也可以通过对象调用） 需要在函数前面加一个修饰语句 @staticmethod，表示它是一个静态方法 static method
        :param s: 这个参数之所以加进来，是想说明这个函数可以传参数的
        :return:
        """
        print("s = {}".format(s))


# new 一个User类的对象，注意Python不需要写new User() User即可

# 会报错，因为我们定义了初始化方法需要传入参数
# user = User()
# 如果定义函数时选择选填参数 就不会报错了
user = User(email='abc@test.com')
user.password = input()
user = User(password='1234')
# 正确写法
# user_test1 = User("。@test.com", "testPassword")


# 获取私有属性，需要通过对象
# print(user_test1.email)
# print(user_test1.password)
# # 通过类名获取，报错，因为他是私有的
# # print(User.email)
# # print(User.password)
# # 静态属性 可以通过类名或者对象访问
# print(User.static_name)
# print(user_test1.static_name)
#
user_test2 = User("test2@test.com", "test2password")

# 不用对象直接的私有属性值不一致
# print("email 1: {} password 1:{}".format(user_test1.email, user_test1.password))
# print("email 2: {} password 2:{}".format(user_test2.email, user_test2.password))

# 不同对象直接静态属性值一致
# print("name 1: {} name 2: {}".format(user_test1.static_name, user_test2.static_name))

# # 可以修改静态属性的值
# User.static_name = "update name"  # 可以通过类名点的方法修改是所有对象都会修改
# print("name 1: {} name 2: {}".format(user_test1.static_name, user_test2.static_name))
# # 通过对象点的方法只作用于当前对象
# user_test1.static_name = "hhh"
# print("name 1: {} name 2: {}".format(user_test1.static_name, user_test2.static_name))

# 调用私有方法
# user_test1.print_user_info("测试私有方法1")
# 错误写法
# print(User.print_user_info("测试私有方法"))
# 可以这样写但是不推荐
# 这里其实前面相当于new了个新的对象只是没用变量存起来是一个临时的对象
# User("test", "test").print_user_info("测试私有方法2")

# # 调用公共方法
# user_test1.print_user_info_static("测试公共方法1")
# User.print_user_info_static("测试公共方法2")

# 拓展 讲解一下类反射知识
# 反射就是我们代码类已经写好的前提下，不修改类中的代码，通过反射，获取和修改类的信息（后面会讲解）
# 通过type测试我们的对象的类型
# print(type(user_test1))
# 通过dir查看类的属性和函数，打印了很多除了我们写的，其他都是继承自object类，报错我们调用的__dir__()就是Object类的方法
# print(user_test1.__dir__())
# # 上面这个最大的用途就是，举个例子比如我们的pycharm软件，写代码的时候会提示这个变量，有什么属性或者函数，他这个提示，其实就是调用了dir方法，来提示我们，也就是上面说的获取类的信息
# # hasattr判断对象是否有函数或者属性 （pycharm报错和警告就是这个原理，判断有没有这个属性）
# print(hasattr(user_test1, "print_user_info"))
# print(hasattr(user_test1, "email"))
# # print(hasattr(user_test1, "userName"))
# # # 为一个已经编写好的类的某个对象新增属性，只作用该对象 （一般用于，不想修改别人的代码，又不想在别人的代码上改动，直接通过反射增强他类的功能，很多框架就是做这个事情）
# setattr(user_test1, "add_new_filed", "我是新增的属性")
# # # # 判断是否设置成功，直接打印方式
# print(user_test1.add_new_filed)  # 只所以是警告，是因为编译器不够只能，我们这个是通过反射加入的新变量
# # getattr获取字段的值
# print(getattr(user_test1, "add_new_filed"))
# # 报错写法，因为setattr只做用传入的对象
# # print(user_test2.add_new_filed)
# # print(getattr(user_test2, "add_new_filed"))
#
# # # 为一个已经编写好的类,作用与该类的所有对象，因为他是全局的新增
# setattr(User, "static_new_filed", "我是新增的公共属性")
# print(user_test1.static_new_filed)
# print(user_test2.static_new_filed)
# print(getattr(user_test2, "static_new_filed"))
