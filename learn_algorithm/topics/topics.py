# -*- coding: utf-8 -*-
# 001
# nums = [3,2,3]
# n = len(nums)/3
# res_dict={}
# res = []
# for i in nums:
#     res_dict[i] = res_dict.get(i,0)+1
# for k in res_dict:
#     if res_dict[k] > n and k not in res:
#         res.append(k)
# print(res)

# res = []
# for i in nums:
#     if nums.count(i) > n and i not in res:
#         res.append(i)
# print(res)


# for i in range(len(nums)):
#     flag = False
#     if i+1 < len(nums) and nums[i+1] == nums[i]:
#         count += 1
#         flag = True
#     else:
#         continue
#     if flag:
#         print(count)


# 002
# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用补码运算方法。 2022.07.31
# 注意：
# 1.十六进制中所有字母(a-f)都必须是小写。
# 2.十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中 的第一个字符将不会是0字符。
# 2022.07.3
# 3.给定的数确保在32位有符号整数范围内。
# 4.不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

# num = 26
# print(hex(num))
# temp={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
# num_list = []
# while num != 0:
#     if num % 16 in temp:
#         num_list.append(temp[num % 16])
#     else:
#         num_list.append(str(num % 16))
#     num = num // 16
# num_list.reverse()
# print(num_list)
# print(''.join(num_list))

# # 负数转正数处理
# if num < 0:
#     num = 2 ** 32 + num
# # a = hex(num)
# # 去掉0x
# # print(a[2:])


# 给定一个二进制数组 nums ,计算其中最大连续1的个数。
# nums = [0, 0]
# res = []
# count = 1
# for i in range(0, len(nums)):
#     if i+1 < len(nums) and nums[i+1] == nums[i] and nums[i]==1:
#         count += 1
#     else:
#         if nums[i] == 1:
#             res.append(count)
#             count = 1
# if len(res)==0:
#     print(0)
# print(max(res))


# 给你一个数组rr,请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用-1替换。
# 完成所有替换操作后，请你返回这个数组。
# arr = [17, 18, 5, 4, 6, 1]
#
# ans = []
# for i in range(0, len(arr)):
#     ans.append(-1)
# for i in range(len(arr) - 2, -1, -1):
#     # ans[i]数组其实表示的第i位后面数字的最大值，那么我们计算ans[i] ，只要判断ans[i+1]（第i+1位后面的最大值）和arr[i + 1]的（和第i+1位的值）
#     print(i)
#     ans[i] = max(ans[i+1], arr[i + 1])
#     print('+++'+str(ans[i]))
# print(ans)


# new_arr = []
# for i in range(0, len(arr)-1):
#     new_arr.append(max(arr[i+1:]))
# new_arr.append(-1)
# print(new_arr)


# for i in range(0, len(arr)):
#     temp = 0
#     flag = False
#     for j in range(i+1, len(arr)):
#         if j != len(arr):
#             if arr[j] > temp:
#                 temp = arr[j]
#     if temp !=0:
#         new_arr.append(temp)
# new_arr.append(-1)
# print(new_arr)
# temp = 0
# for j in range(1, len(arr)):
#     if j != len(arr):
#         if arr[j] > temp:
#             temp = arr[j]
#             flag = True
#         else:
#             new_arr.append(temp)
#             temp = 0
#     else:
#         new_arr.append(-1)
# print(new_arr)


# 给你两个字符串数组words1和words2，请你返回在两个字符串数组中都恰好出现一次的字符串的数目。
# words1 = ["leetcode","is","amazing","as","is"]
# words2 = ["amazing","leetcode","is"]
#
# def mad_dict(words):
#     dict = {}
#     for i in words:
#         dict[i] = dict.get(i, 0)+1
#     return dict
#
# w1 = mad_dict(words1)
# w2 = mad_dict(words2)
# count = 0
# for k in w1:
#     if w1[k] == 1:
#         if k in w2 and w2[k] == 1:
#             print(k)
#             count +=1
#         else:
#             continue
#     else:
#         continue
# print(count)


# 给你一个整数数组digits，其中每个元素是一个数字（0-9)。数组中可能存在重复元素。
# 你需要找出所有满足下述条件且互不相同的整数：
# ·该整数由digits中的三个元素按任意顺序依次连接组成。
# ·该整数不含前导零
# ·该整数是一个偶数
#
# 例如，给定的digits是[1,2,3]，整数132和312满足上面列出的全部条件。
# 将找出的所有互不相同的整数按递增顺序排列，并以数组形式返回。

# digits = [2, 1, 3, 0]
# res_temp = {}
# res = []
#
# for i in digits:
#     res_temp[i] = res_temp.get(i, 0)+1
#
# for i in range(100, 999):
#     temp_dict = {}
#     one = i//100
#     two = i//10 % 10
#     three = i % 10
#     temp_dict[one] = temp_dict.get(one, 0) + 1
#     temp_dict[two] = temp_dict.get(two, 0) + 1
#     temp_dict[three] = temp_dict.get(three, 0) + 1
#     flag = False
#     for k in temp_dict:
#         if k in res_temp and temp_dict[k] <= res_temp[k]:
#             flag = True
#         else:
#             flag = False
#             break
#     if flag and i%2 == 0:
#         res.append(i)
# print(res)

# for i in range(0, len(digits)):
#     for j in range(0, len(digits)):
#
#         k = 0
#         while k < len(digits):
#             s = ''
#             if digits[i] != digits[j] and digits[j] != digits[k] and digits[i] != digits[k]:
#                 s += str(digits[i])+str(digits[j])+str(digits[k])
#             k += 1
#             if len(s) == 3:
#                 if s[0] != '0' and int(s) % 2 == 0 and s not in res:
#                     print(s)
#                     res_temp[int(s)] = res_temp.get(int(s), 0)+1
#                 else:
#                     continue
# for k in res_temp:
#     if res_temp[k] == 1:
#         res.append(k)
# res.sort(reverse=False)
# print(res)

# 编写一个算法来判断一个数n是不是快乐数。
# 「快乐数」定义为：
# ·对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# ·然后重复这个过程直到这个数变为1，也可能是无限循环但始终变不到1。
# # ·如果这个过程结果为1，那么这个数就是快乐数。
# # 如果n是快乐数就返回true;不是，则返回false。
# def isHappy(n):
#     """
#     :type n: int
#     :rtype: bool
#     """
#     cnt = 0
#     while int(n) > 1:
#         a = str(n)
#         n = 0
#         for i in a:
#             n += int(i) * int(i)
#         cnt += 1
#         if cnt > 1000:
#             return False
#     if int(n) == 1:
#         return True
#     else:
#         return False


# 给定整数n，返回所有小于非负整数n的质数的数量。
#
# def countPrimes(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     visit = []
#     for i in range(0, n):
#         visit.append(True)
#     for i in range(2, n):
#         if visit[i]:
#             j = i + i
#             while j < n:
#                 visit[j] = False
#                 j += i
#     ans = 0
#     for i in range(2, n):
#         if (visit[i]):
#             ans += 1
#     return ans
#
#
# ans = countPrimes(n=10)
# print(ans)

# if n == 0:
#     print(0)
# for m in range(2, n):
#     flag = True
#     for i in range(2, m):
#         if m % i == 0:
#             flag = False
#             break
#     if flag:
#         cnt += 1
# print(cnt)


# 给你一个长度为n的整数数组nums，请你返回nums中最接近0的数字。如果有多个答案，请你返回它们中的最大值。
# def findClosestNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     temp = pow(10, 5) + 10
#     res = 0
#     for i in nums:
#         if abs(i) < temp:
#             temp = abs(i)
#             res = i
#         elif abs(i) == temp:
#             if res < i:
#                 res = i
#             else:
#                 continue
#         else:
#             continue
#     return res


# 给你一个整数，请你每隔三位添加点（即""符号）作为千位分隔符，并将结果以字符串格式返回。
# n = 1234
# n = str(n)
# s = []
# if len(n) <= 3:
#     print(n)
# else:
#     cnt = 0
#     for i in range(len(n)-1, -1, -1):
#         # print(i)
#         s.append(n[i])
#         cnt += 1
#         print(s)
#         if cnt % 3 == 0 and i != len(n)-1:
#             s.append('.')
#     s.reverse()
#     print(''.join(s))


# n = str(n)
#
# s = ''
# if len(n) <= 3:
#     print(n)
# else:
#     for i in range(0, len(n)):
#         # print(i)
#         if i % 3 == 0 and i != len(n)-1:
#             s = s + n[i]
#             s += '.'
#         else:
#             s = s + n[i]
#     print(s)


# 给你一个仅由数字6和9组成的正整数 num
# 你最多只能翻转一位数字，将6变成9，或者把9变成6。
# 请返回你可以得到的最大数字。
#
# num = 9999
# temp = 0
# if num > int(temp):
#     new = ''
#     flag = False
#     for i in str(num):
#         if i == '6' and flag == False:
#             new += '9'
#             flag = True
#             continue
#         new += i
#     temp = int(new)
# print(temp)

# 给你两个二进制字符串，返回它们的和（用二进制表示)。
# 输入为非空字符串且只包含数字1和0。 1011 = 1 * 2 ^3 + 0 * 2 ^2 + 1 * 2  ^ 1 + 1 * 2 ^ 0
# a = "11"
# b = "1"
#
#
# def two_to_ten(s):
#     new_s = 0
#     temp = 0
#     for i in range(len(s) - 1, -1, -1):
#         print(i, s[i])
#         new_s += int(s[i]) * pow(2, temp)
#         temp += 1
#     return new_s
#
#
# new_a = two_to_ten(a)
# new_b = two_to_ten(b)
# res = new_a + new_b
# res_list = []
# while res != 0:
#     res_list.append(str(res % 2))
#     res = res // 2
# res_list.reverse()
# print(''.join(res_list))

# print(new_a,new_b,bin(res))


# 给你两个字符串：ransomNote和magazine,判断ransomNote能不能由magazine里面的字符构成。
# 如果可以，返回true;否则返回false。
# magazine中的每个字符只能在ransomNote中使用一次。
# ransomNote = "aa"
# magazine = "aab"
#
# ransomNote_dict = {}
# magazine_dict = {}
# for i in ransomNote:
#     ransomNote_dict[i] = ransomNote_dict.get(i,0)+1
# for i in magazine:
#     magazine_dict[i] = magazine_dict.get(i,0)+1
# if len(magazine) <= pow(10,5)+10:
#     flag = False
#     for k in magazine_dict:
#         if k in ransomNote_dict and magazine_dict[k] == ransomNote_dict[k]:
#             flag = True
#     if flag:
#         print(True)
#     else:
#         print(False)
# else:
#     print(True)

# 给你一个字符串s和一个字符letter,返回在s中等于letter字符所占的百分比，向下取整到最接近的百分比。
import math

# s = "foobar"
# letter = "o"
# l = len(s)
# s_dict={}
# for i in s:
#     s_dict[i] = s_dict.get(i,0)+1
# print(s_dict)
# res = 0
# for i in s_dict:
#     if letter == i:
#         res = round(s_dict[i]/l * 100)
# print(res)
#
# colors =[1,8,3,8,3]
# cnt = 1
# cnt_list = []
# temp = 0
# for i in range(0, len(colors)):
#     for j in range(i+1, len(colors)):
#         # print(colors[i])
#         if colors[i] == colors[j]:
#             cnt += 1
#         else:
#             if abs(i-j) > temp:
#                 temp = abs(i-j)
#             cnt = 0
# print(temp)

# 给你两个非负整数1ow和high。请你返回1ow和high之间（包括二者)奇数的数目。
# low = 3
# high = 7
# for i in range(low,high+1):
#     if i%2!=0:
#         print(i)

# 给你两个字符串数组word1和word2。如果两个数组表示的字符串相同，返回true;否则，返回false。
# 数组表示的字符串是由数组中的所有元素按顺序连接形成的字符串。
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
#
# def become_str(word):
#     s = ''
#     for i in word:
#         if 1 <= len(i)<=pow(10,3):
#             s += i
#     return s
#
#
# if 1<=len(word1)<=pow(10,3) and 1<=len(word2)<=pow(10,3):
#     s1 = become_str(word1)
#     s2 = become_str(word2)
#     if 1 <= len(s1) <= pow(10, 3) and 1 <= len(s2) <= pow(10, 3):
#         if s1 == s2:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(False)
# else:
#     print(False)


# 给你一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。

#
# class Solution(object):
#     def find_third(self, l):
#         temp = []
#         t = max(l)
#         for i in l:
#             if i != t:
#                 temp.append(i)
#         return temp
#
#     def thirdMax(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         temp1 = self.find_third(nums)
#         res_list = self.find_third(temp1)
#         return max(res_list)
#
#
# nums = [2, 2, 3, 1]
# print(Solution().thirdMax(nums))


# 给你一个字符串s表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字 符：
# 。'A':Absent,缺勤 。'工'：Late,迟到
# ·'p':Present,到场

# 如果学生能够同时满足下面两个条件，则可以获得出勤奖励：
# 。按总出勤计，学生缺勤（'A')严格少于两天。
# ·学生不会存在连续3天或连续3天以上的迟到（'工')记录。
# # 如果学生可以获得出勤奖励，返回true;否则，返回false。
# class Solution(object):
#     def checkRecord(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         a_cnt = 0
#         l_cnt = 0
#         flag = False
#         for i in s:
#             if i == 'A':
#                 a_cnt += 1
#                 l_cnt = 0
#             elif i == 'L' and l_cnt < 3:
#                 l_cnt += 1
#                 if l_cnt >= 3:
#                     flag = True
#                     l_cnt = 0
#             else:
#                 l_cnt = 0
#         if a_cnt < 2 and flag == False:
#             return True
#         else:
#             return False

# 如果一个正方形矩阵满足下述全部条件，则称之为一个X矩阵：
# 1.矩阵对角线上的所有元素都不是0
# 2.矩阵中所有其他元素都是0
# 给你一个大小为nxn的二维整数数组grid,表示一个正方形矩阵。如果grid是一个X矩阵，返回true;否则，返回 false。
# grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
#
# flag = True
# for i in range(0, len(grid)):
#     m = len(grid[i])
#     print(grid[i])
#     for j in range(0, len(grid[i])):
#         # print(grid[i][j])
#         if i == j or i == m-j-1:
#             if grid[i][j] == 0:
#                 flag = False
#         else:
#             if grid[i][j] != 0:
#                 flag = False
#
# print(flag)

# 给定两个表示复数的字符串。
# 返回表示它们乘积的字符串。注意，根据定义2=-1。
#   "0+2i" (1+1)*(1+1)=1+12+2*1=2i,你需要将它转换为0+2i的形式。

# n1 = int(num1.split('+')[0])
# n2 = int(num1.split('+')[1].split('i')[0])

# m1 = int(num2.split('+')[0])
# m2 = int(num2.split('+')[1].split('i')[0])


# def split_str(n):
#     temp1 = ''
#     temp2 = ''
#     flag = False
#     for i in range(0, len(n)):
#         if n[i] == '+' or n[i] == '-':
#             flag=True
#             continue
#         if flag:
#             temp1 += n[i]
#         else:
#             temp2 += n[i]
#     return temp1, temp2

