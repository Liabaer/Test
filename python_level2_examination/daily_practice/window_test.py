# 《神雕侠侣》中出现了很多人物，这里给出6个人物名字：杨过、小龙女、李莫 愁、裘千尺、郭靖、黄蓉。
# 统计人物之间的关联关系，定义一种“亲和度"如下：如 果某名字后的100个词语出现另外任何一个人名，则该名字亲和度加1，
# 如果之后不 存在100个词语则停止检查。
import jieba

fi = open("神雕侠侣-网络版本.txt", "r", encoding='utf-8')
fo = open("神雕侠侣-亲和度.txt", 'w')
names = ["杨过", "小龙女", "李莫愁", "裘千尺", "郭靖", "黄蓉"]
d = {}
for item1 in names:
    for item2 in names:
        if item1 != item2:
            d[item1 + "-" + item2] = 0
txt = fi.read()
ls = jieba.lcut(txt)
# 循环数组
for i in range(len(ls)):
    # 如果名字在names里面就找他在100之内是否有存在另一个名字
    if ls[i] in names:
        for j in range(1, 101):
            # 这里处理越界
            if i + j >= len(ls):
                break
            else:
                # 如果100个词语中出现任一一个在names里的名字且不与i相等，则让他在字典中的values+1
                if ls[i + j] in names and ls[i] != ls[i + j]:
                    d[ls[i] + '-' + ls[i + j]] += 1
                    break
ols = []
for key in d:
    ols.append('{}:{}'.format(key, d[key]))
fo.write(",".join(ols))
fo.close()
fi.close()
