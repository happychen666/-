# 使用调整后的正确符号绘制图像

# 原始主成分和次成分向量
v1_original = np.array([0.6, 0.8])
v2_original = np.array([-0.8, 0.6])

# 符号调整后的主成分和次成分向量
v1_adjusted = np.array([0.6, 0.8])
v2_adjusted = np.array([0.8, -0.6])

# 绘制图形
plt.figure(figsize=(8, 6))

# 原始主成分和次成分
plt.quiver(0, 0, v1_original[0], v1_original[1], angles='xy', scale_units='xy', scale=1, color='b', label="Original First PC (v1)")
plt.quiver(0, 0, v2_original[0], v2_original[1], angles='xy', scale_units='xy', scale=1, color='r', label="Original Second PC (v2)")

# 符号调整后的主成分和次成分
plt.quiver(0, 0, v1_adjusted[0], v1_adjusted[1], angles='xy', scale_units='xy', scale=1, color='g', label="Adjusted First PC (v1)")
plt.quiver(0, 0, v2_adjusted[0], v2_adjusted[1], angles='xy', scale_units='xy', scale=1, color='orange', label="Adjusted Second PC (v2)")

# 设置图形的范围和样式
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')

# 添加标签和图例
plt.legend()
plt.title("Comparison of Principal Components Before and After Sign Adjustment")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# 显示图形   
plt.show() 
