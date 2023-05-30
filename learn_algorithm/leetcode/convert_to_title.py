# -*- coding: utf-8 -*-
# 给你一个整数columnNumber，返回它在Excel表中相对应的列名称
columnNumber = 28
temp = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M',
        14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
        26: 'Z'}
res = ''
# 小于26的时候直接从字典取值
if columnNumber <= 26:
    res = temp[columnNumber]
else:
    # 大于0的时候进入循环
    while columnNumber > 0:
        # 取余是0 的时候，字典没有对应取值，相当于已经整除了z，所以借一位 res加上Z，
        if columnNumber % 26 == 0:
            res = 'Z' + res
            # 除以26 - 1，-1是0 的时候 借一位
            columnNumber = columnNumber // 26 - 1
        else:
            # 取余不为0的时候，取字典值，再整除26
            res = temp[columnNumber % 26]+res
            columnNumber = columnNumber // 26
print(res)


#
# class Solution:
#     def convertToTitle(self, columnNumber: int) -> str:
#         result=""
#         d={'1':'A','2':'B','3':'C','4':'D','5':'E','6':'F','7':'G','8':'H','9':'I','10':'J','11':'K','12':'L','13':'M', '14':'N','15':'O','16':'P','17':'Q','18':'R','19':'S','20':'T','21':'U','22':'V','23':'W','24':'X','25':'Y','26':'Z'}
#         while columnNumber/26>1:
#             if columnNumber%26!=0:
#                 result=d[str(columnNumber%26)]+result
#                 columnNumber = columnNumber//26
#             else:
#                 result=d[str(26)]+result
#                 columnNumber = columnNumber//26-1
#         else:
#             result=d[str(columnNumber)]+result
#         return result
#
# print(Solution().convertToTitle(columnNumber))