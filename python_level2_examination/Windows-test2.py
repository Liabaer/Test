picd = {}
fi = open('C:\\Users\\dayday\\Desktop\\dir_50.txt','r')
for l in fi:
    l = l.strip()
    if len(l):
        t = l.find('_')
        temp = l[t+1:]
        temp2 = l[:t]
        lkey = temp.split('.')[0]
        val = eval(temp2)
        lval = []
        for j in val:
            if j != '0':
                lval.append(j)
        picd[lkey] = lval

fi.close()
idd = {}
for key in picd:
    for k in picd[key]:
        idd[k] = idd.get(k,0) + 1
count = 0
s = 0
for i in idd:
    s += idd[i]
    count += 1
print("实际参加测试的人数是：{}".format(count))
print("人均被测次数是：{:.1f}".format(s/count))
