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
        self.points_set = [self.point1, self.point2, self.point3]
        self.set_normal_vector()

    def __repr__(self):
        points_set = str(self.points_set)
        normal_vector = str(self.normal_vector)
        return points_set+', normal vector = '+normal_vector

    def set_normal_vector(self):
        '''
        삼각형이 포함한 평면의 법선벡터를 계산
        '''
        vec1 = self.point1-self.point2
        vec2 = self.point1-self.point3
        self.normal_vector = vec1.cross(vec2)

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
        self.normal_vector = -self.normal_vector

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
            for pt in self.points_set:
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

def inter(point1, point2, point3, point4):
    '''
    선분 point1 point2와 선분 point3 point4의 교점을 출력
    '''
    vec1 = point2-point1
    vec2 = point4-point3
    if vec1.x*vec2.y==vec2.x*vec1.y:
        return None
    else:
        t = vec2.cross(point1-point3).z / vec1.cross(vec2).z
        inter_pt = point1 + vec1*t
        bool_1 = min(point1.x, point2.x)-1.0e-8 <= inter_pt.x <= max(point1.x, point2.x)+1.0e-8
        bool_2 = min(point1.y, point2.y)-1.0e-8 <= inter_pt.y <= max(point1.y, point2.y)+1.0e-8
        bool_3 = min(point3.x, point4.x)-1.0e-8 <= inter_pt.x <= max(point3.x, point4.x)+1.0e-8
        bool_4 = min(point3.y, point4.y)-1.0e-8 <= inter_pt.y <= max(point3.y, point4.y)+1.0e-8
        if bool_1 & bool_2 & bool_3 & bool_4:
            return inter_pt
        else:
            return None

'''
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


'''