# -*- coding: utf-8 -*-
# 2019.01/04


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



T1 = form_triangle([2, 0, 0], [-1, 3, 0], [0, 0, 4])
T2 = form_triangle([2, 0, 0], [-1, 3, 0], [0, -1, 0])
print('triangle1 : %r\n' % T1)
print('triangle2 : %r\n' % T2)

light = [0, 0, 1]

print('light : ', light)
print('옯겨진 좌표 : ')
for point in T1[:-1]:
	print(proj_pt(point, light, T2), end = ' ')
