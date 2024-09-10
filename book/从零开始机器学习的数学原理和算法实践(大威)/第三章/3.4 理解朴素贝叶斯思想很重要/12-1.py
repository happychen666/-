# 导入天气情况的数据集
import numpy as np

x = np.array([[0, 1, 0, 1], 
              [1, 1, 1, 1], 
              [1, 1, 1, 0], 
              [0, 1, 1, 0], 
              [0, 1, 0, 0], 
              [0, 1, 0, 1], 
              [1, 1, 0, 1], 
              [1, 0, 0, 1], 
              [1, 1, 0, 1], 
              [0, 0, 0, 0]])

y = np.array([1, 1, 1, 1, 0, 1, 0, 1, 1, 0])

# 导入伯努利贝叶斯分类器并训练数据
from sklearn.naive_bayes import BernoulliNB

bnb = BernoulliNB()
bnb.fit(x, y)

# 对新的数据进行预测
day_pre = [[0, 0, 1, 0]]
pre = bnb.predict(day_pre)

print('预测结果如下所示：')
print('*' * 50)
print('结果为：', pre)
print('*' * 50)

#进⼀步查看是否下⾬的概率分布情况
pre_pro=bnb.predict_proba(day_pre)
print(' 预测概率情况如下所⽰：')
print('*'*50)
print(' 结果为：',pre_pro)
print('*'*50)