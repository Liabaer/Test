# -*- coding: utf-8 -*-
# 一个 句子由一些 单词以及它们之间的单个空格组成，句子的开头和结尾不会有多余空格。
#
# 给你一个字符串数组sentences，其中sentences[i]表示单个 句子。
#
# 请你返回单个句子里 单词的最多数目。
# 外面假设循环的是n次里面循环的是m次 所以是O(n * m ) 所以这个题目就是O(n * m) 如果m 等于n就是o(n^2)（该代码时间复杂度是O(n*m) n是字符串数组的长度 m是字符串的长度）
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

i = 0
res = 0
while i < len(sentences):
    j = 0
    new_sen_str = ''
    new_sentences = []
    num = 0
    while j < len(sentences[i]):
        if sentences[i][j] != ' ':
            new_sen_str = new_sen_str + sentences[i][j]
        else:
            num = num + 1
            new_sentences.append(new_sen_str)
            new_sen_str = ' '
        j = j + 1
    i = i + 1
    if new_sen_str != ' ':
        num = num + 1
        new_sentences.append(new_sen_str)
    if res < num:
        res = num
    print(new_sentences, num)
print(res)