# num1 = "1+1i"
# num2 = "1+1i"
#
#
# def split_str(n):
#     temp1 = ''
#     temp2 = ''
#     flag = False
#     # 判断开始是不是'-'
#     if n[0] == '-':
#         start_index = 1
#     else:
#         start_index = 0
#     # 根据符号出现位置拼接str
#     is_add = False
#     for i in range(start_index, len(n)):
#         if n[i] == '+' or n[i] == '-':
#             flag = True
#             if n[i] == '+':
#                 is_add = True
#             if n[i] == '-':
#                 is_add = False
#             continue
#         if flag:
#             temp2 += n[i]
#         else:
#             temp1 += n[i]
#     if start_index == 1:
#         new_temp1 = '-' + temp1
#     else:
#         new_temp1 = temp1
#     if is_add == False:
#         new_temp2 = '-' + temp2
#     else:
#         new_temp2 = temp2
#     return new_temp1, new_temp2
#
#
# t1, t2 = split_str(num1)
# n1, n2 = split_str(num2)
# t2 = t2.split('i')[0]
# n2 = n2.split('i')[0]
# print(t1, t2, n1, n2)
#
# # print(n1, n2, m1, m2)
# x = int(t1) * int(n1) - int(t2) * int(n2)
# y = int(t1) * int(n2) + int(t2) * int(n1)
# if y > 0:
#     res = str(x) + '+' + str(y) + 'i'
# else:
#     res = str(x) + '-' + str(abs(y)) + 'i'
# print(res)
#


# 给你一个整数数组 nums
# 如果一组数字(i,j)满足nums[i]==nums[j]且i<j,就可以认为这是一组好数对。
# 返回好数对的数目。
#
# nums = [1,1,1,1]
# cnt = 0
# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]:
#             cnt+=1
# # print(cnt)
#
# class Solution:
#     def numIdenticalPairs(self, nums):
#         dict_count = {}
#         for i in nums:
#             dict_count[i] = dict_count.get(i, 0) + 1
#         res = 0
#         # 统计每个相同数组 构成好数对的个数
#         for k, v in dict_count.items():
#             # 只有一个构成不了好数对
#             if v <= 1:
#                 continue
#             # 利用排列组合
#             res += (v * (v-1)) // 2
#         return res

# 给你一个正方形矩阵mat，请你返回矩阵对角线元素的和。
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
# mat = [[1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]]
#
# res = 0
# # temp = 0
# # cnt = 0
# for i in range(0, len(mat)):
#     m = len(mat[i])
#     for j in range(0, len(mat[i])):
#         if i == j or i + j + 1 == m:
#             res += mat[i][j]
#         # if (m - 1) / 2 == i and i == j:
#         #     temp += mat[i][j]
#         #     cnt += 1
# # res += temp/cnt
# print(res)


# 给你一个整数数组arr，以及a、b、c三个整数。请你统计其中好三元组的数量。
# 如果三元组 (arr[i],arr[j],arr[k])满足下列全部条件，则认为它是一个好三元组。
#
# arr = [3, 0, 1, 1, 9, 7]
# a = 7
# b = 2
# c = 3
#
# cnt = 0
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if abs(arr[i]-arr[j]) <=a:
#             for k in range(j+1,len(arr)):
#                 if abs(arr[j]-arr[k]) <=b and abs(arr[i]-arr[k]) <= c:
#                     cnt+=1
# print(cnt)

# 给你一个整数数组arr，请你帮忙统计数组中每个数的出现次数。
# 如果每个数的出现次数都是独一无二的，就返回true;否则返回false。
# arr = [1, 2, 2, 1, 1, 3]
# arr_dict = {}
# for i in arr:
#     arr_dict[i] = arr_dict.get(i, 0) + 1
# print(arr_dict)
# arr_list = [i for i in arr_dict.values()]
#
# flag = True
# arr_list.sort(reverse=False)
# print(arr_list)
# for i in range(0, len(arr_list)):
#     if i+1 < len(arr_list) and arr_list[i] == arr_list[i+1]:
#         flag=False
#         break
# print(flag)


# 给你一个整数数组nums (下标从0开始计数)以及两个整数target和start,请你找出一个下标i,满足nums[i]== target且abs(i-start)最小化。
# 注意：abs(x)表示x的绝对值。
# 返abs(i-start)。
# # 题目数据保证target存在于nums中。
#
# nums = [1,1,1,1,1,1,1,1,1,1]
# target = 1
# start = 0
# temp = pow(10, 4) + 10
# for i in range(0, len(nums)):
#     if nums[i] == target:
#         if abs(i - start) < temp:
#             temp = abs(i - start)
#
# print(temp)

# Given two integers num1 and num2 return the sum of the two integers.
# num1 = -10
# num2 = 4
# res = num2+num1
# print(res)

# 给你一个mxn的整数网格accounts,其中accounts[i][j]是第i位客户在第j家银行托管的资产数量。返回最富有客户 所拥有的资产总量。
# 客户的资产总量就是他们在各家银行托管的资产数量之和。最富有客户就是资产总量最大的客户。
# accounts = [[1,2,3],[3,2,1]]
# res = 0
# for i in accounts:
#     temp = 0
#     for j in i:
#         temp+=j
#     if temp > res:
#         res = temp
# print(res)

# 给你一个数组items,其中items[i]=[typei,colori,namei],描述第i件物品的类型、颜色以及名称。
# 另给你一条由两个字符串ruleKey和rulevalue表示的检索规则。
# 如果第1件物品能满足下述条件之一，则认为该物品与给定的检索规则匹配：
# ·ruleKey=="type"且rulevalue=typei。
# ·ruleKey=="color"且rulevalue==colori。
# 、ruleKey="name"且rulevalue==namei。
# 统计并返回匹配检索规则的物品数量。
# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"
# rule_temp = {'type':0,"color":1,'name':2}
# cnt = 0
# for i in items:
#     for j in range(0, len(i)):
#         if j == rule_temp[ruleKey] and i[j]==ruleValue:
#             cnt+=1
# print(cnt)

# 给你一个整数数组nus和一个整数k，请你返回其中出现频率前k高的元素。你可以按任意顺序返回答案。
# nums = [1,1,1,2,2,3]
# k = 2
# temp={}
# res = []
# for i in nums:
#     temp[i] =temp.get(i,0)+1
# tl = list(temp.items())
# tl.sort(key=lambda x:x[1],reverse=True)
# print(tl[0:k])
# for i in tl[0:k]:
#     res.append(i[0])
# print(res)

# # 给定一个24小时制（小时：分钟"HH:MM）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
# def split_time(time):
#     t1 = time.split(':')[0]
#     t2 = time.split(':')[1]
#     t = int(t1) * 60 + int(t2)
#     return t

#
# timePoints = ["23:59", "00:00"]
# timePoints.sort(reverse=False)
# print(timePoints)
# res = pow(10, 4) * 2 + 10
# # temp_time = split_time(timePoints[len(timePoints) - 1]) - split_time('00:00') + split_time('00:00') + split_time(timePoints[0])
# for i in range(0, len(timePoints)):
#     if i + 1 < len(timePoints):
#         temp = abs(split_time(timePoints[i]) - split_time(timePoints[i + 1]))
#         if temp < res:
#             res = temp
# # 这里是计算例如今晚23:59到明早00:00的时间差
# temp_time = split_time('24:00') - split_time(timePoints[len(timePoints) - 1])  + split_time(timePoints[0])
# if temp_time < res:
#     res = temp_time
# print(res)


# 给定一个m×n的矩阵，如果一个元素为0，则将其所在行和列的所有元素都设为0。请使用原地算法。
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# m = len(matrix)
# n = len(matrix[0])
# row = {}  # 标记第i行是否都是0
# col = {}  # 标记第j行是否都是0
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == 0:
#             row[i] = 1  # 如果这个i,j元素是0那么第i行标记一下要清0
#             col[j] = 1  # 如果这个i,j元素是0那么第j列标记一下要清0
#
# for i in range(m):
#     for j in range(n):
#         # 如果这行要被标记了要记为0，就将该元素修改为0
#         if i in row:
#             matrix[i][j] = 0
#         # 如果这列要被标记了要记为0，就将该元素修改为0
#         if j in col:
#             matrix[i][j] = 0
# print(matrix)


#  字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2blc5a3。
#  若"压缩"后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（至z)。

# S = "aaabcccd"
#
# cnt = 1
# new_s = ''
# res = ''
# for i in range(0, len(S)):
#     # if S[i]:
#     #     cnt = 1
#     if i + 1 < len(S) and S[i] == S[i + 1]:
#         cnt += 1
#         new_s = S[i] + str(cnt)
#     else:
#         if cnt == 1:
#             res += S[i]+'1'
#             cnt = 0
#         res += new_s
#         new_s = ''
#         cnt = 1
# print(res)


# nums = [3,2,3]
# temp = len(nums)/2
# nums_dict = {}
# for i in nums:
#     nums_dict[i] = nums_dict.get(i,0)+1
# res = -1
# for i in nums_dict:
#     if nums_dict[i] >= temp:
#         res = i
# print(res)
#


# 给你一个m行n列的二维网格grid和一个整数k。你需要将grid迁移k次。
# 每次「迁移」操作将会引发下述活动：
# ·位于grid[i][j]的元素将会移动到grid[i][j+1]。
# ·位于grid[i][n-1]的元素将会移动到grid[i+1][0]。
# ·位于grid[m-1][n-1]的元素将会移动到grid[0][0]。
# 请你返回k次迁移操作后最终得到的二维网格。
#
#
# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# k = 1
# if k == 0:
#     print(grid)
# while k != 0:
#     new = []
#     m = len(grid)
#     for i in range(m):
#         temp = []
#         n = len(grid[i])
#         for j in range(n):
#             temp.append(0)
#         new.append(temp)
#     for i in range(m):
#         n = len(grid[i])
#         for j in range(n):
#             if i == m - 1 and j == n - 1:
#                 new[0][0] = grid[i][j]
#             if j == n - 1 and i < m - 1:
#                 new[i + 1][0] = grid[i][j]
#             elif j < n - 1:
#                 new[i][j + 1] = grid[i][j]
#     grid = new
#     k = k - 1
# print(new)


# 给你一个大小为rows x cols的矩阵mat,其中mat[i][j]是0或1，请返回矩阵mat中特殊位置的数目。
# 特殊位置定义：如果mat[i][j]=1并且第i行和第j列中的所有其他元素均为0（行和列的下标均从0开始），则位置(i, j)被称为特殊位置。
# mat = [[1, 0, 0],
#        [0, 0, 1],
#        [1, 0, 0]]
#
# cnt = 0
# m = len(mat)
# for i in range(m):
#     n = len(mat[i])
#     for j in range(n):
#         flag = False
#         if mat[i][j] == 1:
#             for k in range(n):
#                 if k == j:
#                     continue
#                 if mat[i][k] == 0:
#                     flag = True
#                 else:
#                     flag = False
#                     break
#             if flag:
#                 for v in range(m):
#                     if v == i:
#                         continue
#                     if mat[v][j] == 0:
#                         flag = True
#                     else:
#                         flag = False
#                         break
#         if flag:
#             cnt += 1
# print(cnt)


# 给你一个*n的矩阵，矩阵中的数字各不相同。请你按任意顺序返回矩阵中的所有幸运数。
# 幸运数是指矩阵中满足同时下列两个条件的元素：
# ·在同一行的所有元素中最小
# ·在同一列的所有元素中最大

# matrix = [[3,7,8],[9,11,13],[15,16,17]]
#
# m = len(matrix)
# res = []
# for i in range(m):
#     n = len(matrix[i])
#     temp_s = matrix[i][0]
#     ts = 0
#     for j in range(1,n):
#         if matrix[i][j] < temp_s:
#             temp_s = matrix[i][j]
#             ts = j
#     temp_l = matrix[0][ts]
#     tl = 0
#     for k in range(1,m):
#         if matrix[k][ts] > temp_l:
#             temp_l = matrix[k][ts]
#     if temp_l == temp_s:
#         res.append(temp_l)
# print(res)

# Alice有n枚糖，其中第i枚糖的类型为candyType[i]。Alice注意到她的体重正在增长，所以前去拜访了一位医生。
# 医生建议Alice要少摄入糖分，只吃掉她所有糖的n/2即可（n是一个偶数)。Alice非常喜欢这些糖，她想要在遵循医生建议的情况 下，尽可能吃到最多不同种类的糖。
# 给你一个长度为n的整数数组candyType，返回：Alice在仅吃掉n/2枚糖的情况下，可以吃到糖的最多种类数。

# candyType = [1,1,2,2,3,3]
# num = len(candyType)/2
# candy_dict = {}
# for i in candyType:
#     candy_dict[i] = candy_dict.get(i,0)+1
# temp = len(candy_dict)
# if num >= temp:
#     print(temp)
# else:
#     print(num)
# print(len(candy_dict),num)

# pwd = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
#         "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# words = ["gin", "zen", "gig", "msg"]
# cnt = 0
# res_list = []
# for i in words:
#     temp = ''
#     for j in i:
#         temp += pwd[ord(j) - ord('a')]
#     res_list.append(temp)
# print(res_list)
# res_dict = {}
# for i in res_list:
#     res_dict[i] = res_dict.get(i,0)+1
# print(len(res_dict))

#
# firstWord = "acb"
# secondWord = "cba"
# targetWord = "cdb"
#
#
# def get_words_num(s):
#     res = ''
#     for i in s:
#         res += str(ord(i) - ord('a'))
#     return int(res)
#
#
# num1 = get_words_num(firstWord)
# num2 = get_words_num(secondWord)
# num3 = get_words_num(targetWord)
# if num1+num2 == num3:
#     print(True)
# else:
#     print(False)
# print(num1,num2)


# 给你一个整数数组arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回true;否则，返回false。

# arr = [2, 6, 4, 1]
# cnt = 0
# for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#         cnt += 1
#     else:
#         cnt = 0
#     if cnt==3:
#         print(True)
#         break
# if cnt==3:
#     print(True)
# else:
#     print(False)


# # 给你一个整数数组nums, 统计并返回在nums中同时至少具有一个严格较小元素和一个严格较大元素的元素数目。
# nums = [11, 7, 2, 2, 15]
# num_dict={}
# for i in nums:
#     num_dict[i] = num_dict.get(i,0)+1
# nl = list(set(num_dict))
# nl.sort(reverse=False)
# print(nl)
# # print(nums)
# cnt = 0
# for i in range(len(nl)):
#     if i + 1 < len(nl) and i - 1 >= 0:
#         if nl[i - 1] < nl[i] < nl[i + 1]:
#             cnt += num_dict[nl[i]]
# print(cnt)


# 给你一个二维整数数组 matrix,返回matrix的转置矩阵。
# # 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
# matrix = [[1,2,3],[4,5,6]]
# new = []
# m = len(matrix)
# n = len(matrix[0])
# for i in range(n):
#     temp=[]
#     for j in range(m):
#         temp.append(0)
#     new.append(temp)
# print(new)
# for i in range(m):
#     print(matrix[i])
#     for j in range(n):
#         new[j][i]=matrix[i][j]
# print(new)
#


# 给你一个字符串text,你需要使用text中的字母来拼凑尽可能多的单词"balloon"（气球)。
# 字符串text中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词"balloon"。

# text = "leetcode"
# def get_dict(s):
#     s_dict = {}
#     for i in s:
#         s_dict[i] = s_dict.get(i,0)+1
#     return s_dict
#
#
# temp = get_dict('balloon')
# t_dict = get_dict(text)
# ls = []
# for k in temp:
#     if k in t_dict:
#          ls.append(int(t_dict[k]/temp[k]))
#     else:
#         ls.append(0)
#         break
# print(min(ls))


# 一个平方和三元组(a,b,c)指的是满足a2+b2=c2的整数三元组a,b和c。
# 给你一个整数n,请你返回满足1<=a,b,c<=n的平方和三元组的数目。


# 3重循环版本
# n = 10
# res = 0
# for a in range(1,n + 1):
#     for b in range(1, n + 1):
#         for c in range(1, n + 1):
#             if a * a + b * b == c * c:
#                 res += 1
# print(res)
#
# # 2重循环版本
# n = 10
# res = 0
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         c = int(math.sqrt(a * a + b * b))
#         if c <= n and c * c == a * a + b * b:
#             res += 1


# 给你一个从0开始的排列nums(下标也从0开始)。请你构建一个同样长度的数组ans，其中，对于每个i（0<=i< nums.length),都满足ans[i]=nums[nums[i]]。返回构建好的数组ans。
# 从0开始的排列nums是一个由0到nums.1 ength-1（0和nums.length-1也包含在内)的不同整数组成的数组。

