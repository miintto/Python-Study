# -*- coding: utf-8 -*-
# 2019.01/02

### Function2

def ops(x, y):
    print('\nBasic Operators')
    print('%r + %r = %r' % (x, y, x+y))
    print('%r - %r = %r' % (x, y, x-y))
    print('%r * %r = %r' % (x, y, x*y))
    print('%r ** %r = %r' % (x, y, x**y))
    print('%r %% %r = %r' % (x, y, x%y))   ### 나머지
    print('%r / %r = %r' % (x, y, x/y))
    print('%r // %r = %r' % (x, y, x//y))   ### 나누기 몫
    print('\nBitwise Operators')
    ### 비트에서 제일 앞은 부호 나머지는 2의 거듭제곱
    ### ~ : 비트의 숫자를 모두 다 반대로 (1->0, 0->1) -> ( ~x = -(x+1) )
    ### and : 0&0=0 0&1=0 1&0=0 1&1=1
    ### or : 0&0=0 0&1=1 1&0=1 1&1=1
    ### << n : 숫자들을 오른쪽으로 n칸 이동 (101101 << 2 : 110100)
    print('~%r = %r' % (x, ~x))
    print('~%r = %r' % (y, ~y))
    print('%r & %r = %r' % (x, y, x & y))
    print('%r | %r = %r' % (x, y, x | y))
    print('%r << %r' % (x, x << 2))
    print('%r >> %r' % (x, x >> 2))
    print('\nBrief Operatots')
    xs, ys = x, y
    x += y
    print('(x = %r, y = %r) --> x+=y --> x = %r' % (xs, ys, x))
    x, y = xs, ys
    x -= y
    print('(x = %r, y = %r) --> x-=y --> x = %r' % (xs, ys, x))
    x, y = xs, ys
    x *= y
    print('(x = %r, y = %r) --> x*=y --> x = %r' % (xs, ys, x))
    x, y = xs, ys
    x /= y
    print('(x = %r, y = %r) --> x/=y --> x = %r' % (xs, ys, x))
    x, y = xs, ys
    x //= y
    print('(x = %r, y = %r) --> x//=y --> x = %r' % (xs, ys, x))
    x, y = xs, ys
    x %= y
    print('(x = %r, y = %r) --> x%%=y --> x = %r' % (xs, ys, x))
    print()

def sum(*num):
    total = 0
    for i in num:
        total+=float(i)
    return total

def boolalgebra(x, y):
    print('x = %r, y = %r' % (x, y))
    print('not x = %r' % (not x))
    print('x or y = %r' % (x or y))
    print('x and y = %r' % (x and y))
    print()

def parts(num):
    head = num//1
    tail = num - head
    return int(head), tail


### test Function

ops(7, 3)
print('sum(1, 2, 3, 4) = %d' % sum(1, 2, 3, 4))
print()

print('x = True, y = False')
boolalgebra(True, False)

print('x = 1<2, y = 1+2==5')
boolalgebra(1<2, 1+2==5)

print('x = (False==0), y = (True==1)')
boolalgebra(False==0, True==1)

print('x = 1, y = 0')
boolalgebra(1, 0)

x = -3.1415926535
n, alpha = parts(x)
print('%r = %r + %r' % (x, n, alpha))
