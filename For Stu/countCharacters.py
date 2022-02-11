# -*- coding: utf-8 -*-
# 给你一份『词汇表』（字符串数组）words和一张『字母表』（字符串）chars。
#
# 假如你可以用chars中的『字母』（字符）拼写出 words中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
#
# 注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。
#
# 返回词汇表words中你掌握的所有单词的 长度之和。

words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
         "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb", "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl", "boygirdlggnh",
         "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
         "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
         "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
         "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr", "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
         "oxgaskztzroxuntiwlfyufddl", "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
         "qnagrpfzlyrouolqquytwnwnsqnmuzphne", "eeilfdaookieawrrbvtnqfzcricvhpiv", "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
         "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
         "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
         "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo", "teyygdmmyadppuopvqdodaczob",
         "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs", "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]

chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"


def be_dict(a):
    b = {}
    for i in range(0, len(a)):
        if a[i] not in b:
            b[a[i]] = 1
        else:
            b[a[i]] = b[a[i]] + 1
    return b


chars_dict = be_dict(chars)
print(chars_dict)

i = 0
num = 0
while i < len(words):
    j = 0
    flag = True
    words_dict = be_dict(words[i])
    # print(words[i])
    for k, v in words_dict.items():
        if k in chars_dict:
            if v > chars_dict[k]:
                flag = False
                break
        else:
            # 注意这里也要让flag等于false
            flag = False
            break
    if flag:
        num = num + len(words[i])
        print(num)
    i = i + 1
print(num)