# nums = [0,2,1,5,3,4]
# ans = [0 for i in range(len(nums))]
# for i in range(len(nums)):
#     ans[i] = nums[nums[i]]
# print(ans)


# 给你一个整数数组nums,其中总是存在唯一的一个最大整数。
# 请你找出数组中的最大元素并检查它是否至少是数组中每个其他数字的两倍。如果是，则返回最大元素的下标，否则返回-1。
# nums = [3, 6, 1, 0]
# res = -1
#
# for i in range(len(nums)):
#     flag = False
#     for j in range(0, len(nums)):
#         if i==j:
#             continue
#         if nums[i] >= nums[j] * 2:
#             flag = True
#         else:
#             flag=False
#             break
#     if flag:
#         res = i
# print(res)

# 对一个大小为nxn的矩阵而言，如果其每一行和每一列都包含从1到n的全部整数（含1和n)，则认为该矩阵是一个有效矩 阵。
# 给你一个大小为nxn的整数矩阵matrix,请你判断矩阵是否为一个有效矩阵：如果是，返回true;否侧，返回false。
# matrix = [[1,1,1],[1,2,3],[1,2,3]]
# class Solution(object):
#     def checkValid(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: bool
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         flag = True
#         for i in range(m):
#             temp = [k for k in range(1, n + 1)]
#             for j in range(n):
#                 if matrix[i][j] not in temp:
#                     flag = False
#                     # print(False)
#                     break
#                 else:
#                     temp.remove(matrix[i][j])
#                     flag = True
#             if not flag:
#                 break
#         for j in range(n):
#             temp = [k for k in range(1, n + 1)]
#             for i in range(m):
#                 if matrix[i][j] not in temp:
#                     flag = False
#                     break
#                 else:
#                     temp.remove(matrix[i][j])
#             if not flag:
#                 break
#         return flag


# # 给定一个整数num，将其转化为7进制，并以字符串形式输出。
# num = 0
# s = []
# flag = True
# if num < 0:
#     flag = False
# num = abs(num)
# while num != 0:
#     s.append(str(num % 7))
#     num = num // 7
# s.reverse()
# res = ''.join(s)
# if flag:
#     print(res)
# else:
#     print('-'+res)


# 给定一个罗马数字，将其转换成整数。
# s = "MCMXCIV"
# roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
# res = 0
# if s in roman_dict:
#     res = roman_dict[s]
# else:
#     i=0
#     while i < len(s):
#         if i+1 < len(s) and s[i]+s[i+1] in roman_dict:
#             res += roman_dict[s[i]+s[i+1]]
#             i+=2
#         elif s[i] in roman_dict:
#             res += roman_dict[s[i]]
#             i+=1
# print(res)

#
# initialEnergy = 5
# initialExperience = 3
# energy = [1, 4, 3, 2]
# experience = [2, 6, 3, 1]
#
# m=0
# cnt = 0
# while m <len(energy):
#     if initialEnergy <= energy[m]:
#         cnt += (energy[m] - initialEnergy)+1
#         initialEnergy += (energy[m]-initialEnergy)+1
#     if initialExperience <= experience[m]:
#         cnt += (experience[m] - initialExperience)+1
#         initialExperience += (experience[m]-initialExperience)+1
#     initialExperience += experience[m]
#     initialEnergy -= energy[m]
#     m += 1
# print(cnt)


# 给你一个整数n,请你判断该整数是否是2的幂次方。如果是，返回true;否则，返回false。
# # 如果存在一个整数x使得n==2x，则测认为n是2的幂次方。
# n = 5
# m=0
# flag = True
# while True:
#     if pow(2, m) == n:
#         break
#     if pow(2, m) > n:
#         flag = False
#         break
#     m += 1
# print(flag)


# 给你一个整数，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
#
# n = 234
# a = 1
# b = 0
# for i in str(n):
#     a *= int(i)
#     b += int(i)
# print(a-b)


# 给你一个由若干0和1组成的字符串s，请你计算并返回将该字符串分割成两个非空子字符串（即左子字符串和右子字符串）所能获 得的最大得分。
# 「分割字符串的得分」为左子字符串中0的数量加上右子字符串中1的数量。
# s = "00111"
#
#
#
# def get_cnt(t):
#     cnt_1 = 0
#     cnt_0 = 0
#     for i in t:
#         if i == '1':
#             cnt_1 += 1
#         else:
#             cnt_0 += 1
#     return cnt_0, cnt_1
#
#
# res = 0
# i = 0
# while i < len(s)-1:
#     a = s[0:i+1]
#     b = s[i+1:]
#     temp_a_0, temp_a_1 = get_cnt(a)
#     temp_b_0, temp_b_1 = get_cnt(b)
#     if res < temp_a_0 + temp_b_1:
#         res = temp_a_0 + temp_b_1
#     i += 1
# print(res)


# 给你一个整数数组nums(下标从0开始)。每一次操作中，你可以选择数组中一个元素，并将它增加1。
# ·比方说，如果nums=[l,2,3],你可以选择增加nums[1]得到nums=[1,3,3]。
# 请你返回使nums严格递增的最少操作次数。
# 我们称数组nums是严格递增的，当它满足对于所有的0<=i<nums.length-1都有nums[i]<nums[i+l]。一个长度 为1的数组是严格递增的一种特殊情况。
# nums = [1,5,2,4,1]
# cnt = 0
# if len(nums) > 1:
#     for i in range(len(nums)):
#         if i+1 < len(nums):
#             while nums[i] >= nums[i+1]:
#                 nums[i+1] += 1
#                 cnt+=1
# print(nums)
# print(cnt)
#
# nums = [1, 5, 2, 4, 1]
# cnt = 0
# if len(nums) > 1:
#     for i in range(len(nums)):
#         if i+1 < len(nums):
#             if nums[i] >= nums[i+1]:
#                 cnt += nums[i] - nums[i + 1] + 1
#                 nums[i+1] += nums[i]-nums[i+1] + 1
# print(nums)
# print(cnt)


# 给你两个非负整数num1和num2。
# 每一步操作中，如果num1>=num2,你必须用numl减num2;否则，你必须用num2减num1。
# ·例如，num1=5且num2=4,应该用numl减num2,因此，得到num1=1和num2=4。然而，如果num1= 4且num2=5,一步操作后，得到num1=4和num2=1。
# 返回使numl=0或num2=0的操作数。

# num1 = 10
# num2 = 10
# cnt = 0
# while True:
#     if num1 == 0 or num2 == 0:
#         break
#     if num1 >= num2:
#         num1 -= num2
#         cnt += 1
#     else:
#         num2 -= num1
#         cnt += 1
# print(cnt)


# 给你一个长度为n的整数数组nums，请你返回nums中最接近0的数字。如果有多个答案，请你返回它们中的最大值。

# nums = [1, -2, 1]
# num = pow(10, 5) + 10
# res = 0
# for i in nums:
#     if abs(i) < num:
#         num = abs(i)
#         res = i
#     if abs(i) == num:
#         if res < i:
#             res = i
# print(res)


# 符合下列属性的数组arr称为山脉数组：
# ·arr.length>=3
# ·存在i(0<i<arr.length-1)使得：
# o arr[0]arr[1]<..arr[i-1]<arr[i]
# o arr[i]arr[i+1]>..arr[arr.length -1]
# 给你由整数组成的山脉数组arr,返回任何满足arr[0]<arr[1]<·.·arr[i-1]<arr[i]>arr[i+1]>···> arr[arr.length-1]的下标i。

# arr = [3,4,5,1]
#
# res = 0
# for i in range(len(arr)):
#     if i+1 < len(arr) and i-1 >= 0:
#         if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
#             res = i
#             break
# print(res)


# # 给你一个非负整数nu，请你返回将它变成0所需要的步数。如果当前数字是偶数，你需要把它除以2；否则，减去1。
# num = 14
# cnt = 0
# while num > 0:
#     if num % 2 == 0:
#         num = num / 2
#         cnt += 1
#     else:
#         num -= 1
#         cnt += 1
# print(cnt)


# 给你一个m*n的矩阵grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。请你统计并返回grid中负数的数目。
# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# cnt = 0
# for i in grid:
#     for j in i:
#         if j < 0:
#             cnt+=1
# print(cnt)


# 斐波那契数列，首位是0，第二位是1，第三位是1....第n位是x, 第n+1位是 y, 第n+2位是 x+ y
# fb = []
# # 数组第一位是0
# fb.append(0)
# # 数组第二为是1
# fb.append(1)
# # 于是根据斐波那契的性质我们可以计算出第三位是第0项加第一项
# c = fb[0] + fb[1]
# fb.append(c)
# # 第四位就是第1项加第二项
# d = fb[1] + fb[2]
# fb.append(d)
# print(fb)

# # 写成循环的形式就是
# fb = []
# # 数组第一位是0
# fb.append(0)
# # 数组第二为是1
# fb.append(1)
# # 计算第2项到第99项的斐波那契数列,只素以从第2项开始是以为你第1项和第0项已经计算过了
# for i in range(2, 100):
#     temp = fb[i - 1] + fb[i - 2]
#     fb.append(temp)
# print(fb)

# 假设你正在爬楼梯。需要n「 阶你才能到达楼顶。
# 每次你可以爬1或2个台阶。你有多少种不同的方法可以爬到楼顶呢？
# fb = []
# n = 2
# for i in range(2, n):
#     temp = fb[i - 1] + fb[i - 2]
#     fb.append(temp)
# print(fb)


# 给定一个数组prices,它的第i个元素prices[i]表示一支给定股票第i天的价格。
# 你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回0。
# prices = [7,6,4,3,1]
# res = 0
# for i in range(len(prices)):
#     for j in range(i, len(prices)):
#         if prices[j] > prices[i]:
#             if prices[j]-prices[i] > res:
#                 res = prices[j]-prices[i]
# print(res)
# prices = [7,1,5,3,6,4]
# res = 0
# buy = min(prices)
# buy_index = prices.index(buy)
# # print(buy_index)
#
# if buy_index+1 >= len(prices):
#     print(0)
# else:
#     for i in range(buy_index+1, len(prices)):
#         if prices[i] - buy > res:
#             res = prices[i] - buy
# print(res)


# prices = [7,1,5,3,6,4]
# res = 0
# buy = pow(10, 5)+10
# buy_index = 0
# sell_index = pow(10, 4)
# for i in range(len(prices)):
#     if prices[i] < buy:
#         buy = prices[i]
#         buy_index = i
#     if prices[i]-buy > res:
#         res = prices[i]-buy
# print(res)


# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：
# 你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？
# nums = [4,1,2,1,2]
# nums.sort()
# print(nums)
# for i in range(len(nums)):
#     if i+1<len(nums) and i-1 >= 0:
#         if i == len(nums)-1:
#             if nums[i-1] != nums[i]:
#                 print(nums[i])
#         elif nums[i-1] != nums[i] and nums[i] != nums[i+1]:
#             print(nums[i - 1])
#


# 编写一个算法来判断一个数n是不是快乐数。 9.03
# 「快乐数」定义为：
# ·对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# ·然后重复这个过程直到这个数变为1，也可能是无限循环但始终变不到1。
# ·如果这个过程结果为1，那么这个数就是快乐数。
# 如果n是快乐数就返回true;不是，则返回false。
# class Solution(object):
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         temp = str(n)
#         cnt = 0
#         while temp !='1':
#             res = 0
#             for i in temp:
#                 res += pow(int(i),2)
#                 temp = str(res)
#             cnt+=1
#             if cnt ==1000:
#                 break
#         if int(temp) == 1:
#             return True
#         else:
#             return False


# 给你一个有效的IPv4地址address,返回这个IP地址的无效化版本。
# 所谓无效化P地址，其实就是用"[.]"代替了每个"."。

# address = "1.1.1.1"
# res=''
# for i in address:
#     if i == '.':
#         res += '[.]'
#     else:
#         res += i
# print(res)


# 给你一个长度为n的整数数组nums。请你构建一个长度为2n的答案数组ans，数组下标从0开始计数，对于所有0<=i< n的i,满足下述所有要求：
# ·ans[i]==nums[i]
# ans[i+n]=nums[i]
# 具体而言，ans由两个nums数组串联形成。
# 返回数组ans。
#
# nums = [1, 2, 1]
# # ans = nums*2
# # print(ans)
# n = 2
# ans = []
# while n != 0:
#     for i in nums:
#         ans.append(i)
#     n -= 1
# print(ans)


# 给定一个无重复元素的有序整数数组nums。
# 返回恰好覆盖数组中所有数字的最小有序区间范围列表。也就是说，nus的每个元素都恰好被某个区间范围所覆盖，并且不存在属于 某个范围但不属于nums的数字x。
# 列表中的每个区间范围[a,b]应该按如下格式输出：
# 。"a->b",如果a!=b
# 。"a",如果a=b
#
# nums = [0,2,3,4,6,8,9]
#
# ans = []
# start = ''
# end = ''
# for i in range(len(nums)):
#     if i+1 < len(nums):
#         if nums[i]+1 == nums[i+1]:
#             if start != "":
#                 continue
#             else:
#                 start = str(nums[i])
#         else:
#             end = str(nums[i])
#             if start != "":
#                 ans.append(start + "->" + end)
#                 start = ""
#             else:
#                 ans.append(end)
#     else:
#         if start == '':
#             ans.append(str(nums[i]))
#         else:
#             ans.append(start + '->' + str(nums[i]))
#
# print(ans)


# 给定一个非负整数numRows,生成「杨辉三角」的前 numRows行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

# numRows = 5
# res = []
# i = 0
# for i in range(numRows):
#     # 初始化temp
#     temp = [1]*(i+1)
#     # 从第三行开始
#     if i >= 2:
#         # 两边的还是1
#         for j in range(1, i):
#             temp[j] = t[j-1]+t[j]
#     res.append(temp)
#     t = temp
# # print(res)
# #
# res = []
# for i in range(numRows):
#     temp = []
#     for j in range(0, i + 1):
#         if j == 0 or j == i:
#             temp.append(1)
#         else:
#             temp.append(res[i - 1][j] + res[i - 1][j - 1])
#     res.append(temp)
# print(res)

# class Solution:
#     def generate(self, numRows):
#         res = []
#         i = 0
#         # 初始化res如下
#         # [0]
#         # [0,0]
#         # [0,0,0]
#         while i < numRows:
#             temp = []
#             j = 0
#             while j <= i:
#                 temp.append(0)
#                 j = j + 1
#             i = i + 1
#             res.append(temp)
#         # 第一个肯定是1最顶上的
#         res[0][0] = 1
#         # 第0行肯定是1，所以从第一行开始求，根据上一行
#         i = 1
#         # 开始从第一个开始递推公式 res[i][j] = res[i-1][j-1] + res[i-1][j] 要满足i-1 j-1 j不越界，越界的情况下另外一个直接+0即可
#         while i < numRows:
#             j = 0
#             while j <= i:
#                 # 正常的
#                 if i - 1 >= 0 and j - 1 >= 0 and j < i:
#                     print(i, j)
#                     res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
#                     j = j + 1
#                     continue
#                 # 左边越界，左边+0
#                 if j - 1 < 0 and j < i:
#                     res[i][j] = 0 + res[i - 1][j]
#                     j = j + 1
#                     continue
#                 # 剩下的都是右边越界，右边+0
#                 res[i][j] = res[i - 1][j - 1] + 0
#                 j = j + 1
#             i = i + 1
#         return res
#
# print(Solution().generate(5))


