import csv

b_f = open('b.txt', 'r')
b_f = b_f.readlines()
flag = False
temp = []
dict_b = []
max_lenth = 0
for i in b_f:
    if "01." in i:
        if flag == False:
            flag = True
            temp.append(i)
        else:
            flag = True
            if max_lenth < len(temp) :
                max_lenth = len(temp)
            dict_b.append(temp)
            temp = []
            temp.append(i)
    else:
        temp.append(i)

print(dict_b)

f = open('a.txt', 'r')
f = f.readlines()
csv_f = open('out.csv', 'w')
csv_write = csv.writer(csv_f)
# 单行写入
i = 0
row_list = []

for i in f:
    row_list.append(i)
csv_write.writerow(row_list)
i = 0
j = 0
while j < max_lenth:
    temp = []
    i = 0
    while i < len(dict_b):
        if j >= len(dict_b[i]):
            i += 1
            temp.append("")
            continue
        temp.append(dict_b[i][j])
        i += 1
    j += 1
    if len(temp) != 0:
        csv_write.writerow(temp)





