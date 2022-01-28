# -*- coding: utf-8 -*-
# 在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在(0, 0) 处结束。
#
# 移动顺序由字符串表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有R（右），L（左），U（上）和 D（下）。如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。
#
# 注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。
moves = "LL"
# 方法二
x = 0
y = 0
i = 0
flag = True
while i < len(moves):
    if moves[i] == 'U':
        y = y + 1
    if moves[i] == 'D':
        y = y - 1
    if moves[i] == 'R':
        x = x + 1
    if moves[i] == 'L':
        x = x - 1
    i = i + 1
if x != 0 or y != 0:
    flag = False
print(flag)

# 方法一
# dict_moves = {}
# i = 0
# flag = True
# while i < len(moves):
#     if moves[i] not in dict_moves:
#         dict_moves[moves[i]] = 1
#     else:
#         dict_moves[moves[i]] = dict_moves[moves[i]] + 1
#     i = i + 1
# print(dict_moves)
# if 'U' in dict_moves and 'D' not in dict_moves:
#     flag = False
# if 'U' not in dict_moves and 'D' in dict_moves:
#     flag = False
# if 'U' in dict_moves and 'D' in dict_moves:
#     if dict_moves['U'] != dict_moves['D']:
#         flag = False
# if 'L' in dict_moves and 'R' not in dict_moves:
#     flag = False
# if 'L' not in dict_moves and 'R' in dict_moves:
#     flag = False
# if 'L' in dict_moves and 'R' in dict_moves:
#     if dict_moves['L'] != dict_moves['R']:
#         flag = False
# print(flag)