# 给定一种规律pattern和一个字符串s，判断s是否遵循相同的规律。
# 这里的遵循指完全匹配，例如，pattern里的每个字母和字符串s中的每个非空单词之间存在着双向连接的对应规律。
# pattern = "abba"
# s = "dog cat cat dog"
#
# class Solution(object):
#     def create_temp(self,a):
#         s = ''
#         cnt = 0
#         dict_s = {}
#         for i in a:
#             if i in dict_s:
#                 now_cnt = dict_s[i]
#             else:
#                 now_cnt = cnt + 1
#                 cnt = cnt + 1
#                 dict_s[i] = now_cnt
#             s += str(now_cnt)
#             # print('{}第几次出现的{}'.format(i, now_cnt))
#         return s
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#         sl = s.split(' ')
#         if len(pattern)!= len(sl):
#             return False
#         else:
#             pattern_s = self.create_temp(pattern)
#             ss = self.create_temp(sl)
#             if pattern_s==ss:
#                 return True
#             else:
#                 return False


# # 整数转换成罗马数字
#
#
# roman_dict = { 1:'I', 4: 'IV',5:  'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90:'XC', 100:'C', 400: 'CD', 500: 'D',
#               900: 'CM', 1000: 'M'}
#
# roman_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# num = 719
#
# res = ''
#
# while num > 0:
#     if num in roman_list:
#         if num in roman_dict:
#             res += roman_dict[num]
#             break
#     else:
#         i = 0
#         while i < len(roman_list):
#             if num >= roman_list[i]:
#                 num -= roman_list[i]
#                 res += roman_dict[roman_list[i]]
#                 i += 1
#             else:
#                 i += 1
# print(res)


# 编写一个高效的算法来判断×n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# ·每行中的整数从左到右按升序排列。
# ·每行的第一个整数大于前一行的最后一个整数。
#
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
#
# m = len(matrix)
# n = len(matrix[0])
# flag = False
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == target:
#             flag = True
#             break
# print(flag)


# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如， waterbottle是erbottlewat旋转后的字 符串)。
#
# s1 = "waterbottle"
# s2 = "erbottlewat"
#
# if len(s1) != len(s2):
#     print(False)
# else:
#     i = 0
#     flag = False
#     while i < len(s1):
#         new_s1 = ''
#         print(s1[i:], s1[:i])
#         new_s1 += s1[i:] + s1[:i]
#         if new_s1 == s2:
#             flag = True
#             break
#         i += 1
#
#     print(new_s1)
#     print(flag)


# 给你-个数组nums,数组中有2n个元素，按[x1,x2,.·,xny1,y2,.·,yn]的格式排列。
# 请你将数组按[x1,y1,x2,Y2,·.·,n,Yn]格式重新排列，返回重排后的数组。

# nums = [2,5,1,3,4,7]
# n = 3
# n1 = nums[:n]
# n2 = nums[n:]
# res = []
# i = 0
# while i < n:
#     res.append(n1[i])
#     res.append(n2[i])
#     i+=1
# print(res)

# 给你一个下标从0开始的整数数组nus，判断是否存在两个长度为2的子数组且它们的和相等。注意，这两个子数组起始位置的下 标必须不相同。
# 如果这样的子数组存在，请返回true, 否则返回fa1se。
# 子数组是一个数组中一段连续非空的元素组成的序列。

# nums = [4, 2, 4]
# m = len(nums)
# temp = {}
# flag = False
# for i in range(m):
#     if i+1 < len(nums):
#         if nums[i]+nums[i+1] not in temp:
#             temp[nums[i]+nums[i+1]] = 1
#         else:
#             flag = True
#             break
# print(flag)


# 给你一个下标从0开始长度为n的整数数组nums和一个整数k,请你返回满足0<=i<j<n,nums[i]==nums[j]
# 且(i*j)能被k整除的数对(i,j)的数目。
#
# nums = [3, 1, 2, 2, 2, 1, 3]
# k = 2

# for i in n# -*- coding: utf-8 -*-
# 001
# nums = [3,2,3]
# n = len(nums)/3
# res_dict={}
# res = []
# for i in nums:
#     res_dict[i] = res_dict.get(i,0)+1
# for k in res_dict:
#     if res_dict[k] > n and k not in res:
#         res.append(k)
# print(res)

# res = []
# for i in nums:
#     if nums.count(i) > n and i not in res:
#         res.append(i)
# print(res)


# for i in range(len(nums)):
#     flag = False
#     if i+1 < len(nums) and nums[i+1] == nums[i]:
#         count += 1
#         flag = True
#     else:
#         continue
#     if flag:
#         print(count)


# 002
# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用补码运算方法。 2022.07.31
# 注意：
# 1.十六进制中所有字母(a-f)都必须是小写。
# 2.十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中 的第一个字符将不会是0字符。
# 2022.07.3
# 3.给定的数确保在32位有符号整数范围内。
# 4.不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

# num = 26
# print(hex(num))
# temp={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
# num_list = []
# while num != 0:
#     if num % 16 in temp:
#         num_list.append(temp[num % 16])
#     else:
#         num_list.append(str(num % 16))
#     num = num // 16
# num_list.reverse()
# print(num_list)
# print(''.join(num_list))

# # 负数转正数处理
# if num < 0:
#     num = 2 ** 32 + num
# # a = hex(num)
# # 去掉0x
# # print(a[2:])


# 给定一个二进制数组 nums ,计算其中最大连续1的个数。
# nums = [0, 0]
# res = []
# count = 1
# for i in range(0, len(nums)):
#     if i+1 < len(nums) and nums[i+1] == nums[i] and nums[i]==1:
#         count += 1
#     else:
#         if nums[i] == 1:
#             res.append(count)
#             count = 1
# if len(res)==0:
#     print(0)
# print(max(res))


# 给你一个数组rr,请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用-1替换。
# 完成所有替换操作后，请你返回这个数组。
# arr = [17, 18, 5, 4, 6, 1]
#
# ans = []
# for i in range(0, len(arr)):
#     ans.append(-1)
# for i in range(len(arr) - 2, -1, -1):
#     # ans[i]数组其实表示的第i位后面数字的最大值，那么我们计算ans[i] ，只要判断ans[i+1]（第i+1位后面的最大值）和arr[i + 1]的（和第i+1位的值）
#     print(i)
#     ans[i] = max(ans[i+1], arr[i + 1])
#     print('+++'+str(ans[i]))
# print(ans)


# new_arr = []
# for i in range(0, len(arr)-1):
#     new_arr.append(max(arr[i+1:]))
# new_arr.append(-1)
# print(new_arr)


# for i in range(0, len(arr)):
#     temp = 0
#     flag = False
#     for j in range(i+1, len(arr)):
#         if j != len(arr):
#             if arr[j] > temp:
#                 temp = arr[j]
#     if temp !=0:
#         new_arr.append(temp)
# new_arr.append(-1)
# print(new_arr)
# temp = 0
# for j in range(1, len(arr)):
#     if j != len(arr):
#         if arr[j] > temp:
#             temp = arr[j]
#             flag = True
#         else:
#             new_arr.append(temp)
#             temp = 0
#     else:
#         new_arr.append(-1)
# print(new_arr)


# 给你两个字符串数组words1和words2，请你返回在两个字符串数组中都恰好出现一次的字符串的数目。
# words1 = ["leetcode","is","amazing","as","is"]
# words2 = ["amazing","leetcode","is"]
#
# def mad_dict(words):
#     dict = {}
#     for i in words:
#         dict[i] = dict.get(i, 0)+1
#     return dict
#
# w1 = mad_dict(words1)
# w2 = mad_dict(words2)
# count = 0
# for k in w1:
#     if w1[k] == 1:
#         if k in w2 and w2[k] == 1:
#             print(k)
#             count +=1
#         else:
#             continue
#     else:
#         continue
# print(count)


# 给你一个整数数组digits，其中每个元素是一个数字（0-9)。数组中可能存在重复元素。
# 你需要找出所有满足下述条件且互不相同的整数：
# ·该整数由digits中的三个元素按任意顺序依次连接组成。
# ·该整数不含前导零
# ·该整数是一个偶数
#
# 例如，给定的digits是[1,2,3]，整数132和312满足上面列出的全部条件。
# 将找出的所有互不相同的整数按递增顺序排列，并以数组形式返回。

# digits = [2, 1, 3, 0]
# res_temp = {}
# res = []
#
# for i in digits:
#     res_temp[i] = res_temp.get(i, 0)+1
#
# for i in range(100, 999):
#     temp_dict = {}
#     one = i//100
#     two = i//10 % 10
#     three = i % 10
#     temp_dict[one] = temp_dict.get(one, 0) + 1
#     temp_dict[two] = temp_dict.get(two, 0) + 1
#     temp_dict[three] = temp_dict.get(three, 0) + 1
#     flag = False
#     for k in temp_dict:
#         if k in res_temp and temp_dict[k] <= res_temp[k]:
#             flag = True
#         else:
#             flag = False
#             break
#     if flag and i%2 == 0:
#         res.append(i)
# print(res)

# for i in range(0, len(digits)):
#     for j in range(0, len(digits)):
#
#         k = 0
#         while k < len(digits):
#             s = ''
#             if digits[i] != digits[j] and digits[j] != digits[k] and digits[i] != digits[k]:
#                 s += str(digits[i])+str(digits[j])+str(digits[k])
#             k += 1
#             if len(s) == 3:
#                 if s[0] != '0' and int(s) % 2 == 0 and s not in res:
#                     print(s)
#                     res_temp[int(s)] = res_temp.get(int(s), 0)+1
#                 else:
#                     continue
# for k in res_temp:
#     if res_temp[k] == 1:
#         res.append(k)
# res.sort(reverse=False)
# print(res)

# 编写一个算法来判断一个数n是不是快乐数。
# 「快乐数」定义为：
# ·对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# ·然后重复这个过程直到这个数变为1，也可能是无限循环但始终变不到1。
# # ·如果这个过程结果为1，那么这个数就是快乐数。
# # 如果n是快乐数就返回true;不是，则返回false。
# def isHappy(n):
#     """
#     :type n: int
#     :rtype: bool
#     """
#     cnt = 0
#     while int(n) > 1:
#         a = str(n)
#         n = 0
#         for i in a:
#             n += int(i) * int(i)
#         cnt += 1
#         if cnt > 1000:
#             return False
#     if int(n) == 1:
#         return True
#     else:
#         return False


# 给定整数n，返回所有小于非负整数n的质数的数量。
#
# def countPrimes(n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     visit = []
#     for i in range(0, n):
#         visit.append(True)
#     for i in range(2, n):
#         if visit[i]:
#             j = i + i
#             while j < n:
#                 visit[j] = False
#                 j += i
#     ans = 0
#     for i in range(2, n):
#         if (visit[i]):
#             ans += 1
#     return ans
#
#
# ans = countPrimes(n=10)
# print(ans)

# if n == 0:
#     print(0)
# for m in range(2, n):
#     flag = True
#     for i in range(2, m):
#         if m % i == 0:
#             flag = False
#             break
#     if flag:
#         cnt += 1
# print(cnt)


# 给你一个长度为n的整数数组nums，请你返回nums中最接近0的数字。如果有多个答案，请你返回它们中的最大值。
# def findClosestNumber(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     temp = pow(10, 5) + 10
#     res = 0
#     for i in nums:
#         if abs(i) < temp:
#             temp = abs(i)
#             res = i
#         elif abs(i) == temp:
#             if res < i:
#                 res = i
#             else:
#                 continue
#         else:
#             continue
#     return res


# 给你一个整数，请你每隔三位添加点（即""符号）作为千位分隔符，并将结果以字符串格式返回。
# n = 1234
# n = str(n)
# s = []
# if len(n) <= 3:
#     print(n)
# else:
#     cnt = 0
#     for i in range(len(n)-1, -1, -1):
#         # print(i)
#         s.append(n[i])
#         cnt += 1
#         print(s)
#         if cnt % 3 == 0 and i != len(n)-1:
#             s.append('.')
#     s.reverse()
#     print(''.join(s))


# n = str(n)
#
# s = ''
# if len(n) <= 3:
#     print(n)
# else:
#     for i in range(0, len(n)):
#         # print(i)
#         if i % 3 == 0 and i != len(n)-1:
#             s = s + n[i]
#             s += '.'
#         else:
#             s = s + n[i]
#     print(s)


# 给你一个仅由数字6和9组成的正整数 num
# 你最多只能翻转一位数字，将6变成9，或者把9变成6。
# 请返回你可以得到的最大数字。
#
# num = 9999
# temp = 0
# if num > int(temp):
#     new = ''
#     flag = False
#     for i in str(num):
#         if i == '6' and flag == False:
#             new += '9'
#             flag = True
#             continue
#         new += i
#     temp = int(new)
# print(temp)

# 给你两个二进制字符串，返回它们的和（用二进制表示)。
# 输入为非空字符串且只包含数字1和0。 1011 = 1 * 2 ^3 + 0 * 2 ^2 + 1 * 2  ^ 1 + 1 * 2 ^ 0
# a = "11"
# b = "1"
#
#
# def two_to_ten(s):
#     new_s = 0
#     temp = 0
#     for i in range(len(s) - 1, -1, -1):
#         print(i, s[i])
#         new_s += int(s[i]) * pow(2, temp)
#         temp += 1
#     return new_s
#
#
# new_a = two_to_ten(a)
# new_b = two_to_ten(b)
# res = new_a + new_b
# res_list = []
# while res != 0:
#     res_list.append(str(res % 2))
#     res = res // 2
# res_list.reverse()
# print(''.join(res_list))

# print(new_a,new_b,bin(res))


# 给你两个字符串：ransomNote和magazine,判断ransomNote能不能由magazine里面的字符构成。
# 如果可以，返回true;否则返回false。
# magazine中的每个字符只能在ransomNote中使用一次。
# ransomNote = "aa"
# magazine = "aab"
#
# ransomNote_dict = {}
# magazine_dict = {}
# for i in ransomNote:
#     ransomNote_dict[i] = ransomNote_dict.get(i,0)+1
# for i in magazine:
#     magazine_dict[i] = magazine_dict.get(i,0)+1
# if len(magazine) <= pow(10,5)+10:
#     flag = False
#     for k in magazine_dict:
#         if k in ransomNote_dict and magazine_dict[k] == ransomNote_dict[k]:
#             flag = True
#     if flag:
#         print(True)
#     else:
#         print(False)
# else:
#     print(True)

# 给你一个字符串s和一个字符letter,返回在s中等于letter字符所占的百分比，向下取整到最接近的百分比。
import math

# s = "foobar"
# letter = "o"
# l = len(s)
# s_dict={}
# for i in s:
#     s_dict[i] = s_dict.get(i,0)+1
# print(s_dict)
# res = 0
# for i in s_dict:
#     if letter == i:
#         res = round(s_dict[i]/l * 100)
# print(res)
#
# colors =[1,8,3,8,3]
# cnt = 1
# cnt_list = []
# temp = 0
# for i in range(0, len(colors)):
#     for j in range(i+1, len(colors)):
#         # print(colors[i])
#         if colors[i] == colors[j]:
#             cnt += 1
#         else:
#             if abs(i-j) > temp:
#                 temp = abs(i-j)
#             cnt = 0
# print(temp)

# 给你两个非负整数1ow和high。请你返回1ow和high之间（包括二者)奇数的数目。
# low = 3
# high = 7
# for i in range(low,high+1):
#     if i%2!=0:
#         print(i)

# 给你两个字符串数组word1和word2。如果两个数组表示的字符串相同，返回true;否则，返回false。
# 数组表示的字符串是由数组中的所有元素按顺序连接形成的字符串。
# word1 = ["ab", "c"]
# word2 = ["a", "bc"]
#
# def become_str(word):
#     s = ''
#     for i in word:
#         if 1 <= len(i)<=pow(10,3):
#             s += i
#     return s
#
#
# if 1<=len(word1)<=pow(10,3) and 1<=len(word2)<=pow(10,3):
#     s1 = become_str(word1)
#     s2 = become_str(word2)
#     if 1 <= len(s1) <= pow(10, 3) and 1 <= len(s2) <= pow(10, 3):
#         if s1 == s2:
#             print(True)
#         else:
#             print(False)
#     else:
#         print(False)
# else:
#     print(False)


