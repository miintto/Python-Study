'''
==========================
3D surfaces with triangles
==========================

Plot a 3D surface with MyTri.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from MyTriangle import *

fig = plt.figure()
ax = fig.gca(projection='3d')
#ax = plt.axes(projection='3d');   ### 이렇게 사용해도 무방함

light = { 'position':[3,3,3], 'direction':[1,1,1] }

### 삼각형 만들기
v0 = Vector(1,0,0)
v1 = Vector(0,0,0)
v2 = Vector(0,0,1)
T_1 = AugTri3D(v0,v1,v2);
### 삼각형 2
v0 = Vector(2,3,0)
v1 = Vector(2,0,0)
v2 = Vector(0,2,0)
T_2 = AugTri3D(v0,v1,v2);
### 삼각형 3
v0 = Vector(0,0,1)
v1 = Vector(2,0,0)
v2 = Vector(0,2,0)
T_3 = AugTri3D(v0,v1,v2);
### 삼각형 4
v0 = Vector(1,0,1)
v1 = Vector(2,2,0)
v2 = Vector(1,3,1)
T_4 = AugTri3D(v0,v1,v2);

T_list = [T_1, T_2, T_3, T_4]

### 삼각형 하나마다 점찍기
for T in T_list:
    ### 벡터형태로 변환
    x_tri, y_tri, z_tri = [],[],[];
    for vlst in T(closed=True):
        x_tri.append(vlst[0]);
        y_tri.append(vlst[1]);
        z_tri.append(vlst[2]);

    # ax.quiver(x, y, z, u, v, w, length=0.1)   ### 화살표
    ax.plot3D(x_tri, y_tri, z_tri, 'gray')   ### 세개의 리스트 받아야 함
    ax.scatter3D(x_tri, y_tri, z_tri, c=z_tri, cmap='Greens',linewidth=0.5);

### 제목
ax.set_title('triangles');

### 화살표 제작
x = [1/3, 1/3, 1/3, 1/3]
y = [0, 0, 0, 0]
z = [1/3, 1/3, 1/3, 1/3]
u = [1,0,0,0.5]
v = [0,1,0,0.5]
w = [0,0,1,0.5]

# ax.quiver(x, y, z, u, v, w, length=0.1)   ### 화살표

plt.show()
