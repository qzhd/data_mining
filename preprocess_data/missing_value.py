# -*- coding: utf-8 -*-

#   file-name | missing_value
#      author | qzhd
#        date | 2017/12/23
# description |

import pandas as pd

from io import StringIO

csv_data = '''A,B,C,D
helo,1.0,2.0,2.0
helo,1.0,2.0,2.0
helo,,2.0,2.0
helo,NaN,2.0,2.0
helo,1.0,2.0,
'''

df = pd.read_csv(StringIO(csv_data))
print(df.columns)
# 查看numpy数组
#print(df.values)
# 查看每一列缺失值的个数
#print(df.isnull().sum())
# 删除包含nan的所有行(默认)
#df = df.dropna(axis=0)
# 删除包含nan的所有列
#df = df.dropna(axis=0)
#
df = df.dropna(how='all')
df = df.dropna(thresh=4)
df = df.dropna(subset=['C'])
print(df)





