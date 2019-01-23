#-*- coding: utf-8 -*-

import sys, math, functools

# interesting functions

def power(n):

    def compute(x):
        prod = 1;
        for k in range(n): prod *= x;
        return prod;

    return compute;
    # return 함수 가능

def do_this(fun):
    val = fun(4);
    return val;

def do_this_smart(fun):
    def running(*ags, **kws):
        val = fun(*ags, **kws);
        return val;
    return running;

def fun_1(x):
    return x * x;

def fun_2(x, y):
    return x * y;

# decorators

def decoration(fun):

    '''decoration house'''
    # print(decoration.__doc__); -> 함수안에 있는 script가 출력됨

    @functools.wraps(fun)
    def wrapping_fun(*ags, **kvs):
        print('wrapping-pre');
        rtv = fun(*ags, **kvs);
        print('wrapping-post');
        return rtv;

    return wrapping_fun;

def setunit(unit):
    def reflecting(fun):
        fun.unit = unit;
        # def 밖에서 함수에 변수를 지정해줄 수 있음
        return fun;
    return reflecting;

def sample_1(x, y):
    print('args in sample_1 = ', x, y);
    return x + y;

def sample_2(x, y, z):
    print('args in sample_2 = ', x, y, z);
    return x * y * z;

@decoration
# another가 decoration이랑 같이 실행됨
# 여기서는 decoration이 함수지만, class로도 된다.
# 밑에있는 첫번째 함수에만 작동
# 한 줄마다 @로 여러개의 decoration이 가능함.
# 밑에 있는 decoration부터 실행됨
def another(x, y, z):
    print('args in another function = ', x, y, z);
    return x + y + z;

@setunit('cm')
def sample_3(x, y, z):
    return x * y * z;

if __name__ == '__main__':
    pw = power(3);
    print(pw(2));

    print(do_this(fun_1));

    myfun = do_this_smart(fun_2);
    print(myfun(4, 5), '\n');

# decoration test

    sample_1 = decoration(sample_1);
    print(sample_1(1, 2), '\n');

    print(another(1, 2, 3), '\n');

    sample_2 = setunit('cm')(sample_2);
    print(sample_2(3, 4, 5), sample_2.unit, '\n');

    print(sample_3(3, 4, 5), sample_3.unit);
