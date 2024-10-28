from sklearn.datasets import load_breast_cancer
breast_cancer = load_breast_cancer()
# 分离出特征变量与目标变量
x = breast_cancer.data
y = breast_cancer.target
from sklearn.model_selection import train_test_split
# 使用数据分割器将样本数据分割为训练数据和测试数据，其中测试数据占比为 30%。
# 数据分割是为了获得训练集和测试集。训练集用来训练模型，测试集用来评估模型性能。
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=33, test_size=0.3)

from sklearn.preprocessing import StandardScaler
breast_cancer_ss = StandardScaler()
# 对训练数据进行标准化处理，使得每个特征维度的均值为 0，方差为 1，防止受到某个维度特征数值较大的影响。
x_train = breast_cancer_ss.fit_transform(x_train)
# 对测试数据进行标准化处理，使用的是在训练数据上拟合得到的标准化参数。
x_test = breast_cancer_ss.transform(x_test)

from sklearn.linear_model import LogisticRegression
# 使用默认配置初始化线性回归器。
lr = LogisticRegression()
# 使用训练数据来估计参数，也就是通过训练数据的学习，找到一组合适的参数，从而获得一个带有参数的、具体的算法模型。
lr.fit(x_train, y_train)
# 对测试数据进行预测。利用上述训练数据学习得到的带有参数的、具体的线性回归模型对测试数据进行预测，
# 即将测试数据中每一条记录的特征变量输入该模型中，得到一个该条记录的预测分类值。
lr_y_predict = lr.predict(x_test)

from sklearn.metrics import classification_report
# 使用逻辑回归自带的评分函数 score 获取预测准确率数据，并使用 sklearn.metrics 的 classification_report 模块对预测结果进行全面评估。
print('Accuracy:', lr.score(x_test, y_test))
print(classification_report(y_test, lr_y_predict, target_names=['benign', 'malignant']))