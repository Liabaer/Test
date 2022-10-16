# -*- coding: utf-8 -*-
# 包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度(向下舍入)
# 平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。
img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
avg = 0
i = 0
z = 0
new_img = []
while z < len(img):
    y = 0
    b = []
    while y < len(img[0]):
        b.append(0)
        y += 1
    z += 1
    new_img.append(b)
while i < len(img):
    j = 0
    while j < len(img[i]):
        # print img[i][j]
        count = 1
        sum = 0
        # 上边
        if i - 1 >= 0:
            count = count + 1
            sum = sum + img[i - 1][j]
        # 下边
        if i + 1 < len(img):
            count = count + 1
            sum = sum + img[i + 1][j]
        # 左边
        if j - 1 >= 0:
            count = count + 1
            sum = sum + img[i][j - 1]
        # 右边
        if j + 1 < len(img[i]):
            count = count + 1
            sum = sum + img[i][j + 1]
        # 左上边
        if j - 1 >= 0 and i - 1 >= 0:
            count = count + 1
            sum = sum + img[i - 1][j - 1]
        # 右上边
        if i - 1 >= 0 and j + 1 < len(img[i]):
            count = count + 1
            sum = sum + img[i - 1][j + 1]
        # 左下边
        if j - 1 >= 0 and i + 1 < len(img):
            count = count + 1
            sum = sum + img[i + 1][j - 1]
        # 右下边
        if j + 1 < len(img[i]) and i + 1 < len(img):
            count = count + 1
            sum = sum + img[i + 1][j + 1]
        sum = sum + img[i][j]
        print(sum, count)
        avg = sum / count
        # print avg
        # print '----'
        new_img[i][j] = avg
        j = j + 1
    i = i + 1
# print new_img
