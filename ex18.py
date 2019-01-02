# -*- coding: utf-8 -*-
# 2019.01/02

### Function

def myprint_1(*ags):
    ### * 이 붙어있으면 여러개의 인자를 받아올 수 있음
    ag1, ag2 = ags   ### unpacking
    print('%r %r' % (ag1, ag2))

def myprint_2(arg1, arg2):
    print('%r %r' % (arg1, arg2))

def myprint_3(arg):
    print('%r' % arg)

def myprint_4():
    print('No Argument.')

myprint_1('Kim', 'Lee')
myprint_1('Kim', 1)
myprint_2('Kim', 'Lee')
myprint_3('Kim')
myprint_4()
