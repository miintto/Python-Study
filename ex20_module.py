# -*- coding: utf-8 -*-
# 2019.01/03

### Function을 만드는 두 가지 방법
myfun = lambda x, y: x+y

def myfun_2(x, y):
    return x+y
### 와 같은 의미

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

def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b
    print()

def separate(sen):
    '''
    문장을 입력받아 띄어쓰기 간격으로 분리
    '''
    wds = sen.split(' ')
    whatwewant = [wd for wd in wds if wd != '']   ### 띄어쓰기 두번으로 생긴  blank제거
    return whatwewant

def first_word(sen):
    wds = separate(sen)
    word = wds.pop(0)
    ### pop : 리스트의 n번째 인자를 return
    ### -> index of list : [0, 1, 2, ... -1] 0부터 시작, 마지막은 -1로 뽑아낼 수 있음
    print(word)

def last_word(sen):
    wds = separate(sen)
    word = wds.pop(-1)
    print(word)

def first_last(sen):
    wds = separate(sen)
    return wds.pop(0), wds.pop(-1)
