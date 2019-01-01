# -*- coding: utf-8 -*-    파이썬이 한글도 받아들일수 있도록...
# 2018.12/28

print('Hello, World!')
print('안녕하세요')

print('암탉 %f 수탉 %f' % (15+1/2, 1/3))
### Format
### %f : 소수점   %d : 정수   %s : 문자열

print(22%5)  ### 나머지
print(2+2*2)
print(2+3 < 5-2)   ### boolen도 출력

print('이렇게', end=' ');print('이을수있음ㅋ')
print('This %r' % (1==2))
print('This %r' % (3<5))



age = input('나이를 입력하시오 : ')
print('내 나이는 %d살' % int(age))
print('내 나이는 %s살' % age)
print('내 나이는 '+age+'살')
