好的！我们将使用之前提供的`cross_entropy_error`函数，并通过一个具体的例子详细说明每一步的计算过程。

### 示例数据

假设我们有3个样本的预测概率和真实标签如下：

- **预测概率 \( y \)**：
    - 样本1：\( [0.7, 0.2, 0.1] \)
    - 样本2：\( [0.1, 0.8, 0.1] \)
    - 样本3：\( [0.2, 0.2, 0.6] \)

- **真实标签 \( t \)**（one-hot编码）：
    - 样本1：\( [1, 0, 0] \)  (类别1)
    - 样本2：\( [0, 1, 0] \)  (类别2)
    - 样本3：\( [0, 0, 1] \)  (类别3)

### 代码实现

以下是如何使用`cross_entropy_error`函数的步骤：

```python
import numpy as np

def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    # 在监督标签为one-hot-vector的情况下，转换为正确解标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)
             
    batch_size = y.shape[0]

    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size

# 预测概率
y = np.array([[0.7, 0.2, 0.1], 
              [0.1, 0.8, 0.1], 
              [0.2, 0.2, 0.6]])

# 真实标签
t = np.array([[1, 0, 0], 
              [0, 1, 0], 
              [0, 0, 1]])

# 计算交叉熵损失
loss = cross_entropy_error(y, t)
print("Cross entropy loss:", loss)
```

### 计算步骤详解

1. **输入数据**：
   - 预测概率 \( y \) 为一个 \( 3 \times 3 \) 的数组。
   - 真实标签 \( t \) 也是一个 \( 3 \times 3 \) 的数组。

2. **维度调整**：
   ```python
   if y.ndim == 1:
       t = t.reshape(1, t.size)
       y = y.reshape(1, y.size)
   ```
   - 在这个例子中，`y`和`t`都是二维数组，所以这一段代码不会改变它们的形状。

3. **标签转换**：
   ```python
   if t.size == y.size:
       t = t.argmax(axis=1)
   ```
   - 这里的`t`是one-hot编码，所以需要转换为类别索引。
   - 计算过程：
     - 样本1的真实标签：\( t[0] = [1, 0, 0] \) → 类别索引为0
     - 样本2的真实标签：\( t[1] = [0, 1, 0] \) → 类别索引为1
     - 样本3的真实标签：\( t[2] = [0, 0, 1] \) → 类别索引为2
   - 转换后的`t`为：\[0, 1, 2\]

4. **批量大小**：
   ```python
   batch_size = y.shape[0]
   ```
   - `batch_size` = 3，因为有3个样本。

5. **计算交叉熵损失**：
   ```python
   return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
   ```
   - 提取每个样本对应的预测概率：
     - 样本1：\( y[0, 0] = 0.7 \)
     - 样本2：\( y[1, 1] = 0.8 \)
     - 样本3：\( y[2, 2] = 0.6 \)

   - 计算对数：
     \[
     \log(y[0, 0]) = \log(0.7) \approx -0.3567
     \]
     \[
     \log(y[1, 1]) = \log(0.8) \approx -0.2231
     \]
     \[
     \log(y[2, 2]) = \log(0.6) \approx -0.5108
     \]

   - 加上一个小常数防止对数为零：
     \[
     \text{Total} = -\left(\log(0.7) + \log(0.8) + \log(0.6)\right) \approx -(-0.3567 - 0.2231 - 0.5108) \approx 1.0906
     \]

   - 计算平均损失：
     \[
     \text{Loss} = \frac{1.0906}{3} \approx 0.3635
     \]

### 输出结果
最终，运行代码后将输出：
```
Cross entropy loss: 0.3635
```

这个结果表明，模型的预测和真实标签之间的差异，损失值越小，模型的预测越接近真实标签。