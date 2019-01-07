# -*- coding: utf-8 -*-
# 2019.01/04

import numpy as np


class Triangle():
    '''
    3차원 상의 점 3개를 입력하면
    그 점이 이루는 평면의 법선벡터를 추가하여
    삼각형 오브젝트를 출력
    '''
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.set_normal_vector()

    def __repr__(self):
        pt1 = str(self.point1)
        pt2 = str(self.point2)
        pt3 = str(self.point3)
        normal_vector = str(self.normal_vector)
        return '['+pt1+', '+pt2+', '+pt3+'], normal vector = '+normal_vector

    def set_normal_vector(self):
        '''
        삼각형이 포함한 평면의 법선벡터를 계산
        '''
        x = [self.point1[i]-self.point2[i] for i in range(3)]
        y = [self.point1[i]-self.point3[i] for i in range(3)]
        self.normal_vector = list(np.cross(x, y))

    def area(self):
        '''
        세 점이 주어지면 삼각형의 넓이 계산
        '''
        vec1 = [self.point1[i]-self.point2[i] for i in range(3)]
        vec2 = [self.point1[i]-self.point3[i] for i in range(3)]
        crss_prd_vec = [i**2 for i in np.cross(vec1, vec2)]
        return np.sqrt(sum(crss_prd_vec))/2

    def reverse_vector(self):
        '''
        법선벡터의 방향을 반대로 바꿈
        '''
        self.normal_vector.x = -self.normal_vector.x
        self.normal_vector.y = -self.normal_vector.y
        self.normal_vector.z = -self.normal_vector.z

    def project(self, vector, triangle):
        '''
        주어진 벡터에 대하여 삼각형이 포함된 평면으로 정사영
        평면과 벡터가 서로 평행이면 None을 반환
        '''
        normal_vec_plane = triangle.normal_vector
        if np.dot(normal_vec_plane, vector) == 0:
            raise ValueError('정사영시킬 수 없음. (벡터와 평면이 서로 평행)')
        else:
            projected_pt = []
            for pt in [self.point1, self.point2, self.point3]:
                P_vec = [triangle.point1[i]-pt[i] for i in range(3)]
                t = np.dot(normal_vec_plane, P_vec) / np.dot(normal_vec_plane, vector)
                x, y, z = [pt[i]+vector[i]*t for i in range(3)]
                projected_pt.append([x, y, z])
            return projected_pt



def is_in_triangle(point, triangle):
    '''
    특정한 점이 주어진 삼각형 내부인지 외부인지 판별
    내부이면 True, 외부이면 False
    경계선에 걸쳐있는 경우도 내부로 간주
    '''
    pt1, pt2, pt3, normal_vec = triangle

    vec1 = [pt1[i]-point[i] for i in range(3)]
    vec2 = [pt2[i]-point[i] for i in range(3)]
    vec3 = [pt3[i]-point[i] for i in range(3)]

    prd1 = innr_prd(vec1, vec2)
    prd2 = innr_prd(vec2, vec3)
    prd3 = innr_prd(vec3, vec1)

    if (abs(innr_prd(vec1, normal_vec)) > 1.0e-8) | (abs(innr_prd(vec2, normal_vec)) > 1.0e-8):
        raise ValueError('Error : 해당 점과 삼각형이 동일 평면상에 있지 않음.')
    elif ((prd1>0) & (prd2>0)) | ((prd2>0) & (prd3>0)) | ((prd3>0) & (prd1>0)):
        return False
    else:
        return True




T1 = Triangle([3, 0, 0], [0, 4, 0], [0, -1, 0])
T2 = Triangle([2, 2, 3], [2, 0, 5], [-3, 0, 7])
print('triangle1 :', T1)
print('triangle2 :', T2)
print()

light = [0, 0, -1]
x, y, z = T2.project(light, T1)
T3 = Triangle(x, y, z)
print(T3)
print(T1.area())
print(T2.area())
print(T3.area())
