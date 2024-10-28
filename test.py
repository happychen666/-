from scipy import linalg
n_components_ = 3
X,y = datasets.load_iris(return_X_y = True)
# 1、去中心化
mean_ = np.mean(X, axis=0)
X -= mean_
# 2、奇异值分解
U, S, Vt = linalg.svd(X, full_matrices=False)
# 3、符号翻转（如果为负数，那么变成正直）
max_abs_cols = np.argmax(np.abs(U), axis=0)
signs = np.sign(U[max_abs_cols, range(U.shape[1])])
U *= signs
# 4、降维特征筛选
U = U[:, :n_components_]
# 5、归一化
# U = (U - U.mean(axis = 0))/U.std(axis = 0)
U *= np.sqrt(X.shape[0] - 1)
U[:5]