# 给你一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。

#
# class Solution(object):
#     def find_third(self, l):
#         temp = []
#         t = max(l)
#         for i in l:
#             if i != t:
#                 temp.append(i)
#         return temp
#
#     def thirdMax(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         temp1 = self.find_third(nums)
#         res_list = self.find_third(temp1)
#         return max(res_list)
#
#
# nums = [2, 2, 3, 1]
# print(Solution().thirdMax(nums))


# 给你一个字符串s表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字 符：
# 。'A':Absent,缺勤 。'工'：Late,迟到
# ·'p':Present,到场

# 如果学生能够同时满足下面两个条件，则可以获得出勤奖励：
# 。按总出勤计，学生缺勤（'A')严格少于两天。
# ·学生不会存在连续3天或连续3天以上的迟到（'工')记录。
# # 如果学生可以获得出勤奖励，返回true;否则，返回false。
# class Solution(object):
#     def checkRecord(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         a_cnt = 0
#         l_cnt = 0
#         flag = False
#         for i in s:
#             if i == 'A':
#                 a_cnt += 1
#                 l_cnt = 0
#             elif i == 'L' and l_cnt < 3:
#                 l_cnt += 1
#                 if l_cnt >= 3:
#                     flag = True
#                     l_cnt = 0
#             else:
#                 l_cnt = 0
#         if a_cnt < 2 and flag == False:
#             return True
#         else:
#             return False

# 如果一个正方形矩阵满足下述全部条件，则称之为一个X矩阵：
# 1.矩阵对角线上的所有元素都不是0
# 2.矩阵中所有其他元素都是0
# 给你一个大小为nxn的二维整数数组grid,表示一个正方形矩阵。如果grid是一个X矩阵，返回true;否则，返回 false。
# grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
#
# flag = True
# for i in range(0, len(grid)):
#     m = len(grid[i])
#     print(grid[i])
#     for j in range(0, len(grid[i])):
#         # print(grid[i][j])
#         if i == j or i == m-j-1:
#             if grid[i][j] == 0:
#                 flag = False
#         else:
#             if grid[i][j] != 0:
#                 flag = False
#
# print(flag)

# 给定两个表示复数的字符串。
# 返回表示它们乘积的字符串。注意，根据定义2=-1。
#   "0+2i" (1+1)*(1+1)=1+12+2*1=2i,你需要将它转换为0+2i的形式。

# n1 = int(num1.split('+')[0])
# n2 = int(num1.split('+')[1].split('i')[0])

# m1 = int(num2.split('+')[0])
# m2 = int(num2.split('+')[1].split('i')[0])


# def split_str(n):
#     temp1 = ''
#     temp2 = ''
#     flag = False
#     for i in range(0, len(n)):
#         if n[i] == '+' or n[i] == '-':
#             flag=True
#             continue
#         if flag:
#             temp1 += n[i]
#         else:
#             temp2 += n[i]
#     return temp1, temp2

# num1 = "1+1i"
# num2 = "1+1i"
#
#
# def split_str(n):
#     temp1 = ''
#     temp2 = ''
#     flag = False
#     # 判断开始是不是'-'
#     if n[0] == '-':
#         start_index = 1
#     else:
#         start_index = 0
#     # 根据符号出现位置拼接str
#     is_add = False
#     for i in range(start_index, len(n)):
#         if n[i] == '+' or n[i] == '-':
#             flag = True
#             if n[i] == '+':
#                 is_add = True
#             if n[i] == '-':
#                 is_add = False
#             continue
#         if flag:
#             temp2 += n[i]
#         else:
#             temp1 += n[i]
#     if start_index == 1:
#         new_temp1 = '-' + temp1
#     else:
#         new_temp1 = temp1
#     if is_add == False:
#         new_temp2 = '-' + temp2
#     else:
#         new_temp2 = temp2
#     return new_temp1, new_temp2
#
#
# t1, t2 = split_str(num1)
# n1, n2 = split_str(num2)
# t2 = t2.split('i')[0]
# n2 = n2.split('i')[0]
# print(t1, t2, n1, n2)
#
# # print(n1, n2, m1, m2)
# x = int(t1) * int(n1) - int(t2) * int(n2)
# y = int(t1) * int(n2) + int(t2) * int(n1)
# if y > 0:
#     res = str(x) + '+' + str(y) + 'i'
# else:
#     res = str(x) + '-' + str(abs(y)) + 'i'
# print(res)
#


# 给你一个整数数组 nums
# 如果一组数字(i,j)满足nums[i]==nums[j]且i<j,就可以认为这是一组好数对。
# 返回好数对的数目。
#
# nums = [1,1,1,1]
# cnt = 0
# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] == nums[j]:
#             cnt+=1
# # print(cnt)
#
# class Solution:
#     def numIdenticalPairs(self, nums):
#         dict_count = {}
#         for i in nums:
#             dict_count[i] = dict_count.get(i, 0) + 1
#         res = 0
#         # 统计每个相同数组 构成好数对的个数
#         for k, v in dict_count.items():
#             # 只有一个构成不了好数对
#             if v <= 1:
#                 continue
#             # 利用排列组合
#             res += (v * (v-1)) // 2
#         return res

# 给你一个正方形矩阵mat，请你返回矩阵对角线元素的和。
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。
# mat = [[1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1],
#        [1, 1, 1, 1]]
#
# res = 0
# # temp = 0
# # cnt = 0
# for i in range(0, len(mat)):
#     m = len(mat[i])
#     for j in range(0, len(mat[i])):
#         if i == j or i + j + 1 == m:
#             res += mat[i][j]
#         # if (m - 1) / 2 == i and i == j:
#         #     temp += mat[i][j]
#         #     cnt += 1
# # res += temp/cnt
# print(res)


# 给你一个整数数组arr，以及a、b、c三个整数。请你统计其中好三元组的数量。
# 如果三元组 (arr[i],arr[j],arr[k])满足下列全部条件，则认为它是一个好三元组。
#
# arr = [3, 0, 1, 1, 9, 7]
# a = 7
# b = 2
# c = 3
#
# cnt = 0
# for i in range(0,len(arr)):
#     for j in range(i+1,len(arr)):
#         if abs(arr[i]-arr[j]) <=a:
#             for k in range(j+1,len(arr)):
#                 if abs(arr[j]-arr[k]) <=b and abs(arr[i]-arr[k]) <= c:
#                     cnt+=1
# print(cnt)

# 给你一个整数数组arr，请你帮忙统计数组中每个数的出现次数。
# 如果每个数的出现次数都是独一无二的，就返回true;否则返回false。
# arr = [1, 2, 2, 1, 1, 3]
# arr_dict = {}
# for i in arr:
#     arr_dict[i] = arr_dict.get(i, 0) + 1
# print(arr_dict)
# arr_list = [i for i in arr_dict.values()]
#
# flag = True
# arr_list.sort(reverse=False)
# print(arr_list)
# for i in range(0, len(arr_list)):
#     if i+1 < len(arr_list) and arr_list[i] == arr_list[i+1]:
#         flag=False
#         break
# print(flag)


# 给你一个整数数组nums (下标从0开始计数)以及两个整数target和start,请你找出一个下标i,满足nums[i]== target且abs(i-start)最小化。
# 注意：abs(x)表示x的绝对值。
# 返abs(i-start)。
# # 题目数据保证target存在于nums中。
#
# nums = [1,1,1,1,1,1,1,1,1,1]
# target = 1
# start = 0
# temp = pow(10, 4) + 10
# for i in range(0, len(nums)):
#     if nums[i] == target:
#         if abs(i - start) < temp:
#             temp = abs(i - start)
#
# print(temp)

# Given two integers num1 and num2 return the sum of the two integers.
# num1 = -10
# num2 = 4
# res = num2+num1
# print(res)

# 给你一个mxn的整数网格accounts,其中accounts[i][j]是第i位客户在第j家银行托管的资产数量。返回最富有客户 所拥有的资产总量。
# 客户的资产总量就是他们在各家银行托管的资产数量之和。最富有客户就是资产总量最大的客户。
# accounts = [[1,2,3],[3,2,1]]
# res = 0
# for i in accounts:
#     temp = 0
#     for j in i:
#         temp+=j
#     if temp > res:
#         res = temp
# print(res)

# 给你一个数组items,其中items[i]=[typei,colori,namei],描述第i件物品的类型、颜色以及名称。
# 另给你一条由两个字符串ruleKey和rulevalue表示的检索规则。
# 如果第1件物品能满足下述条件之一，则认为该物品与给定的检索规则匹配：
# ·ruleKey=="type"且rulevalue=typei。
# ·ruleKey=="color"且rulevalue==colori。
# 、ruleKey="name"且rulevalue==namei。
# 统计并返回匹配检索规则的物品数量。
# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
# ruleKey = "color"
# ruleValue = "silver"
# rule_temp = {'type':0,"color":1,'name':2}
# cnt = 0
# for i in items:
#     for j in range(0, len(i)):
#         if j == rule_temp[ruleKey] and i[j]==ruleValue:
#             cnt+=1
# print(cnt)

# 给你一个整数数组nus和一个整数k，请你返回其中出现频率前k高的元素。你可以按任意顺序返回答案。
# nums = [1,1,1,2,2,3]
# k = 2
# temp={}
# res = []
# for i in nums:
#     temp[i] =temp.get(i,0)+1
# tl = list(temp.items())
# tl.sort(key=lambda x:x[1],reverse=True)
# print(tl[0:k])
# for i in tl[0:k]:
#     res.append(i[0])
# print(res)

# # 给定一个24小时制（小时：分钟"HH:MM）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。
# def split_time(time):
#     t1 = time.split(':')[0]
#     t2 = time.split(':')[1]
#     t = int(t1) * 60 + int(t2)
#     return t

#
# timePoints = ["23:59", "00:00"]
# timePoints.sort(reverse=False)
# print(timePoints)
# res = pow(10, 4) * 2 + 10
# # temp_time = split_time(timePoints[len(timePoints) - 1]) - split_time('00:00') + split_time('00:00') + split_time(timePoints[0])
# for i in range(0, len(timePoints)):
#     if i + 1 < len(timePoints):
#         temp = abs(split_time(timePoints[i]) - split_time(timePoints[i + 1]))
#         if temp < res:
#             res = temp
# # 这里是计算例如今晚23:59到明早00:00的时间差
# temp_time = split_time('24:00') - split_time(timePoints[len(timePoints) - 1])  + split_time(timePoints[0])
# if temp_time < res:
#     res = temp_time
# print(res)


# 给定一个m×n的矩阵，如果一个元素为0，则将其所在行和列的所有元素都设为0。请使用原地算法。
# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# m = len(matrix)
# n = len(matrix[0])
# row = {}  # 标记第i行是否都是0
# col = {}  # 标记第j行是否都是0
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == 0:
#             row[i] = 1  # 如果这个i,j元素是0那么第i行标记一下要清0
#             col[j] = 1  # 如果这个i,j元素是0那么第j列标记一下要清0
#
# for i in range(m):
#     for j in range(n):
#         # 如果这行要被标记了要记为0，就将该元素修改为0
#         if i in row:
#             matrix[i][j] = 0
#         # 如果这列要被标记了要记为0，就将该元素修改为0
#         if j in col:
#             matrix[i][j] = 0
# print(matrix)


#  字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串aabcccccaaa会变为a2blc5a3。
#  若"压缩"后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（至z)。

# S = "aaabcccd"
#
# cnt = 1
# new_s = ''
# res = ''
# for i in range(0, len(S)):
#     # if S[i]:
#     #     cnt = 1
#     if i + 1 < len(S) and S[i] == S[i + 1]:
#         cnt += 1
#         new_s = S[i] + str(cnt)
#     else:
#         if cnt == 1:
#             res += S[i]+'1'
#             cnt = 0
#         res += new_s
#         new_s = ''
#         cnt = 1
# print(res)


# nums = [3,2,3]
# temp = len(nums)/2
# nums_dict = {}
# for i in nums:
#     nums_dict[i] = nums_dict.get(i,0)+1
# res = -1
# for i in nums_dict:
#     if nums_dict[i] >= temp:
#         res = i
# print(res)
#


# 给你一个m行n列的二维网格grid和一个整数k。你需要将grid迁移k次。
# 每次「迁移」操作将会引发下述活动：
# ·位于grid[i][j]的元素将会移动到grid[i][j+1]。
# ·位于grid[i][n-1]的元素将会移动到grid[i+1][0]。
# ·位于grid[m-1][n-1]的元素将会移动到grid[0][0]。
# 请你返回k次迁移操作后最终得到的二维网格。
#
#
# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# k = 1
# if k == 0:
#     print(grid)
# while k != 0:
#     new = []
#     m = len(grid)
#     for i in range(m):
#         temp = []
#         n = len(grid[i])
#         for j in range(n):
#             temp.append(0)
#         new.append(temp)
#     for i in range(m):
#         n = len(grid[i])
#         for j in range(n):
#             if i == m - 1 and j == n - 1:
#                 new[0][0] = grid[i][j]
#             if j == n - 1 and i < m - 1:
#                 new[i + 1][0] = grid[i][j]
#             elif j < n - 1:
#                 new[i][j + 1] = grid[i][j]
#     grid = new
#     k = k - 1
# print(new)


# 给你一个大小为rows x cols的矩阵mat,其中mat[i][j]是0或1，请返回矩阵mat中特殊位置的数目。
# 特殊位置定义：如果mat[i][j]=1并且第i行和第j列中的所有其他元素均为0（行和列的下标均从0开始），则位置(i, j)被称为特殊位置。
# mat = [[1, 0, 0],
#        [0, 0, 1],
#        [1, 0, 0]]
#
# cnt = 0
# m = len(mat)
# for i in range(m):
#     n = len(mat[i])
#     for j in range(n):
#         flag = False
#         if mat[i][j] == 1:
#             for k in range(n):
#                 if k == j:
#                     continue
#                 if mat[i][k] == 0:
#                     flag = True
#                 else:
#                     flag = False
#                     break
#             if flag:
#                 for v in range(m):
#                     if v == i:
#                         continue
#                     if mat[v][j] == 0:
#                         flag = True
#                     else:
#                         flag = False
#                         break
#         if flag:
#             cnt += 1
# print(cnt)


# 给你一个*n的矩阵，矩阵中的数字各不相同。请你按任意顺序返回矩阵中的所有幸运数。
# 幸运数是指矩阵中满足同时下列两个条件的元素：
# ·在同一行的所有元素中最小
# ·在同一列的所有元素中最大

# matrix = [[3,7,8],[9,11,13],[15,16,17]]
#
# m = len(matrix)
# res = []
# for i in range(m):
#     n = len(matrix[i])
#     temp_s = matrix[i][0]
#     ts = 0
#     for j in range(1,n):
#         if matrix[i][j] < temp_s:
#             temp_s = matrix[i][j]
#             ts = j
#     temp_l = matrix[0][ts]
#     tl = 0
#     for k in range(1,m):
#         if matrix[k][ts] > temp_l:
#             temp_l = matrix[k][ts]
#     if temp_l == temp_s:
#         res.append(temp_l)
# print(res)

# Alice有n枚糖，其中第i枚糖的类型为candyType[i]。Alice注意到她的体重正在增长，所以前去拜访了一位医生。
# 医生建议Alice要少摄入糖分，只吃掉她所有糖的n/2即可（n是一个偶数)。Alice非常喜欢这些糖，她想要在遵循医生建议的情况 下，尽可能吃到最多不同种类的糖。
# 给你一个长度为n的整数数组candyType，返回：Alice在仅吃掉n/2枚糖的情况下，可以吃到糖的最多种类数。

