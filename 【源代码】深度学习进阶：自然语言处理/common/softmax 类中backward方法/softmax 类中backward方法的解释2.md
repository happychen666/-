明白了，我们重点详细地展开重组与最终化简的过程，从中间步骤到最终结果，不省略任何部分。

### 目标公式

我们要化简的公式是：
\[
\frac{\partial L}{\partial x_i} = \frac{\partial L}{\partial o_i} \cdot (o_i (1 - o_i)) - o_i \sum_{j \neq i} o_j \cdot \frac{\partial L}{\partial o_j}
\]

### 1. 将公式重写

我们可以将这个公式分开为两部分：

1. 自导数部分：
   \[
   \frac{\partial L}{\partial o_i} \cdot (o_i (1 - o_i))
   \]
2. 互导数部分：
   \[
   -o_i \sum_{j \neq i} o_j \cdot \frac{\partial L}{\partial o_j}
   \]

### 2. 提取公共因子

我们注意到 \(o_i\) 在两个部分中都可以提取出来。为此，我们重新组织这个公式。

1. 首先，保留自导数部分，得到：
   \[
   \frac{\partial L}{\partial x_i} = o_i \cdot \frac{\partial L}{\partial o_i} (1 - o_i) + \text{(互导数部分)}
   \]

2. 现在，互导数部分可以改写为：
   \[
   -o_i \sum_{j \neq i} o_j \cdot \frac{\partial L}{\partial o_j} = -o_i \left( \sum_{j} o_j \cdot \frac{\partial L}{\partial o_j} - o_i \cdot \frac{\partial L}{\partial o_i} \right)
   \]

   这里我们将和式 \( \sum_{j} o_j \cdot \frac{\partial L}{\partial o_j} \) 拆分为 \(j=i\) 和 \(j\neq i\) 两部分。这样做的目的是将 \(o_i\) 的项提取出来。

### 3. 合并两部分

将自导数部分与互导数部分结合：
\[
\frac{\partial L}{\partial x_i} = o_i \cdot \frac{\partial L}{\partial o_i} (1 - o_i) - o_i \left( \sum_{j} o_j \cdot \frac{\partial L}{\partial o_j} - o_i \cdot \frac{\partial L}{\partial o_i} \right)
\]

### 4. 展开互导数部分

展开互导数部分：
\[
= o_i \cdot \frac{\partial L}{\partial o_i} (1 - o_i) - o_i \sum_{j} o_j \cdot \frac{\partial L}{\partial o_j} + o_i^2 \cdot \frac{\partial L}{\partial o_i}
\]

### 5. 组合同类项

将同类项组合在一起，注意到：

- \(o_i \cdot \frac{\partial L}{\partial o_i} (1 - o_i) + o_i^2 \cdot \frac{\partial L}{\partial o_i} = o_i \cdot \frac{\partial L}{\partial o_i}\)

因此我们可以得到：
\[
\frac{\partial L}{\partial x_i} = o_i \left( \frac{\partial L}{\partial o_i} (1 - o_i) + o_i \cdot \frac{\partial L}{\partial o_i} - \sum_{j} o_j \cdot \frac{\partial L}{\partial o_j} \right)
\]

### 6. 最终化简

最终，我们可以将其整理为：
\[
\frac{\partial L}{\partial x_i} = o_i \left( \frac{\partial L}{\partial o_i} - \sum_{j} o_j \cdot \frac{\partial L}{\partial o_j} \right)
\]

### 总结

在这个过程中，我们通过提取公共因子、展开和组合同类项，最终得到了清晰的结果。这个推导的核心是将影响输出 \(o_i\) 的部分合并在一起，最终得到简洁的形式。如果还有任何不清楚的地方，欢迎继续提问！
