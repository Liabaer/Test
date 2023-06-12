# -*- coding: utf-8 -*-
import pandas as pd
# 这是一个简单的pandas实例
mydataset = {
    'sites':["Google","Runoob","Wiki"],
    'number':[1,2,3]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

# 输出结果
#     sites  number
# 0  Google       1
# 1  Runoob       2
# 2    Wiki       3
