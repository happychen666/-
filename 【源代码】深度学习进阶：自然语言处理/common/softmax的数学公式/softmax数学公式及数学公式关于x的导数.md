### Softmax 的数学公式

Softmax 函数用于将任意实数向量转换为概率分布，其数学表达式为：

对于输入向量 \( x \) 的第 \( i \) 个元素，Softmax 函数定义为：

\[
y_i = \frac{e^{x_i}}{\sum_{j} e^{x_j}}
\]

其中：

- \( y_i \) 是归一化后的输出（概率）。
- \( e \) 是自然对数的底数。
- \( x_j \) 是输入向量 \( x \) 的第 \( j \) 个元素。

### Softmax 的性质

- 输出的所有 \( y_i \) 之和为 1：
  \[
  \sum_{i} y_i = 1
  \]
- 输出值 \( y_i \) 的范围在 \( (0, 1) \) 之间。

### Softmax 的导数

Softmax 的导数在计算反向传播时非常重要。我们需要求得 Softmax 输出 \( y_i \) 对于输入 \( x_j \) 的导数。

#### 导数的推导

对于 Softmax 输出 \( y_i \)，可以推导出其导数：

\[
\frac{\partial y_i}{\partial x_j} =
\begin{cases}
y_i (1 - y_i), & \text{if } i = j \\
-y_i y_j, & \text{if } i \neq j
\end{cases}
\]

### 解释推导过程

1. **对角项（\( i = j \)）**：

\[
\frac{\partial y_i}{\partial x_i} = \frac{\partial}{\partial x_i} \left( \frac{e^{x_i}}{\sum_{k} e^{x_k}} \right)
\]

使用商法则得到：

\[
= \frac{e^{x_i} \cdot \sum_{k} e^{x_k} - e^{x_i} \cdot e^{x_i}}{(\sum_{k} e^{x_k})^2}
\]
\[
= \frac{e^{x_i} \left( \sum_{k} e^{x_k} - e^{x_i} \right)}{(\sum_{k} e^{x_k})^2}
\]
\[
= \frac{e^{x_i}}{\sum_{k} e^{x_k}} \left(1 - \frac{e^{x_i}}{\sum_{k} e^{x_k}}\right)
\]
\[
= y_i (1 - y_i)
\]

2. **非对角项（\( i \neq j \)）**：

\[
\frac{\partial y_i}{\partial x_j} = \frac{\partial}{\partial x_j} \left( \frac{e^{x_i}}{\sum_{k} e^{x_k}} \right)
\]
使用商法则得到：

\[
= \frac{0 \cdot \sum_{k} e^{x_k} - e^{x_i} \cdot e^{x_j}}{(\sum_{k} e^{x_k})^2}
\]
\[
= -\frac{e^{x_i} \cdot e^{x_j}}{(\sum_{k} e^{x_k})^2}
\]
\[
= -y_i y_j
\]

### 总结

- **Softmax 函数**：将输入向量 \( x \) 转换为概率分布 \( y \) 的公式为：

\[
y_i = \frac{e^{x_i}}{\sum_{j} e^{x_j}}
\]

- **Softmax 导数**：

\[
\frac{\partial y_i}{\partial x_j} =
\begin{cases}
y_i (1 - y_i), & \text{if } i = j \\
-y_i y_j, & \text{if } i \neq j
\end{cases}
\]

这个导数对于实现反向传播和梯度更新非常重要。
