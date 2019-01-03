# -*- coding: utf-8 -*-
# 2019.01/02

'''
    원하는 숫자와 자릿수를 입력하면
    해당 숫자를 2진법 변환시의 자릿수를 출력한다.
'''

def find_binary_bit(num, n):
    while n >= 0:
        R = num % 2
        Q = num // 2
        n -= 1
        num = Q
    return R
