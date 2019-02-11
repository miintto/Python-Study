#-*- coding: utf-8 -*-

import sys, math, functools

# interesting functions

def power(n):

    def compute(x):
        prod = 1
        for _ in range(n):
            prod *= x
        return prod

    return compute   ### 함수를 return 가능


def do_this(fun):   ### 함수를 받아서
    val = fun(4)   ### 함수에 4 대입 (대신 4를 input으로 받을수 있는 fun만 가능)
    return val


def do_this_smart(fun):
    def running(*ags, **kws):   ### 이렇게 여러 인자를 받아서
        val = fun(*ags, **kws)   ### 그걸 계산하고
        return val   ### 결과를 출력
    return running   ### 하는 함수를 출력  (사실살 그냥 fun()과 똑같은 기능...)


def fun_1(x):
    return x * x

def fun_2(x, y):
    return x * y


def setunit(unit):
    def reflecting(fun):
        fun.unit = unit   ### def 밖에서 함수에 변수를 지정해줄 수 있음
        return fun
    return reflecting


# decorators

def decoration(fun):
    '''decoration house'''   ### Docstring : decoration.__doc__ 으로 출력

    @functools.wraps(fun)
    def wrapping_fun(*ags, **kvs):
        print('<< wrapping-pre >>')
        rtv = fun(*ags, **kvs)
        print('<< wrapping-post >>')
        return rtv

    return wrapping_fun


@decoration
# another가 decoration이랑 같이 실행됨
# 여기서는 decoration이 함수지만, class로도 된다.
# 밑에있는 첫번째 함수에만 작동
# 한 줄마다 @로 여러개의 decoration이 가능함.
# 밑에 있는 decoration부터 실행됨
def another(x, y, z):
    print('더할 숫자들은 = ', x, y, z)
    return x + y + z

def sample_1(x, y, z):
    print('더할 숫자들은 : ', x, y, z)
    return x + y + z

def sample_2(x, y, z):
    print('곱할 숫자들은 = ', x, y, z)
    return x * y * z

@setunit('cm')
def sample_3(x, y, z):
    return x * y * z

if __name__ == '__main__':
    pw = power(3);   ###  pw(x) = x^3
    print('pw(2) =', pw(2))

    print('do_this(fun_1) =', do_this(fun_1))   ### 4*4

    myfun = do_this_smart(fun_2)
    print(myfun(4, 5))
    print(fun_2(4, 5), '\n')   ### 결과가 같다.


# decoration test

    print(another(1, 2, 3), '\n')

    sample_1 = decoration(sample_1)
    print(sample_1(1, 2, 3), '\n')   ### 얘랑 같은 효과임

    sample_2 = setunit('cm')(sample_2)
    print(sample_2(3, 4, 5), sample_2.unit)

    print(sample_3(3, 4, 5), sample_3.unit, '\n')
