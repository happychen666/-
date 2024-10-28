import numpy as np
import pandas as pd
y = np.array(list('NYYYYYNYYN'))
print(y)
X = pd.DataFrame({'日志密度':list('sslmlmmlms'),
'好友密度':list('slmmmlsmss'),
'真实头像':list('NYYYYNYYYY'),
'真实用户':y})

X['日志密度'] = X['日志密度'].map({'s':0,'m':1,'l':2})
X['好友密度'] = X['好友密度'].map({'s':0,'m':1,'l':2})
X['真实头像'] = X['真实头像'].map({'N':0,'Y':1})

x = X['日志密度'].unique()
x.sort()

for i in range(len(x) - 1):
split = x[i:i+2].mean()
cond = X['日志密度'] <= split
# 概率分布
p = cond.value_counts()/cond.size
# 按照条件划分，两边的概率分布情况
indexs =p.index
entropy = 0
for index in indexs:
user = X[cond == index]['真实用户']
p_user = user.value_counts()/user.size
entropy += (p_user * np.log2(1/p_user)).sum() * p[index]
print(split,entropy)