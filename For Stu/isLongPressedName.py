# -*- coding: utf-8 -*-
# 你的朋友正在使用键盘输入他的名字name。偶尔，在键入字符c时，按键可能会被长按，而字符可能被输入 1 次或多次。
#
# 你将会检查键盘输入的字符typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回True

name = "alex"
typed = "aaleex"
i = 0
j = 0
while i < 0 and j < 0:
    if name[i] == typed[j]:
        i = i + 1
        j = j + 1
    else:
       if name[i] == typed[j + 1] and j + 1<=len(typed):
           j = j + 1



