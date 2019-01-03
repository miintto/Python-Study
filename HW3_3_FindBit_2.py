# -*- coding: utf-8 -*-
# 2019.01/03

from HW2_FindBit import find_binary_bit


def find_binary_numbers(n, i, j):
    bits = ''
    for idx in range(i, j+1)[::-1]:
        bits += str(find_binary_bit(n, idx))
    return bits