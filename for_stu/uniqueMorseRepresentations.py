# -*- coding: utf-8 -*-
# 国际摩尔斯密码定义一种标准编码方式，将每个字母对应于一个由一系列点和短线组成的字符串， 比如:
#
# 'a' 对应 ".-" ，
# 'b' 对应 "-..." ，
# 'c' 对应 "-.-." ，以此类推。
# 为了方便，所有 26 个英文字母的摩尔斯密码表如下：
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# 给你一个字符串数组 words ，每个单词可以写成每个字母对应摩尔斯密码的组合。
#
# 例如，"cab" 可以写成 "-.-..--..." ，(即 "-.-." + ".-" + "-..." 字符串的结合)。我们将这样一个连接过程称作 单词翻译 。
# 对 words 中所有单词进行单词翻译，返回不同 单词翻译 的数量。

nums = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
words = ["gin","zen","gig","msg"]

temps = []
for i in range(0, len(words)):
    temp = ''
    # temp = temp + nums[ord(words[i]) - ord('a')]
    # print(words[i])
    for j in range(0, len(words[i])):
        temp = temp + nums[ord(words[i][j]) - ord('a')]
        # print(words[i][j], temp)
    temps.append(temp)
print(temps)
m = 0
count = 1

if len(temps) == 1:
    count = 1
else:
    while m <= len(temps) - 1:
        n = m + 1
        flag = False
        while n <= len(temps)-1:
            print(m, temps[m], n ,temps[n], count)
            if m == n:
                n = n + 1
                continue
            if temps[m] != temps[n]:
                flag = True
                n = n + 1
            else:
                flag = False
                break
        m = m + 1
        if flag:
            count = count + 1
print(count)