# candyType = [1,1,2,2,3,3]
# num = len(candyType)/2
# candy_dict = {}
# for i in candyType:
#     candy_dict[i] = candy_dict.get(i,0)+1
# temp = len(candy_dict)
# if num >= temp:
#     print(temp)
# else:
#     print(num)
# print(len(candy_dict),num)

# pwd = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
#         "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
# words = ["gin", "zen", "gig", "msg"]
# cnt = 0
# res_list = []
# for i in words:
#     temp = ''
#     for j in i:
#         temp += pwd[ord(j) - ord('a')]
#     res_list.append(temp)
# print(res_list)
# res_dict = {}
# for i in res_list:
#     res_dict[i] = res_dict.get(i,0)+1
# print(len(res_dict))

#
# firstWord = "acb"
# secondWord = "cba"
# targetWord = "cdb"
#
#
# def get_words_num(s):
#     res = ''
#     for i in s:
#         res += str(ord(i) - ord('a'))
#     return int(res)
#
#
# num1 = get_words_num(firstWord)
# num2 = get_words_num(secondWord)
# num3 = get_words_num(targetWord)
# if num1+num2 == num3:
#     print(True)
# else:
#     print(False)
# print(num1,num2)


# 给你一个整数数组arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回true;否则，返回false。

# arr = [2, 6, 4, 1]
# cnt = 0
# for i in range(len(arr)):
#     if arr[i] % 2 != 0:
#         cnt += 1
#     else:
#         cnt = 0
#     if cnt==3:
#         print(True)
#         break
# if cnt==3:
#     print(True)
# else:
#     print(False)


# # 给你一个整数数组nums, 统计并返回在nums中同时至少具有一个严格较小元素和一个严格较大元素的元素数目。
# nums = [11, 7, 2, 2, 15]
# num_dict={}
# for i in nums:
#     num_dict[i] = num_dict.get(i,0)+1
# nl = list(set(num_dict))
# nl.sort(reverse=False)
# print(nl)
# # print(nums)
# cnt = 0
# for i in range(len(nl)):
#     if i + 1 < len(nl) and i - 1 >= 0:
#         if nl[i - 1] < nl[i] < nl[i + 1]:
#             cnt += num_dict[nl[i]]
# print(cnt)


# 给你一个二维整数数组 matrix,返回matrix的转置矩阵。
# # 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。
# matrix = [[1,2,3],[4,5,6]]
# new = []
# m = len(matrix)
# n = len(matrix[0])
# for i in range(n):
#     temp=[]
#     for j in range(m):
#         temp.append(0)
#     new.append(temp)
# print(new)
# for i in range(m):
#     print(matrix[i])
#     for j in range(n):
#         new[j][i]=matrix[i][j]
# print(new)
#


# 给你一个字符串text,你需要使用text中的字母来拼凑尽可能多的单词"balloon"（气球)。
# 字符串text中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词"balloon"。

# text = "leetcode"
# def get_dict(s):
#     s_dict = {}
#     for i in s:
#         s_dict[i] = s_dict.get(i,0)+1
#     return s_dict
#
#
# temp = get_dict('balloon')
# t_dict = get_dict(text)
# ls = []
# for k in temp:
#     if k in t_dict:
#          ls.append(int(t_dict[k]/temp[k]))
#     else:
#         ls.append(0)
#         break
# print(min(ls))


# 一个平方和三元组(a,b,c)指的是满足a2+b2=c2的整数三元组a,b和c。
# 给你一个整数n,请你返回满足1<=a,b,c<=n的平方和三元组的数目。


# 3重循环版本
# n = 10
# res = 0
# for a in range(1,n + 1):
#     for b in range(1, n + 1):
#         for c in range(1, n + 1):
#             if a * a + b * b == c * c:
#                 res += 1
# print(res)
#
# # 2重循环版本
# n = 10
# res = 0
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         c = int(math.sqrt(a * a + b * b))
#         if c <= n and c * c == a * a + b * b:
#             res += 1


# 给你一个从0开始的排列nums(下标也从0开始)。请你构建一个同样长度的数组ans，其中，对于每个i（0<=i< nums.length),都满足ans[i]=nums[nums[i]]。返回构建好的数组ans。
# 从0开始的排列nums是一个由0到nums.1 ength-1（0和nums.length-1也包含在内)的不同整数组成的数组。

# nums = [0,2,1,5,3,4]
# ans = [0 for i in range(len(nums))]
# for i in range(len(nums)):
#     ans[i] = nums[nums[i]]
# print(ans)


# 给你一个整数数组nums,其中总是存在唯一的一个最大整数。
# 请你找出数组中的最大元素并检查它是否至少是数组中每个其他数字的两倍。如果是，则返回最大元素的下标，否则返回-1。
# nums = [3, 6, 1, 0]
# res = -1
#
# for i in range(len(nums)):
#     flag = False
#     for j in range(0, len(nums)):
#         if i==j:
#             continue
#         if nums[i] >= nums[j] * 2:
#             flag = True
#         else:
#             flag=False
#             break
#     if flag:
#         res = i
# print(res)

# 对一个大小为nxn的矩阵而言，如果其每一行和每一列都包含从1到n的全部整数（含1和n)，则认为该矩阵是一个有效矩 阵。
# 给你一个大小为nxn的整数矩阵matrix,请你判断矩阵是否为一个有效矩阵：如果是，返回true;否侧，返回false。
# matrix = [[1,1,1],[1,2,3],[1,2,3]]
# class Solution(object):
#     def checkValid(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: bool
#         """
#         m = len(matrix)
#         n = len(matrix[0])
#         flag = True
#         for i in range(m):
#             temp = [k for k in range(1, n + 1)]
#             for j in range(n):
#                 if matrix[i][j] not in temp:
#                     flag = False
#                     # print(False)
#                     break
#                 else:
#                     temp.remove(matrix[i][j])
#                     flag = True
#             if not flag:
#                 break
#         for j in range(n):
#             temp = [k for k in range(1, n + 1)]
#             for i in range(m):
#                 if matrix[i][j] not in temp:
#                     flag = False
#                     break
#                 else:
#                     temp.remove(matrix[i][j])
#             if not flag:
#                 break
#         return flag


# # 给定一个整数num，将其转化为7进制，并以字符串形式输出。
# num = 0
# s = []
# flag = True
# if num < 0:
#     flag = False
# num = abs(num)
# while num != 0:
#     s.append(str(num % 7))
#     num = num // 7
# s.reverse()
# res = ''.join(s)
# if flag:
#     print(res)
# else:
#     print('-'+res)


# 给定一个罗马数字，将其转换成整数。
# s = "MCMXCIV"
# roman_dict = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
# res = 0
# if s in roman_dict:
#     res = roman_dict[s]
# else:
#     i=0
#     while i < len(s):
#         if i+1 < len(s) and s[i]+s[i+1] in roman_dict:
#             res += roman_dict[s[i]+s[i+1]]
#             i+=2
#         elif s[i] in roman_dict:
#             res += roman_dict[s[i]]
#             i+=1
# print(res)

#
# initialEnergy = 5
# initialExperience = 3
# energy = [1, 4, 3, 2]
# experience = [2, 6, 3, 1]
#
# m=0
# cnt = 0
# while m <len(energy):
#     if initialEnergy <= energy[m]:
#         cnt += (energy[m] - initialEnergy)+1
#         initialEnergy += (energy[m]-initialEnergy)+1
#     if initialExperience <= experience[m]:
#         cnt += (experience[m] - initialExperience)+1
#         initialExperience += (experience[m]-initialExperience)+1
#     initialExperience += experience[m]
#     initialEnergy -= energy[m]
#     m += 1
# print(cnt)


# 给你一个整数n,请你判断该整数是否是2的幂次方。如果是，返回true;否则，返回false。
# # 如果存在一个整数x使得n==2x，则测认为n是2的幂次方。
# n = 5
# m=0
# flag = True
# while True:
#     if pow(2, m) == n:
#         break
#     if pow(2, m) > n:
#         flag = False
#         break
#     m += 1
# print(flag)


# 给你一个整数，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
#
# n = 234
# a = 1
# b = 0
# for i in str(n):
#     a *= int(i)
#     b += int(i)
# print(a-b)


# 给你一个由若干0和1组成的字符串s，请你计算并返回将该字符串分割成两个非空子字符串（即左子字符串和右子字符串）所能获 得的最大得分。
# 「分割字符串的得分」为左子字符串中0的数量加上右子字符串中1的数量。
# s = "00111"
#
#
#
# def get_cnt(t):
#     cnt_1 = 0
#     cnt_0 = 0
#     for i in t:
#         if i == '1':
#             cnt_1 += 1
#         else:
#             cnt_0 += 1
#     return cnt_0, cnt_1
#
#
# res = 0
# i = 0
# while i < len(s)-1:
#     a = s[0:i+1]
#     b = s[i+1:]
#     temp_a_0, temp_a_1 = get_cnt(a)
#     temp_b_0, temp_b_1 = get_cnt(b)
#     if res < temp_a_0 + temp_b_1:
#         res = temp_a_0 + temp_b_1
#     i += 1
# print(res)


# 给你一个整数数组nums(下标从0开始)。每一次操作中，你可以选择数组中一个元素，并将它增加1。
# ·比方说，如果nums=[l,2,3],你可以选择增加nums[1]得到nums=[1,3,3]。
# 请你返回使nums严格递增的最少操作次数。
# 我们称数组nums是严格递增的，当它满足对于所有的0<=i<nums.length-1都有nums[i]<nums[i+l]。一个长度 为1的数组是严格递增的一种特殊情况。
# nums = [1,5,2,4,1]
# cnt = 0
# if len(nums) > 1:
#     for i in range(len(nums)):
#         if i+1 < len(nums):
#             while nums[i] >= nums[i+1]:
#                 nums[i+1] += 1
#                 cnt+=1
# print(nums)
# print(cnt)
#
# nums = [1, 5, 2, 4, 1]
# cnt = 0
# if len(nums) > 1:
#     for i in range(len(nums)):
#         if i+1 < len(nums):
#             if nums[i] >= nums[i+1]:
#                 cnt += nums[i] - nums[i + 1] + 1
#                 nums[i+1] += nums[i]-nums[i+1] + 1
# print(nums)
# print(cnt)


# 给你两个非负整数num1和num2。
# 每一步操作中，如果num1>=num2,你必须用numl减num2;否则，你必须用num2减num1。
# ·例如，num1=5且num2=4,应该用numl减num2,因此，得到num1=1和num2=4。然而，如果num1= 4且num2=5,一步操作后，得到num1=4和num2=1。
# 返回使numl=0或num2=0的操作数。

# num1 = 10
# num2 = 10
# cnt = 0
# while True:
#     if num1 == 0 or num2 == 0:
#         break
#     if num1 >= num2:
#         num1 -= num2
#         cnt += 1
#     else:
#         num2 -= num1
#         cnt += 1
# print(cnt)


# 给你一个长度为n的整数数组nums，请你返回nums中最接近0的数字。如果有多个答案，请你返回它们中的最大值。

# nums = [1, -2, 1]
# num = pow(10, 5) + 10
# res = 0
# for i in nums:
#     if abs(i) < num:
#         num = abs(i)
#         res = i
#     if abs(i) == num:
#         if res < i:
#             res = i
# print(res)


# 符合下列属性的数组arr称为山脉数组：
# ·arr.length>=3
# ·存在i(0<i<arr.length-1)使得：
# o arr[0]arr[1]<..arr[i-1]<arr[i]
# o arr[i]arr[i+1]>..arr[arr.length -1]
# 给你由整数组成的山脉数组arr,返回任何满足arr[0]<arr[1]<·.·arr[i-1]<arr[i]>arr[i+1]>···> arr[arr.length-1]的下标i。

# arr = [3,4,5,1]
#
# res = 0
# for i in range(len(arr)):
#     if i+1 < len(arr) and i-1 >= 0:
#         if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
#             res = i
#             break
# print(res)


# # 给你一个非负整数nu，请你返回将它变成0所需要的步数。如果当前数字是偶数，你需要把它除以2；否则，减去1。
# num = 14
# cnt = 0
# while num > 0:
#     if num % 2 == 0:
#         num = num / 2
#         cnt += 1
#     else:
#         num -= 1
#         cnt += 1
# print(cnt)


# 给你一个m*n的矩阵grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。请你统计并返回grid中负数的数目。
# grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# cnt = 0
# for i in grid:
#     for j in i:
#         if j < 0:
#             cnt+=1
# print(cnt)


# 斐波那契数列，首位是0，第二位是1，第三位是1....第n位是x, 第n+1位是 y, 第n+2位是 x+ y
# fb = []
# # 数组第一位是0
# fb.append(0)
# # 数组第二为是1
# fb.append(1)
# # 于是根据斐波那契的性质我们可以计算出第三位是第0项加第一项
# c = fb[0] + fb[1]
# fb.append(c)
# # 第四位就是第1项加第二项
# d = fb[1] + fb[2]
# fb.append(d)
# print(fb)

# # 写成循环的形式就是
# fb = []
# # 数组第一位是0
# fb.append(0)
# # 数组第二为是1
# fb.append(1)
# # 计算第2项到第99项的斐波那契数列,只素以从第2项开始是以为你第1项和第0项已经计算过了
# for i in range(2, 100):
#     temp = fb[i - 1] + fb[i - 2]
#     fb.append(temp)
# print(fb)

# 假设你正在爬楼梯。需要n「 阶你才能到达楼顶。
# 每次你可以爬1或2个台阶。你有多少种不同的方法可以爬到楼顶呢？
# fb = []
# n = 2
# for i in range(2, n):
#     temp = fb[i - 1] + fb[i - 2]
#     fb.append(temp)
# print(fb)


# 给定一个数组prices,它的第i个元素prices[i]表示一支给定股票第i天的价格。
# 你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回0。
# prices = [7,6,4,3,1]
# res = 0
# for i in range(len(prices)):
#     for j in range(i, len(prices)):
#         if prices[j] > prices[i]:
#             if prices[j]-prices[i] > res:
#                 res = prices[j]-prices[i]
# print(res)
# prices = [7,1,5,3,6,4]
# res = 0
# buy = min(prices)
# buy_index = prices.index(buy)
# # print(buy_index)
#
# if buy_index+1 >= len(prices):
#     print(0)
# else:
#     for i in range(buy_index+1, len(prices)):
#         if prices[i] - buy > res:
#             res = prices[i] - buy
# print(res)


# prices = [7,1,5,3,6,4]
# res = 0
# buy = pow(10, 5)+10
# buy_index = 0
# sell_index = pow(10, 4)
# for i in range(len(prices)):
#     if prices[i] < buy:
#         buy = prices[i]
#         buy_index = i
#     if prices[i]-buy > res:
#         res = prices[i]-buy
# print(res)


# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 说明：
# 你的算法应该具有线性时间复杂度。你可以不使用额外空间来实现吗？
# nums = [4,1,2,1,2]
# nums.sort()
# print(nums)
# for i in range(len(nums)):
#     if i+1<len(nums) and i-1 >= 0:
#         if i == len(nums)-1:
#             if nums[i-1] != nums[i]:
#                 print(nums[i])
#         elif nums[i-1] != nums[i] and nums[i] != nums[i+1]:
#             print(nums[i - 1])
#


# 编写一个算法来判断一个数n是不是快乐数。 9.03
# 「快乐数」定义为：
# ·对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# ·然后重复这个过程直到这个数变为1，也可能是无限循环但始终变不到1。
# ·如果这个过程结果为1，那么这个数就是快乐数。
# 如果n是快乐数就返回true;不是，则返回false。
# class Solution(object):
#     def isHappy(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         temp = str(n)
#         cnt = 0
#         while temp !='1':
#             res = 0
#             for i in temp:
#                 res += pow(int(i),2)
#                 temp = str(res)
#             cnt+=1
#             if cnt ==1000:
#                 break
#         if int(temp) == 1:
#             return True
#         else:
#             return False


