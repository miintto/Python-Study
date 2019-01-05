# -*- coding: utf-8 -*-
# 2019.01/04

import numpy as np


def innr_prd(vec1, vec2):
	'''
	3차원 상의 두 벡터를 입력하면
	두 벡터의 내적을 계산
	'''
	return sum([vec1[i]*vec2[i] for i in range(3)])


def crss_prd(vec1, vec2):
	'''
	3차원 상의 두 벡터를 입력하면
	두 벡터의 외적을 계산
	'''
	i = vec1[1]*vec2[2] - vec1[2]*vec2[1]
	j = vec1[2]*vec2[0] - vec1[0]*vec2[2]
	k = vec1[0]*vec2[1] - vec1[1]*vec2[0]

	return [i, j, k]


def form_triangle(vec1, vec2, vec3):
	'''
	3차원 상의 점 3개를 입력하면
	그 점이 이루는 평면의 법선벡터를 추가하여
	삼각형 오브젝트를 출력
	'''
	x = [vec1[i]-vec2[i] for i in range(3)]
	y = [vec1[i]-vec3[i] for i in range(3)]

	return	[vec1, vec2, vec3, crss_prd(x, y)]


def proj_pt(point, vec, triangle):
	'''
	특정한 점을 주어진 벡터에 대하여
	삼각형이 포함된 평면으로 정사영
	평면과 벡터가 서로 평행이면 None을 반환
	'''
	normal_vec = triangle[3]
	if innr_prd(normal_vec, vec) == 0:
		return None
	else:
		P_vec = [triangle[0][i]-point[i] for i in range(3)]
		t = innr_prd(normal_vec, P_vec) / innr_prd(normal_vec, vec)
		x, y, z = [point[i]+vec[i]*t for i in range(3)]
		return [x, y, z]


def is_in_triangle(point, triangle):
	'''
	점이 주어진 삼각형 내부인지 외부인지 판별
	내부이면 True, 외부이면 False
	'''
	pt1, pt2, pt3, normal_vec = triangle

	vec1 = [pt1[i]-point[i] for i in range(3)]
	vec2 = [pt2[i]-point[i] for i in range(3)]
	vec3 = [pt3[i]-point[i] for i in range(3)]

	prd1 = innr_prd(vec1, vec2)
	prd2 = innr_prd(vec2, vec3)
	prd3 = innr_prd(vec3, vec1)

	if (abs(innr_prd(vec1, normal_vec)) > 0.00000001) | (abs(innr_prd(vec2, normal_vec)) > 0.00000001):
		print('Error : The point is not at the SAME plane')
		return False
	elif ((prd1>0) & (prd2>0)) | ((prd2>0) & (prd3>0)) | ((prd3>0) & (prd1>0)):
		return False
	else:
		return True


def area_triangle(triangle):
	pt1, pt2, pt3, normal_vec = triangle
	vec1 = [pt1[i]-pt2[i] for i in range(3)]
	vec2 = [pt1[i]-pt3[i] for i in range(3)]
	crss_prd_vec = [i**2 for i in crss_prd(vec1, vec2)]
	return np.sqrt(sum(crss_prd_vec))/2



T1 = form_triangle([3, 0, 0], [0, 4, 0], [0, -1, 0])
T2 = form_triangle([2, 2, 3], [2, 0, 5], [-3, 0, 7])
print('triangle1 : %r' % T1)
print('triangle2 : %r' % T2)
print()

light = [0, 1, -1]

T3 = []
print('light : ', light)
print('삼각형 T1을 T2가 포함된 평면으로 정사영')
for point in T1[:-1]:
    projected_pt = proj_pt(point, light, T2)
    print('%r -> %r' % (point, projected_pt))
    print('In triangle :', is_in_triangle(projected_pt, T2))
    T3.append(projected_pt)

T3 = form_triangle(T3[0], T3[1], T3[2])
print('New Triangle :', T3)
print('T1 의 넓이 :', area_triangle(T1))
print('T2 의 넓이 :', area_triangle(T2))
print('T3 의 넓이 :', area_triangle(T3))
