import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
phi = np.linspace(0,2* np.pi, 100) 
theta = np.linspace(0, np.pi, 100)  
theta, phi = np.meshgrid(theta, phi)

# 创建网格
theta, phi = np.meshgrid(theta, phi)

# 计算球面上的笛卡尔坐标 (x, y, z)
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# 计算矢量场（单位矢量）
# 由于我们是绘制单位球面矢量场，每个矢量的方向就是球面上的坐标点
u = x  # x 方向的分量
v = y  # y 方向的分量
w = z  # z 方向的分量

# 创建图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制单位球面矢量场
ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True, color='r', alpha=0.5)

# 绘制球面
ax.plot_surface(x, y, z, color='b', alpha=0.1, rstride=10, cstride=10)

# 设置图形标题和标签
ax.set_title('Unit Sphere Vector Field')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

