# -*- coding: utf-8 -*-
# 2019.01/03

from random import *


def is_updown(num, target):
    if num < target:
        print('Go Up!')
        return 1
    elif num > target:
        print('Go Down!')
        return 1
    else:
        print('Good Job~!')
        return 0

answer = randint(1, 100)
count = 1

while True:
    n = input('Number : ')
    token = is_updown(int(n), answer)
    if token != 0:
        count += token
    else:
        print('You gave the answer %d in %d times' % (answer, count))
        break


### 과제 1 : 다항식의 미분식을 계산
### input : '1-4x^2+3x^3' 의 미분식 계산...

### 과제 2 : 리스트에서 오름차순으로 정렬될때 까지 횟수 카운트
### input : [3, 5, 8, 1, ...] 임의의 리스트

### 과제 3 : 임의의 정수의 i번째 bit와 j번째 bit 사이의 읽어내는 함수