# 给你一个有效的IPv4地址address,返回这个IP地址的无效化版本。
# 所谓无效化P地址，其实就是用"[.]"代替了每个"."。

# address = "1.1.1.1"
# res=''
# for i in address:
#     if i == '.':
#         res += '[.]'
#     else:
#         res += i
# print(res)


# 给你一个长度为n的整数数组nums。请你构建一个长度为2n的答案数组ans，数组下标从0开始计数，对于所有0<=i< n的i,满足下述所有要求：
# ·ans[i]==nums[i]
# ans[i+n]=nums[i]
# 具体而言，ans由两个nums数组串联形成。
# 返回数组ans。
#
# nums = [1, 2, 1]
# # ans = nums*2
# # print(ans)
# n = 2
# ans = []
# while n != 0:
#     for i in nums:
#         ans.append(i)
#     n -= 1
# print(ans)


# 给定一个无重复元素的有序整数数组nums。
# 返回恰好覆盖数组中所有数字的最小有序区间范围列表。也就是说，nus的每个元素都恰好被某个区间范围所覆盖，并且不存在属于 某个范围但不属于nums的数字x。
# 列表中的每个区间范围[a,b]应该按如下格式输出：
# 。"a->b",如果a!=b
# 。"a",如果a=b
#
# nums = [0,2,3,4,6,8,9]
#
# ans = []
# start = ''
# end = ''
# for i in range(len(nums)):
#     if i+1 < len(nums):
#         if nums[i]+1 == nums[i+1]:
#             if start != "":
#                 continue
#             else:
#                 start = str(nums[i])
#         else:
#             end = str(nums[i])
#             if start != "":
#                 ans.append(start + "->" + end)
#                 start = ""
#             else:
#                 ans.append(end)
#     else:
#         if start == '':
#             ans.append(str(nums[i]))
#         else:
#             ans.append(start + '->' + str(nums[i]))
#
# print(ans)


# 给定一个非负整数numRows,生成「杨辉三角」的前 numRows行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

# numRows = 5
# res = []
# i = 0
# for i in range(numRows):
#     # 初始化temp
#     temp = [1]*(i+1)
#     # 从第三行开始
#     if i >= 2:
#         # 两边的还是1
#         for j in range(1, i):
#             temp[j] = t[j-1]+t[j]
#     res.append(temp)
#     t = temp
# # print(res)
# #
# res = []
# for i in range(numRows):
#     temp = []
#     for j in range(0, i + 1):
#         if j == 0 or j == i:
#             temp.append(1)
#         else:
#             temp.append(res[i - 1][j] + res[i - 1][j - 1])
#     res.append(temp)
# print(res)

# class Solution:
#     def generate(self, numRows):
#         res = []
#         i = 0
#         # 初始化res如下
#         # [0]
#         # [0,0]
#         # [0,0,0]
#         while i < numRows:
#             temp = []
#             j = 0
#             while j <= i:
#                 temp.append(0)
#                 j = j + 1
#             i = i + 1
#             res.append(temp)
#         # 第一个肯定是1最顶上的
#         res[0][0] = 1
#         # 第0行肯定是1，所以从第一行开始求，根据上一行
#         i = 1
#         # 开始从第一个开始递推公式 res[i][j] = res[i-1][j-1] + res[i-1][j] 要满足i-1 j-1 j不越界，越界的情况下另外一个直接+0即可
#         while i < numRows:
#             j = 0
#             while j <= i:
#                 # 正常的
#                 if i - 1 >= 0 and j - 1 >= 0 and j < i:
#                     print(i, j)
#                     res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
#                     j = j + 1
#                     continue
#                 # 左边越界，左边+0
#                 if j - 1 < 0 and j < i:
#                     res[i][j] = 0 + res[i - 1][j]
#                     j = j + 1
#                     continue
#                 # 剩下的都是右边越界，右边+0
#                 res[i][j] = res[i - 1][j - 1] + 0
#                 j = j + 1
#             i = i + 1
#         return res
#
# print(Solution().generate(5))


# 给定一种规律pattern和一个字符串s，判断s是否遵循相同的规律。
# 这里的遵循指完全匹配，例如，pattern里的每个字母和字符串s中的每个非空单词之间存在着双向连接的对应规律。
# pattern = "abba"
# s = "dog cat cat dog"
#
# class Solution(object):
#     def create_temp(self,a):
#         s = ''
#         cnt = 0
#         dict_s = {}
#         for i in a:
#             if i in dict_s:
#                 now_cnt = dict_s[i]
#             else:
#                 now_cnt = cnt + 1
#                 cnt = cnt + 1
#                 dict_s[i] = now_cnt
#             s += str(now_cnt)
#             # print('{}第几次出现的{}'.format(i, now_cnt))
#         return s
#     def wordPattern(self, pattern, s):
#         """
#         :type pattern: str
#         :type s: str
#         :rtype: bool
#         """
#         sl = s.split(' ')
#         if len(pattern)!= len(sl):
#             return False
#         else:
#             pattern_s = self.create_temp(pattern)
#             ss = self.create_temp(sl)
#             if pattern_s==ss:
#                 return True
#             else:
#                 return False


# # 整数转换成罗马数字
#
#
# roman_dict = { 1:'I', 4: 'IV',5:  'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90:'XC', 100:'C', 400: 'CD', 500: 'D',
#               900: 'CM', 1000: 'M'}
#
# roman_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
# num = 719
#
# res = ''
#
# while num > 0:
#     if num in roman_list:
#         if num in roman_dict:
#             res += roman_dict[num]
#             break
#     else:
#         i = 0
#         while i < len(roman_list):
#             if num >= roman_list[i]:
#                 num -= roman_list[i]
#                 res += roman_dict[roman_list[i]]
#                 i += 1
#             else:
#                 i += 1
# print(res)


# 编写一个高效的算法来判断×n矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# ·每行中的整数从左到右按升序排列。
# ·每行的第一个整数大于前一行的最后一个整数。
#
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
#
# m = len(matrix)
# n = len(matrix[0])
# flag = False
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == target:
#             flag = True
#             break
# print(flag)


# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如， waterbottle是erbottlewat旋转后的字 符串)。
#
# s1 = "waterbottle"
# s2 = "erbottlewat"
#
# if len(s1) != len(s2):
#     print(False)
# else:
#     i = 0
#     flag = False
#     while i < len(s1):
#         new_s1 = ''
#         print(s1[i:], s1[:i])
#         new_s1 += s1[i:] + s1[:i]
#         if new_s1 == s2:
#             flag = True
#             break
#         i += 1
#
#     print(new_s1)
#     print(flag)


# 给你-个数组nums,数组中有2n个元素，按[x1,x2,.·,xny1,y2,.·,yn]的格式排列。
# 请你将数组按[x1,y1,x2,Y2,·.·,n,Yn]格式重新排列，返回重排后的数组。

# nums = [2,5,1,3,4,7]
# n = 3
# n1 = nums[:n]
# n2 = nums[n:]
# res = []
# i = 0
# while i < n:
#     res.append(n1[i])
#     res.append(n2[i])
#     i+=1
# print(res)

# 给你一个下标从0开始的整数数组nus，判断是否存在两个长度为2的子数组且它们的和相等。注意，这两个子数组起始位置的下 标必须不相同。
# 如果这样的子数组存在，请返回true, 否则返回fa1se。
# 子数组是一个数组中一段连续非空的元素组成的序列。

# nums = [4, 2, 4]
# m = len(nums)
# temp = {}
# flag = False
# for i in range(m):
#     if i+1 < len(nums):
#         if nums[i]+nums[i+1] not in temp:
#             temp[nums[i]+nums[i+1]] = 1
#         else:
#             flag = True
#             break
# print(flag)


# 给你一个下标从0开始长度为n的整数数组nums和一个整数k,请你返回满足0<=i<j<n,nums[i]==nums[j]
# 且(i*j)能被k整除的数对(i,j)的数目。
#
# nums = [3, 1, 2, 2, 2, 1, 3]
# k = 2
# n = len(nums)
# cnt = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if nums[i] == nums[j]:
#             if i * j % k == 0:
#                 cnt += 1
# print(cnt)


# 给你一个数组nums。数组「动态和」的计算公式为：runningSum[i]=sum(nums[0]nums[i])
# 请返回nums的动态和。

# nums = [1, 2, 3, 4]
# res = []
# temp = 0
# for i in range(len(nums)):
#     temp += nums[i]
#     res.append(temp)
# # i = len(nums)-1
# # while i !=0:
# #     temp += nums[i]
# #     res.append(temp)
# #     i -= 1
# print(res)


# 给你一个整数数组nus，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#
# temp = 0
# i = len(nums) - 1
# res = 0
# flag = False
# while i >= 0:
#     if temp + nums[i] < 0:
#         temp = 0
#     else:
#         flag = True
#         temp += nums[i]
#         if res < temp:
#             res = temp
#     i -= 1
# if flag:
#     print(res)
# else:
#     print(max(nums))


# 给你一个正整数num, 请你统计并返回小于或等于num 且各位数字之和为偶数的正整数的数目。
# 正整数的各位数字之和是其所有位上的对应数字相加的结果。
#
# num = 30
# i = 1
# cnt = 0
# while i <= num:
#     if len(str(i)) <= 1:
#         if i % 2 == 0:
#             cnt += 1
#     elif 1 < len(str(i)) <= 2:
#         if (i//10 + i % 10) % 2 == 0:
#             cnt += 1
#     elif 2 < len(str(i)) <= 3:
#         if (i//100 + i//10 + i % 10) % 2 == 0:
#             cnt += 1
#     else:
#         if (i//1000 + i//100 + i//10 + i % 10) % 2 == 0:
#             cnt += 1
#     i += 1
# print(cnt)


# 给你一个整数数组nums，返回出现最频繁的偶数元素。
# 如果存在多个满足条件的元素，只需要返回最小的一个。如果不存在这样的元素，返回-1。
#
# nums = [0, 1, 2, 2, 4, 4, 1]
#
# cnt = {}
# res = -1
# flag = False
# for i in nums:
#     if i % 2 == 0:
#         flag = True
#         if i not in cnt:
#             cnt[i] = 1
#         else:
#             cnt[i] += 1
# if not flag:
#     print(-1)
# else:
#     print(cnt)
#     res_ls = []
#     temp = 0
#     for i in cnt:
#         if temp < cnt[i]:
#             temp = cnt[i]
#             res = i
#         if temp == cnt[i]:
#             if res > i:
#                 res = i
#     print(res)


# 给你两个按非递减顺序排列的整数数组nums1和nums2，另有两个整数m和n，分别表示nums1和nums2中的元素数目。
# 请你合并nums2到nums1中，使合并后的数组同样按非递减顺序排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组nums1中。为了应对这种情况，nums1的初始长度为m+n,其中前m 个元素表示应合并的元素，后n个元素为0，应忽略。nums2的长度为n。
# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1
# i = 0
#
# if m == 0:
#     while i < n:
#         nums1[i] = nums2[i]
#         i += 1
# if n != 0:
#     while i < n:
#         nums1[m+i] = nums2[i]
#         i += 1
# nums1.sort()
# print(nums1)


# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个回文串
# 字母和数字都属于字母数字字符。
# 给你一个字符串s,如果它是回文串，返回true;否则，返回false。

# s = " "

# # 处理字符串
# temp = ''
# for i in s:
#     if ord('z') >= ord(i) >= ord('a'):
#         temp += i
#     elif ord('Z') >= ord(i) >= ord('A'):
#         temp += chr(ord(i)+32)
#     elif ord('9') >= ord(i) >= ord('0'):
#         temp += i
#     else:
#         continue
#
# new_s = temp[::-1]
# print(temp)
# print(new_s)
#
# if new_s == temp:
#     print(True)
# else:
#     print(False)


# 如果一个整数n在b进制下（b为2到n-2之间的所有整数)对应的字符串全部都是回文的，那么我们称这个数n是严格 回文的。
# 给你一个整数n,如果n是严格回文的，请返回true,否则返回false。
# 如果一个字符串从前往后读和从后往前读完全相同，那么这个字符串是回文的。
# n = 9
#
# i = 2
# res = []
# flag = False
# while i <= n-2:
#     temp = []
#     num = n
#     while num != 0:
#         temp.append(str(num % i))
#         num = num // i
#     temp.reverse()
#     temp_res = ''.join(temp)
#     if temp_res != temp_res[::-1]:
#         flag = False
#         break
#     else:
#         flag = True
#     i += 1
# if flag:
#     print(True)
# else:
#     print(False)


# 给你一个字符串s，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。
#
# s = "Hello"
# res = ''
# for i in s:
#     if ord('Z') >= ord(i) >= ord('A'):
#         res += chr(ord(i)+32)
#     else:
#         res+=i
#
# print(res)

#
# # 指定年份year和月份month,返回该月天数。
# year = 1992
# month = 7
# big = [1,3,5,7,8,10,12]
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     if month == 2:
#         print(29)
#     elif month in big:
#         print(31)
#     else:
#         print(30)
# else:
#     if month == 2:
#         print(28)
#     elif month in big:
#         print(31)
#     else:
#         print(30)


# 给你一个整数n，对于0<=i<=n中的每个i，计算其二进制表示中1的个数，返回一个长度为n+1的数组ans作为答 案。
#
# n = 2
#
# i = 1
# res = [0]
# while i <= n:
#     num = i
#     temp = []
#     while num != 0:
#         temp.append(str(num % 2))
#         num = num//2
#     temp.reverse()
#     temp_res = ''.join(temp)
#     cnt = 0
#     for j in temp_res:
#         if j == '1':
#             cnt += 1
#     res.append(cnt)
#     i += 1
# print(res)


# 给你一个下标从0开始的整数数组nums，返回nums中满足i mod 10==nums[i]的最小下标i;如果不存在这样的下标，返 回-1。
# x mod y表示x除以y的余数。

# nums =[0]
# res = 110
# for i in range(len(nums)):
#     if i % 10 == nums[i]:
#         if res >= i:
#             res = i
#
# if res == -1 or res == 110:
#     print(-1)
# else:
#     print(res)


# 存在一种仅支持4种操作和1个变量X的编程语言：
# 2022.09.19
# ++X和X++使变量X的值加1
# --x和x--使变量X的值减1
# 最初，X的值是0
# 给你一个字符串数组operations，这是由操作组成的一个列表，返回执行所有操作后，×的最终值。

# operations = ["--X","X++","X++"]
# x = 0
# for i in operations:
#     if i == 'X++' or i =='++X':
#         x+=1
#     else:
#         x-=1
# print(x)


# 给你一个字符串s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
# 单词是指仅由字母组成、不包含任何空格字符的最大子字符串。

# s = "me"
#
# temp = ''
# sl = []
# for i in s[::-1]:
#     if i != ' ':
#         temp += i
#     else:
#         # print(temp)
#         sl.append(temp)
#         temp = ''
# if temp != '':
#     sl.append(temp)
# print(sl)
# res = 0
# for i in sl:
#     if i != '':
#         res = len(i)
#         break
#
# print(res)


# 给定一个会议时间安排的数组intervals,每个会议时间都会包括开始和结束的时间intervals[i]=[starti,endi]
# # 请你判 断一个人是否能够参加这里面的全部会议。
#
# intervals = [[7,10]]
# #先排序会比较好0
# intervals.sort(key=lambda x:x[0],reverse=False)
# print(intervals)
#
# flag = True
# m = len(intervals)
# for i in range(m):
#     # print(intervals[i])
#     if i + 1 < m:
#         if intervals[i][1] > intervals[i + 1][0]:
#         # if intervals[i][0] <= intervals[i+1][0] <= intervals[i][1] or intervals[i][0] <= intervals[i+1][1] <= intervals[i][1]:
#             flag = False
#             break
# print(flag)


# 给定一个整数，写一个函数来判断它是否是3的幂次方。如果是，返回true;否则，返回false。 2022.09.2
# 整数n是3的幂次方需满足：存在整数x使得n==3x

