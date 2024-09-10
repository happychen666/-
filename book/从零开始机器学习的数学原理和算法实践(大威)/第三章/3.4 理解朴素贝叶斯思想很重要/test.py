# 导入必要的库
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# 文本数据集
docs = [
    "足球 足球 足球 篮球",
    "篮球 篮球 足球",
    "科技 计算机 计算机 计算机",
    "科技 计算机",
    "足球 科技 计算机",
    "足球 篮球 篮球",
    "计算机 科技",
    "足球 篮球 篮球 足球"
]

# 标签：0表示“体育新闻”，1表示“科技新闻”
labels = [0, 0, 1, 1, 1, 0, 1, 0]

# 将文本转换为词频矩阵
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(docs)

# 分割数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=42)

# 训练多项式朴素贝叶斯模型
clf = MultinomialNB()
clf.fit(X_train, y_train)

# 输出模型准确率
print('模型在测试集上的准确率：', clf.score(X_test, y_test))
