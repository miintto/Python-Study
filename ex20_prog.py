# -*- coding: utf-8 -*-
# 2019.01/03

# import ex20_module   ### 모듈 가져오기
import ex20_module as ex20
### 처럼 모듈 이름을 간략하게 재설정 할 수도 있음

# from ex20_module import myfun
### 이런식으로 함수 개별적으로 가져올 수 있음...
### 혹은 import * (모든 함수 불러오기)
### 대신 함수를 실핼할 때에는 myfun으로 실행!


print('lambda function :', ex20.myfun(2, 3))

ex20.ops(7, 3)
print('sum(1, 2, 3, 4) = %d' % ex20.sum(1, 2, 3, 4))
print()

print('x = True, y = False')
ex20.boolalgebra(True, False)

print('x = 1<2, y = 1+2==5')
ex20.boolalgebra(1<2, 1+2==5)

print('x = (False==0), y = (True==1)')
ex20.boolalgebra(False==0, True==1)

print('x = 1, y = 0')
ex20.boolalgebra(1, 0)

x = -3.1415926535
n, alpha = ex20.parts(x)
print('%r = %r + %r' % (x, n, alpha))

ex20.fibo(1000)

line = 'Hello Everybody Good Morning~!'
ex20.first_word(line)
ex20.last_word(line)
first, last = ex20.first_last(line)
print('The first word is %r and the last word is %r' % (first, last))
