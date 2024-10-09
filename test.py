import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D
#绘制三维图像
#转化成矩阵
x1=np.random.randint(-150,150,size=(300,1))
x2=np.random.randint(0,300,size=(300,1))
#斜率和截距，随机生成
w=np.random.randint(1,5,size=2)
b=np.random.randint(1,10,size=1)
y=x1*w[0]+x2*w[1]+b+np.random.randn(300,1)
fig=plt.figure(figsize=(9,6))
ax=Axes3D(fig)
ax.scatter(x1,x2,y)#三维散点图
ax.view_init(elev=10,azim=-20)#调整视角

plt.show()