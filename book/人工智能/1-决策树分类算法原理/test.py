columns = ['日志密度','好友密度','真实头像']
lower_entropy = 1
condition = {}
for col in columns:
    x = X[col].unique()
    x.sort()
    print(x)
    # 如何划分呢，分成两部分
    for i in range(len(x) - 1):
        split = x[i:i+2].mean()
        cond = X[col] <= split
        # 概率分布
        p = cond.value_counts()/cond.size
        # 按照条件划分，两边的概率分布情况
        indexs =p.index
        entropy = 0
        for index in indexs:
            user = X[cond == index]['真实用户']
            p_user = user.value_counts()/user.size
            entropy += (p_user * np.log2(1/p_user)).sum() * p[index]
        print(col,split,entropy)
        if entropy < lower_entropy:
            condition.clear()
            lower_entropy = entropy
            condition[col] = split
print('最佳列分条件是：',condition)
