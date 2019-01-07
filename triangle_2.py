# -*- coding: utf-8 -*-
# 2019.01/04

from vector import Vec3D


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
        x = self.point1-self.point2
        y = self.point1-self.point3
        self.normal_vector = x.cross(y)

    def area(self):
        '''
        세 점이 주어지면 삼각형의 넓이 계산
        '''
        vec1 = self.point1-self.point2
        vec2 = self.point1-self.point3
        return abs(vec1.cross(vec2))/2

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
        if normal_vec_plane*vector == 0:
            raise ValueError('정사영시킬 수 없음. (벡터와 평면이 서로 평행)')
        else:
            projected_pt = []
            for pt in [self.point1, self.point2, self.point3]:
                t = (normal_vec_plane*(triangle.point1-pt)) / (normal_vec_plane*vector)
                projected_pt.append(pt+vector*t)
            return projected_pt



def is_in_triangle(point, triangle):
    '''
    특정한 점이 주어진 삼각형 내부인지 외부인지 판별
    내부이면 True, 외부이면 False
    경계선에 걸쳐있는 경우도 내부로 간주
    '''
    vec1 = triangle.point1-point
    vec2 = triangle.point2-point
    vec3 = triangle.point3-point

    prd1 = vec1*vec2
    prd2 = vec2*vec3
    prd3 = vec3*vec1

    if (abs(vec1*triangle.normal_vector) > 1.0e-8) | (abs(vec2*triangle.normal_vector) > 1.0e-8):
        raise ValueError('Error : 해당 점과 삼각형이 동일 평면상에 있지 않음.')
    elif ((prd1>0) & (prd2>0)) | ((prd2>0) & (prd3>0)) | ((prd3>0) & (prd1>0)):
        return False
    else:
        return True



T1 = Triangle(Vec3D(3, 0, 0), Vec3D(0, 4, 0), Vec3D(0, -1, 0))
T2 = Triangle(Vec3D(2, 2, 3), Vec3D(2, 0, 5), Vec3D(-3, 0, 7))
print('triangle1 :', T1)
print('triangle2 :', T2)
print(T1.area())
print(T2.area())

light = Vec3D(0, 0, -1)
x, y, z = T2.project(light, T1)
T3 = Triangle(x, y, z)
print(T3)

print(is_in_triangle(T3.point1, T1))