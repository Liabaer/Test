#f = open('C:\\Users\\dayday\\Desktop\\SunSign.csv','r',encoding = 'utf-8')
#fr = f.readlines()
#f.close()
#d = {}
#ls = []
#for i in fr[1:]:
#    i = i.strip()
#    temp = i.split(',')
#    ls.append(temp[2])
#    ls.append(temp[3])
#    d[temp[1]] = ls
#    ls = []
#n = input('请输入星座中文名称：')
#for i in d:
#    s = d[i][0]
#    e = d[i][1]
#    if n == i:
#        print("{}的生日位于{}-{}之间".format(n,s,e))


n = input('请输入星座序号：')
ls = []
ls = n.split(',')
f = open('C:\\Users\\dayday\\Desktop\\SunSign.csv','r',encoding = 'utf-8')
fr = f.readlines()
f.close()
d = {}
res = []
for i in fr[1:]:
    i = i.strip()
    temp = i.split(',')
    a = temp[1]
    b = temp[-1]
    sd = temp[2][-2:]
    sy = temp[2][:-2]
    ed = temp[3][-2:]
    ey = temp[3][:-2]
    res=[a,b,sy,sd,ey,ed]
    d[temp[0]] = res
    res = []
while n != "":
    for i in ls:
        if 1<= int(i) <=12 and i in d :
            ans = d[i]
            print("{}({})的生日是{}月{}日至{}月{}日之间".format(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5]))
        else:
            print("输入星座序号有误！")
    n = input('请输入星座序号：')
    
