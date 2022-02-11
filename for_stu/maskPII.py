# -*- coding: utf-8 -*-
# 给你一条个人信息字符串 s ，可能表示一个 邮箱地址 ，也可能表示一串 电话号码 。返回按如下规则 隐藏 个人信息后的结果：
# 电子邮件地址：
# 一个电子邮件地址由以下部分组成：
# 一个 名字 ，由大小写英文字母组成，后面跟着
# 一个 '@' 字符，后面跟着
# 一个 域名 ，由大小写英文字母和一个位于中间的 '.' 字符组成。'.' 不会是域名的第一个或者最后一个字符。
#
# 要想隐藏电子邮件地址中的个人信息：
# 名字 和 域名 部分的大写英文字母应当转换成小写英文字母。
# 名字 中间的字母（即，除第一个和最后一个字母外）必须用 5 个 "*****" 替换。
#
# 电话号码：
# 一个电话号码应当按下述格式组成：
# 电话号码可以由 10-13 位数字组成
# 后 10 位构成 本地号码
# 前面剩下的 0-3 位，构成 国家代码
# 利用 {'+', '-', '(', ')', ' '} 这些 分隔字符 按某种形式对上述数字进行分隔
#
# 要想隐藏电话号码中的个人信息：
# 移除所有 分隔字符
# 隐藏个人信息后的电话号码应该遵从这种格式：
# "***-***-XXXX" 如果国家代码为 0 位数字
# "+*-***-***-XXXX" 如果国家代码为 1 位数字
# "+**-***-***-XXXX" 如果国家代码为 2 位数字
# "+***-***-***-XXXX" 如果国家代码为 3 位数字
# "XXXX" 是最后 4 位 本地号码


s = "LeetCode@LeetCode.com"


def secrets_s_phone(s, secrets_symbol, symbol):
    """
    加密手机号
    :param s: 入参
    :param secrets_symbol: 加密的"**"模板
    :param symbol: 不需要的特殊符号
    :return: 返回加密后的手机格式
    """
    new_phone = ''
    n = 0
    while n < len(s):
        if s[n] in symbol:
            n = n + 1
            continue
        else:
            if len(s) - 4 <= n:
                new_phone = new_phone + s[n]
            if len(new_phone) == 4:
                new_phone = secrets_symbol + new_phone
                break
            n = n + 1
    return new_phone


def lower_s(s):
    """
    将大写转为小写
    :param s: 传入的要计算的字符串
    :return: 返回小写的字符串
    """
    s_new = ''
    i = 0
    while i < len(s):
        # 将字符串转换成小写
        if 65 <= ord(s[i]) <= 90:
            # print(chr(ord(s[i]) + 32))
            # chr()将asscii码转换成字母，ord(）求字母的asscii码
            s_new = s_new + str(chr(ord(s[i]) + 32))
        else:
            s_new = s_new + s[i]
        i = i + 1
    return s_new


def secrets_s_email(s_new):
    """
    邮箱加密
    :param s_new: 传入的处理后的字符串
    :return:返回加密的邮箱
    """
    secrets_s_email = ''
    j = 0
    j_index = 0
    b = "*****"
    while j < len(s_new):
        if j == 0:
            secrets_s_email = s_new[0]
        # print(secrets_s_email)
        if j + 1 < len(s_new) and s_new[j + 1] == '@':
            secrets_s_email = secrets_s_email + b
            secrets_s_email = secrets_s_email + s_new[j] + s_new[j + 1]
            # 这里让j_index 等于@位置的下标
            j_index = j + 1
        # j_index必须要有值且比@位置大的再放入结果
        if j > j_index != 0:
            secrets_s_email = secrets_s_email + s_new[j]
        j = j + 1
    return secrets_s_email


if '@' in s:
    # 是邮箱
    print(secrets_s_email(lower_s(s)))
else:
    # 是手机号码
    m = 0
    num = 0
    remove_symbol_s = ''
    symbol = {'+', '-', '(', ')', ' '}
    while m < len(s):
        # 先判断国家代码
        if s[m] not in symbol:
            remove_symbol_s = remove_symbol_s + s[m]
            num = num + 1
        m = m + 1
    print(remove_symbol_s)
    # "***-***-XXXX" 如果国家代码为 0 位数字
    new_phone = ''
    if num == 10:
        new_phone = secrets_s_phone(remove_symbol_s, '***-***-', symbol)
        # print(new_phone)
    # "+*-***-***-XXXX" 如果国家代码为 1 位数字
    if num == 11:
        new_phone = secrets_s_phone(remove_symbol_s, '+*-***-***-', symbol)
        # print(new_phone)
    # "+**-***-***-XXXX" 如果国家代码为 2 位数字
    if num == 12:
        new_phone = secrets_s_phone(remove_symbol_s, '+**-***-***-', symbol)
        # print(new_phone)
    # "+***-***-***-XXXX" 如果国家代码为 3 位数字
    if num == 13:
        new_phone = secrets_s_phone(remove_symbol_s, '+***-***-***-', symbol)
        # print(new_phone)
    print(new_phone)

