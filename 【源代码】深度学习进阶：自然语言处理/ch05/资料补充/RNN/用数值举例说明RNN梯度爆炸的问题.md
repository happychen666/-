我们使用 ReLU 激活函数，并计算每个时间步的隐藏状态。

### 假设

- 输入权重 \( W_x = 2.0 \)
- 隐藏状态权重 \( W_h = 2.0 \)
- 偏置 \( b = 0.0 \)

输入序列为：

- 输入序列 \( x_1 = 1.0 \)，\( x_2 = 1.0 \)，\( x_3 = 1.0 \)
- 初始隐藏状态 \( h_0 = 0.0 \)

### 1. 前向传播

#### 第一个时间步 \( t=1 \)

**计算隐藏状态**：

\[
z_1 = W_h \cdot h_0 + W_x \cdot x_1 + b = 2.0 \cdot 0.0 + 2.0 \cdot 1.0 + 0.0 = 2.0
\]

**激活函数**（使用 ReLU）：

\[
h_1 = f(z_1) = f(2.0) = 2.0
\]

#### 第二个时间步 \( t=2 \)

**计算隐藏状态**：

\[
z_2 = W_h \cdot h_1 + W_x \cdot x_2 + b = 2.0 \cdot 2.0 + 2.0 \cdot 1.0 + 0.0 = 4.0 + 2.0 = 6.0
\]

**激活函数**：

\[
h_2 = f(z_2) = f(6.0) = 6.0
\]

#### 第三个时间步 \( t=3 \)

**计算隐藏状态**：

\[
z_3 = W_h \cdot h_2 + W_x \cdot x_3 + b = 2.0 \cdot 6.0 + 2.0 \cdot 1.0 + 0.0 = 12.0 + 2.0 = 14.0
\]

**激活函数**：

\[
h_3 = f(z_3) = f(14.0) = 14.0
\]

### 2. 计算损失

假设我们的目标输出为 \( y = 1.0 \)，使用均方误差（MSE）作为损失函数：

\[
L = \frac{1}{2}(y - h_3)^2 = \frac{1}{2}(1.0 - 14.0)^2 = \frac{1}{2}(-13.0)^2 = 84.5
\]

### 3. 反向传播

#### 计算损失相对于 \( h_3 \) 的梯度

\[
\frac{\partial L}{\partial h_3} = h_3 - y = 14.0 - 1.0 = 13.0
\]

#### 计算 \( h_3 \) 相对于 \( z_3 \) 的梯度

激活函数的导数（ReLU 的导数）：

\[
\frac{\partial h_3}{\partial z_3} = 1 \quad (\text{因为 } z_3 = 14.0)
\]

根据链式法则：

\[
\frac{\partial L}{\partial z_3} = \frac{\partial L}{\partial h_3} \cdot \frac{\partial h_3}{\partial z_3} = 13.0 \cdot 1 = 13.0
\]

#### 计算 \( z_3 \) 相对于 \( h_2 \) 的梯度

\[
\frac{\partial L}{\partial h_2} = \frac{\partial L}{\partial z_3} \cdot W_h = 13.0 \cdot 2.0 = 26.0
\]

#### 计算 \( h_2 \) 相对于 \( z_2 \) 的梯度

\[
\frac{\partial h_2}{\partial z_2} = 1 \quad (\text{因为 } z_2 = 6.0)
\]

\[
\frac{\partial L}{\partial z_2} = \frac{\partial L}{\partial h_2} \cdot \frac{\partial h_2}{\partial z_2} = 26.0 \cdot 1 = 26.0
\]

#### 计算 \( h_1 \) 相对于 \( z_1 \) 的梯度

\[
\frac{\partial L}{\partial h_1} = \frac{\partial L}{\partial z_2} \cdot W_h = 26.0 \cdot 2.0 = 52.0
\]

#### 计算 \( z_2 \) 相对于 \( h_1 \) 的梯度

\[
\frac{\partial h_1}{\partial z_1} = 1 \quad (\text{因为 } z_1 = 2.0)
\]

\[
\frac{\partial L}{\partial z_1} = \frac{\partial L}{\partial h_1} \cdot \frac{\partial h_1}{\partial z_1} = 52.0 \cdot 1 = 52.0
\]

### 4. 梯度爆炸的现象

通过这个例子，我们可以看到在每个时间步的反向传播中，梯度都在不断增加，尤其是在使用较大的权重时。这种不断增加的梯度最终导致了“梯度爆炸”现象。

#### 最终梯度

- \( \frac{\partial L}{\partial h_1} = 52.0 \)
- \( \frac{\partial L}{\partial h_2} = 26.0 \)
- \( \frac{\partial L}{\partial h_3} = 13.0 \)

这个修正后的例子展示了在 RNN 中，尤其是当权重较大时，梯度在反向传播过程中可以迅速增大，导致梯度爆炸的问题。实际应用中，需要采用梯度裁剪（gradient clipping）等技术来防止这一现象。
