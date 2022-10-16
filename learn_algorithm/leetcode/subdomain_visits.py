# -*- coding: utf-8 -*-
# 网站域名 "discuss.leetcode.com" 由多个子域名组成。顶级域名为 "com" ，二级域名为 "leetcode.com" ，最低一级为 "discuss.leetcode.com" 。
# 当访问域名 "discuss.leetcode.com" 时，同时也会隐式访问其父域名 "leetcode.com" 以及 "com" 。
# 计数配对域名 是遵循 "rep d1.d2.d3" 或 "rep d1.d2" 格式的一个域名表示，其中 rep 表示访问域名的次数，d1.d2.d3 为域名本身。
# 例如，"9001 discuss.leetcode.com" 就是一个 计数配对域名 ，表示 discuss.leetcode.com 被访问了 9001 次。
# 给你一个 计数配对域名 组成的数组 cpdomains ，解析得到输入中每个子域名对应的计数配对域名 ，并以数组形式返回。可以按 任意顺序 返回答案。
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]

i = 0
temp = {}
while i < len(cpdomains):
    j = 0
    num = ''
    ip_str = ''
    ip = []
    while j < len(cpdomains[i]):
        if cpdomains[i][j] != ' ' and 48 <= ord(cpdomains[i][j]) <= 57:
            num = num + cpdomains[i][j]
            j = j + 1
            continue
        if cpdomains[i][j] == ' ':
            j = j + 1
            continue
        if cpdomains[i][j] != '.':
            ip_str = ip_str + cpdomains[i][j]
        if cpdomains[i][j] == '.':
            ip.append(ip_str)
            ip_str = ''
            j = j + 1
            continue
        if j == len(cpdomains[i]) - 1 and cpdomains[i][j] != '.':
            ip.append(ip_str)
            ip_str = ''
            j = j + 1
            continue
        j = j + 1

    num = int(num)
    if len(ip) == 3:
        ip1 = ip[0] + '.' + ip[1] + '.' + ip[2]
        if ip1 not in temp:
            temp[ip1] = num
        else:
            temp[ip1] = temp[ip1] + num
        ip2 = ip[1] + '.' + ip[2]
        if ip2 not in temp:
            temp[ip2] = num
        else:
            temp[ip2] = temp[ip2] + num
        ip3 = ip[2]
        if ip3 not in temp:
            temp[ip3] = num
        else:
            temp[ip3] = temp[ip3] + num
    if len(ip) == 2:
        ip2 = ip[0] + '.' + ip[1]
        if ip2 not in temp:
            temp[ip2] = num
        else:
            temp[ip2] = temp[ip2] + num
        ip3 = ip[1]
        if ip3 not in temp:
            temp[ip3] = num
        else:
            temp[ip3] = temp[ip3] + num
    if len(ip) == 1:
        ip3 = ip[0]
        if ip3 not in temp:
            temp[ip3] = num
        else:
            temp[ip3] = temp[ip3] + num
    i = i + 1
print(num)
print(ip)
print(temp)
res_times = ''
res = []
for k, v in temp.items():
    res_times = str(v) + ' ' + k
    res.append(res_times)
print(res)
