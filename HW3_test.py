# -*- coding: utf-8 -*-
# 2019.01/03

from HW3_1_Differential import *
from HW3_2_Sorting import *
from HW3_3_FindBit_2 import *


### Test

line = '2+3x+5x^2+6x^4+x^5'
print('\nDifferentiation')
print('f(x) =', line)
print('f\'(1) = %r' % diff_int(line, 1))


print('\nSorting')
sort_sel([5, 2, 1, 3, 4])
sort_sel([10, 8, 7, 5, 2, 11, 1])
sort_sel([2, 4, 1, 5, 7, 8, 6, 10, 3, 0])
sort_sel([20, 18, 16, 13, 10, 11, 7, 6, 4, 1])
sort_bub([5, 2, 1, 3, 4])
sort_bub([10, 8, 7, 5, 2, 11, 1])
sort_bub([2, 4, 1, 5, 7, 8, 6, 10, 3, 0])
sort_bub([20, 18, 16, 13, 10, 11, 7, 6, 4, 1])


print('\nFind binary bit')
n = int(input('정수를 입력하시오 : '))
i = int(input('시작할 비트 자릿수 : '))
j = int(input('마지막 비트 자릿수 : '))
print(find_binary_numbers(n, i, j))