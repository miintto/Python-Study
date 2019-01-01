# -*- coding: utf-8 -*-
# 2018.12/28

### 변수에 대하여

a = 10
b = 20
print(a, type(a))   ### 자동적으로 integer
print(b, type(b))

abc = 3.14
print('abc = %f' % abc)
print(abc, type(abc))   ### 자동적으로 float

x20 = 'xyz1234'
y_30 = 'wxy5678'
print(x20, type(x20))   ### string
print(y_30, type(y_30))
print(x20+y_30)

n = 20
w = '+-'*n
print(w)
print('+-'*20)   ### 이렇게 할수도 있음...

my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print("I got %s eyes, %s hair, and my teeth are usually %s" % (my_eyes, my_hair, my_teeth))

sss = "I got %s eyes, %s hair, and my teeth are usually %s" % (my_eyes, my_hair, my_teeth)
print(sss)   ### 이렇게 해도 무방함