# n = 45
# temp = 1
# while temp < n:
#     temp *= 3
# if temp == n :
#     print(True)
# else:
#     print(False)


# 给定已经按升序排列、由不同整数组成的数组arr,返回满足arr[i]==i的最小索引i。如果不存在这样的i,返回-1。
# arr =  [-10,-5,3,4,7,9]
#
# res = pow(10,9)+10
# for i in range(len(arr)):
#     if arr[i] == i:
#         if res > i:
#             res = i
# if res == pow(10,9)+10:
#     res = -1
# print(res)
#


# Alice和Bob计划分别去罗马开会。
# 给你四个字符串arriveAlice,leaveAlice,arriveBob和leaveBob。Alice会在日
# 期arriveAlice到leaveAlice之间在城市里（日期为闭区间），而Bob在日期arriveBob到leaveBob之间在城市里（日期
# 为闭区间)。每个字符串都包含5个字符，格式为"MM-DD"，对应着一个日期的月和日。
# 请你返回Alice和Bob同时在罗马的天数。 209.20
# 你可以假设所有日期都在同一个自然年，而且不是闰年。每个月份的天数分别为：[31,28,31,30,31,30,31,31,30， 31,30,31]。
#
#
# arriveAlice = "08-15"
# leaveAlice = "08-18"
# arriveBob = "08-16"
# leaveBob = "08-19"
#
#
# def get_day(s):
#     d = 0
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     for i in range(len(days)):
#         if i < int(s[0]) - 1:
#             d += days[i]
#     d += int(s[1])
#     return d
#
#
# temp1 = arriveAlice.split('-')
# temp2 = leaveAlice.split('-')
# temp3 = arriveBob.split('-')
# temp4 = leaveBob.split('-')
#
# alice = [get_day(temp1), get_day(temp2)]
# print(alice)
# bob = [get_day(temp3), get_day(temp4)]
# print(bob)

# day = 0
# if alice[1] >= bob[0] and bob[1] >= alice[1] and alice[0] <= bob[0]:
#     day = (alice[1] - bob[0])+1
# elif alice[1] >= bob[0] and bob[1] <= alice[1] and alice[0] <= bob[0]:
#     day = bob[1] - bob[0] + 1
# elif bob[0] <= alice[1] and alice[1] <= bob[1]:
#     day = alice[1] - alice[0] + 1
# elif bob[0] <= alice[1] and bob[1] >= alice[0] and bob[1] <= alice[1]:
#     day = bob[1] - alice[0] + 1
#
# day = 0
# dict_day = {}
# i = alice[0]
# while i <= alice[1]:
#     dict_day[i] = 1
#     i = i + 1
# i = bob[0]
# res = 0
# while i <= bob[1]:
#     if i in dict_day:
#         res = res + 1
#     i = i + 1
#
#
# print(day)


# 给你一个由小写英文字母组成的字符串s，请你找出并返回第一个出现两次的字母。
# 注意：
# ·如果a的第二次出现比b的第二次出现在字符串中的位置更靠前，则认为字母a在字母b之前出现两次。
# ·s包含至少一个出现两次的字母。

# s = "abccbaacz"
#
# s_dict = {}
# for i in range(len(s)):
#     if s[i] not in s_dict:
#         s_dict[s[i]] = 1
#     else:
#         s_dict[s[i]] = i
#         print(s[i])
#         break
# print(s_dict)

# 数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在0(n)时间内完成吗？
# nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# n = len(nums) + 1
# nums.sort()
# print(nums)
# for i in range(n):
#     if i not in nums:
#         print(i)
#
#

# 给定一个大小为n的数组nums，返回其中的多数元素。多数元素是指在数组中出现次数大于Ln/2」的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# nums = [2,2,1,1,1,2,2]
#
# n = len(nums)/2
#
# cnt = {}
# for i in nums:
#     cnt[i] = cnt.get(i, 0)+1
# print(cnt)
# for i in cnt:
#     if cnt[i] > n:
#         print(i)


# 给你一个数组，将数组中的元素向右轮转k个位置，其中k是非负数。
# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
#
# while k != 0:


# 给定两个字符串s和七，判断它们是否是同构的
# 如果s中的字符可以按某种映射关系替换得到t，那么这两个字符串是同构的。
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，
# 相同字符只能映射到同一个字符 上，字符可以映射到自己本身。
#
# s = "egg"
# t = "add"
#
#
# def get_map(ss):
#     d = {}
#     temp = ''
#     cnt = 1
#     for i in ss:
#         if i not in d:
#             d[i] = cnt
#             cnt += 1
#             temp += str(d[i])
#         else:
#             temp += str(d[i])
#     # print(d)
#     # print(temp)
#     return temp
#
# st = get_map(s)
# tt = get_map(t)
# if st == tt:
#     print(True)
# else:
#     print(False)


# 给定一个字符串数组wordDict和两个已经存在于该数组中的不同的字符串word1和word2。
# 返回列表中这两个单词之间的最短距 离。

# wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
# word1 = "makes"
# word2 = "coding"
#
# dis = len(wordsDict)
# a = None
# b = None
# for i in range(len(wordsDict)):
#     if wordsDict[i] == word1:
#         a = i
#     if wordsDict[i] == word2:
#         b = i
#     if a is not None and b is not None and abs(a - b) <= dis:
#         dis = abs(a - b)
# print(dis)


# 中心对称数是指一个数字在旋转了180度之后看起来依旧相同的数字（或者上下颠倒地看）。
# # 请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。
#
# num = "69"
#
# temp = ['8', '0', '1']
# new_num = ''
# flag = True
# for i in num:
#     if i == '6':
#         new_num += '9'
#     elif i == '9':
#         new_num += '6'
#     elif i in temp:
#         new_num += i
#     else:
#         flag = False
#         break
# print(new_num)
# if new_num[::-1] == num:
#     flag = True
# else:
#     flag = False
# print(flag)


# flag = True
# for i in range(len(num)):
#     if num[i] not in temp:
#         flag = False
#         break
#     else:
#         if i + 1 < len(num):
#             if num[i] == '6' and num[i + 1] == '9':
#                 flag = True
#             if num[i] == '9' and num[i + 1] == '6':
#                 flag = True
# print(flag)


# 给定两个数组nums1和nums2，返回它们的交集。输出结果中的每个元素一定是唯一的。我们可以不考虑输出结果的顺序。
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
#
# res = []
#
# for i in nums1:
#     if i in nums2 and i not in res:
#         res.append(i)
# print(res)


# # 给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串。
# s = "carerac"
# s_dict = {}
# for i in s:
#     s_dict[i] = s_dict.get(i, 0)+1
# print(s_dict)
# n = len(s_dict)-1
# temp = 0
# for i in s_dict:
#     if s_dict[i] % 2 == 0:
#         temp += 1
# print(temp)
# if temp >= n:
#     print(True)
# else:
#     print(False)


# # 给定一个排序的整数数组nums,其中元素的范围在闭区间[lower,upper]当中，返回不包含在数组中的缺失区间。
# nums = [0,1,3,50,75]
# lower = 0
# upper = 99
# res = []
# # 数组中为空特殊处理
# if len(nums) == 0:
#     if lower == upper:
#         print([str(lower)])
#     else:
#         print([str(lower) + '->' + str(upper)])
#
# for i in range(len(nums)):
#     # 小于最小值不处理
#     if nums[i] < lower:
#         continue
#     # 当第0位比最小值大的时候特殊处理
#     if nums[i] > lower and i == 0:
#         if nums[i] - lower > 1:
#             res.append(str(lower) + '->' + str(nums[i] - 1))
#         else:
#             res.append(str(lower))
#     # 大于最大值不处理
#     if nums[i] > upper:
#         break
#     # 最后一位特殊处理
#     if i >= len(nums) - 1:
#         if nums[i] + 1 == upper :
#             res.append(str(nums[i] + 1))
#         elif nums[i] + 1 < upper:
#             res.append(str(nums[i] + 1) + '->' + str(upper))
#         break
#     # 中间相隔大于1个的答案是区间，比如nums[i]是2, nums[i+1]是5，答案就是3->4
#     if nums[i+1] - nums[i] > 2:
#         res.append(str(nums[i] + 1) + '->' + str(nums[i+1] - 1))
#     # 相差等于2的是nums[i] + 1,比如nums[i]是2，nums[i+1]是4，答案就是3，nums[i]+1这个要理解下
#     elif nums[i+1] - nums[i] == 2:
#         res.append(str(nums[i]+1))
#     else:
#         continue
# print(res)


# 给定两个字符串s和七，它们只包含小写字母。
# 字符串t由字符串s随机重排，然后在随机位置添加一个字母。
# 请找出在t中被添加的字母。
# s = "a"
# t = "aa"
# s_dict = {}
# for i in s:
#     s_dict[i] = s_dict.get(i, 0)+1
# print(s_dict)
# t_dict = {}
# for i in t:
#     t_dict[i] = t_dict.get(i, 0)+1
# print(t_dict)
#
# for i in t_dict:
#     if i not in s_dict:
#         print(i)
#     else:
#         if s_dict[i] != t_dict[i]:
#             print(i)


# 给你一个整数x,如果x是一个回文整数，返回true;否则，返回false。
# 回文数是指正序（从左向右)和倒序（从右向左）读都是一样的整数。
# ·例如，121是回文，而123不是。

# x = -121
#
# new_x = str(x)
# temp = str(x)[::-1]
# print(temp)
# for i in range(len(new_x)-1, -1):
#     print(i)
#     temp += i
# print(temp)


# 给你一个整数数组nums。如果任一值在数组中出现至少两次，返回true;如果数组中每个元素互不相同，返回false。

# nums = [1, 2, 3, 1]
# nums_dict = {}
# flag = False
# for i in nums:
#     if i not in nums_dict:
#         nums_dict[i] = 1
#     else:
#         flag = True
#         break
# print(flag)

# 小扣在秋日市集发现了一款速算机器人。店家对机器人说出两个数字（记作×和y)，请小扣说出计算指令：
# 。"A"运算：使x=2*X+y;
# 。"B"运算：使y=2*Y+x。
# 在本次游戏中，店家说出的数字为x=1和y=0，小扣说出的计算指令记作仅由大写字母A、B组成的字符串s，
# 字符串中 字符的顺序表示计算顺序，请返回最终ⅹ与y的和为多少。

#
# x = 1
# y = 0
#
# s = "AB"
#
# for i in s:
#     if i == 'A':
#         x = 2*x + y
#     else:
#         y = 2*y + x
# print(x+y)


# 给定两个整型数字N与M,以及表示比特位置的i与j（i<=j,且从0位开始计算)。
# 编写一种方法，使M对应的二进制数字插入N对应的二进制数字的第1~5位区域，不足之处用0补齐。具体插入过程如图所示。
# # 题目保证从i位到j位足以容纳M,例如：M=10011,则i~j区域至少可容纳5位。

# def calc_1(a):
#     """
#     十进制转二进制
#     :param a:
#     :return:
#     """
#     n = ""
#     while a > 0:
#         n += str(a % 2)
#         a = a // 2
#     n = n[::-1]
#     return n
#
#
# def calc_2(a):
#     """
#     二进制转十进制
#     :param a:
#     :return:
#     """
#     res = 0
#     for x in range(len(a)):
#         res = res + 2 ** x * int(a[x])
#     return res
#
#
# N, M = 1024, 19
# i, j = 2, 6
# # 把n变成二进制
# n = calc_1(N)
# print(n)
# # 把m变成二进制
# m = calc_1(M)
# # n为空字符特殊处理，答案就是m
# if n == "":
#     res = calc_2(m)
#     print(res)
#
# # 在n的第i到j位直接把m放进去，字符串放在ans上记录答案
# ans = ''
# x = len(n) - 1
# cnt = 0
# while x >= 0:
#     if cnt == i:
#         # 刚好直接加m
#         if j - i + 1 == len(m):
#             ans += m[::-1]
#         else:
#             # 不足补0
#             ans += m[::-1] + (j - i + 1 - len(m)) * '0'
#         # 直接让x移动到加完m后的位置
#         x = len(n) - j - 2
#     else:
#         ans += n[x]
#         x = x - 1
#     cnt += 1
# # 把ans转换成10进制答案
# res = calc_2(ans)
# print(res)


# 给定一个整数，写一个函数来判断它是否是4的幂次方。如果是，返回true;否则，返回false。
# 整数n是4的幂次方需满足：存在整数×使得n==4x
#
# n = 16
# m = 1
# while m < n:
#     m *= 4
# if m == n:
#     print(True)
# else:
#     print(False)


# 魔术索引。在数组A[0.··n-1]中，有所谓的魔术索引，满足条件A[1]=1。给定一个有序整数数组，编写一种方法找出魔术索引，
# 若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
#
# nums = [0, 2, 3, 4, 5]
# res = 1000010
# for i in range(len(nums)):
#     if i == nums[i]:
#         if i < res:
#             res = i
# if res == 1000010:
#     res = -1
#
# print(res)


# 给定一个非负整数num, 反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
# num = 38
#
#
# while True:
#     res = 0
#     for i in range(len(str(num))):
#         # print(str(num)[i])
#         res += int(str(num)[i])
#     if len(str(res)) == 1:
#         print(res)
#         break
#     else:
#         num = res


# 给定一个字符串s，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回-1。
# s = "loveleetcode"
# res = -1
# # for i in range(len(s)):
# #     flag = False
# #     for j in range(len(s)):
# #         if s[i] == s[j] and i != j:
# #             flag = True
# #             i= i+2
# #             break
# #     if not flag:
# #         res = i
# #         break
# # print(res)
# res_dict = {}
# for i in range(len(s)):
#     if s[i] not in res_dict:
#         res_dict[s[i]] = 1
#     else:
#         res_dict[s[i]] += 1
# print(res_dict)
# # for i in
#
# for i in range(len(s)):
#     if res_dict[s[i]] == 1:
#         print(s[i])
#         res = i
#         break
# print(res)


# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# s = "Hello, my  name is John"
# # print(len(s.split(' ')))
# res = []
# temp = ''
# for i in s:
#     if i !=' ':
#         temp += i
#     else:
#         if temp != '':
#             res.append(temp)
#             temp = ''
# if temp != '':
#     res.append(temp)
# print(res)
# print(len(res))


# 给你一个含n个整数的数组nums,其中nums[i]在区间[1，n]内。请你找出所有在[1，n]范围内但没有出现在nums中的 数字，
# 并以数组的形式返回结果。
# nums = [1, 1]
# n = len(nums)
# new_num={}
# for i in nums:
#     new_num[i] = new_num.get(i,0)+1
#
# print(nums,n)
# res = []
# for i in range(1,n+1):
#     if i not in new_num:
#         res.append(i)
# print(res)


# 给你两个整数数组nums1和nums2，请你以数组形式返回两数组的交集。
# 返回结果中每个元素出现的次数，应与元素在两个数组中都 出现的次数一致（如果出现次数不一致，则考虑取较小值）。
# # 可以不考虑输出结果的顺序。
#
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
#
# def get_list(n1,n2):
#     temp = []
#     for i in n1:
#         if i in n2:
#             temp.append(i)
#             n2.remove(i)
#     return temp
#
#
#
# res = []
#
# if len(nums1) < len(nums2):
#     res = get_list(nums1,nums2)
# else:
#     res = get_list(nums2, nums1)
#
# print(res)


# 给你一个下标从0开始的一维整数数组original和两个整数m和n。你需要使用origina1中所有元素创建一个m行n列 的二维数组。
# origina1中下标从0到n-1(都包含)的元素构成二维数组的第一行，下标从n到2*n-1(都包含)的元素构成二维 数组的第二行，依此类推。
# 请你根据上述过程返回一个m×n的二维数组。如果无法构成这样的二维数组，请你返回一个空的二维数组。


original = [1, 2, 3, 4]
m = 2
n = 2
