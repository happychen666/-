```python
#导入数据集生成工具
from sklearn.datasets import make_blobs
#生成样本数量为800、分类数量为6的数据集
x, y = make_blobs(n_samples=800, centers=6, random_state=6)
#导入数据拆分工具，将数据集拆分为训练集和测试集
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=33)
#导入高斯朴素贝叶斯分类器
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train, y_train)
print('*' * 50)
print('高斯朴素贝叶斯准确率：', gnb.score(x_test, y_test))
print('*' * 50)
```