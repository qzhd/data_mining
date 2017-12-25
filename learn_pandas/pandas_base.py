# -*- coding: utf-8 -*-

#   file-name | pandas_base
#      author | qzhd
#        date | 2017/12/23
# description |

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Series是pandas的对象，类似于numpy的一维的array，可以理解为带索引的以为数组

s = pd.Series([1,3,5,np.nan,6,8])
print(s)

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
'''
print(df.dtypes)
print(df.head())
print(df.tail(3))

print(df.index,df.columns,df.values)

# describe()函数对于数据的快速统计汇总：
print(df.describe())
print(df.T)

# 按轴进行排序
df.sort_index(axis=1,ascending=False)

# 按值进行排序
df.sort(columns='B')


##########  选择
print(df['A'])
print(df[0:3])

# loc选择交叉区域
print(df.loc[:,['A','B']])
# iloc是通过索引来选择交叉区域
print(df.iloc[3:5,[0,2]])


# 布尔索引
print(df[df.A > 0])
print(df[df > 0])


df2 = df.copy()
df2['E'] = [1,2,3,4,5,6]

print(df2[df2['E'].isin([1,2])])

#########设置新的值
'''
#通过标签设置新的值：
df.at[dates[0],'A'] = 0
#通过位置设置新的值：
df.iat[0,1] = 0
#通过一个numpy数组设置一组新值：
df.loc[:,'D'] = np.array([5] * len(df))

df['E'] = [3,4,3,2,3,2]
print(df.groupby('D').sum())
print(df.groupby(['D','E']).sum())