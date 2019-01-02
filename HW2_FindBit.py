# -*- coding: utf-8 -*-
# 2019.01/02

'''
    원하는 숫자와 자릿수를 입력하면
    해당 숫자를 2진법 변환시의 자릿수를 출력한다.
'''

def find_binary_bit(num, n):
    while n > 0:
        R = num % 2
        Q = num // 2
        n -= 1
        num = Q
    return R


print('101의 1번째 비트는', find_binary_bit(101, 1))
print('101의 2번째 비트는', find_binary_bit(101, 2))
print('101의 3번째 비트는', find_binary_bit(101, 3))
print('101의 4번째 비트는', find_binary_bit(101, 4))
print('101의 5번째 비트는', find_binary_bit(101, 5))
print('101의 6번째 비트는', find_binary_bit(101, 6))
print('101의 7번째 비트는', find_binary_bit(101, 7))
print('101의 8번째 비트는', find_binary_bit(101, 8))
