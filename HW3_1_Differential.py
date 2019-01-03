# -*- coding: utf-8 -*-
# 2019.01/03


def sep_poly(line):
    '''
    다항식에서 각 항을 분리
    '''
    line = line.replace('+', ' +')
    line = line.replace('-', ' -')
    line = line.replace('+x', '+1x')
    line = line.replace('-x', '-1x')
    return line.split(' ')

def sep_expo(string):
    '''
    단항식에서 계수와 지수를 분리
    '''
    if 'x' not in string:
        return string, 0
    elif '^' in string:
        coef, expo = string.split('^')
        coef = coef
        return coef.replace('x', ''), expo
    else:
        return string.replace('x', ''), 1

def diff_int(line, value):
    '''
    다항식을 항 별로 쪼개에 미분,
    주어진 값을 대입하여 미분계수 계산
    '''
    sum_diff = 0
    for string in sep_poly(line):
        coef, expo = sep_expo(string)
        if expo==0:
            pass
        else:
            sum_diff += (int(coef)*int(expo))*(value**(int(expo)-1))
    return sum_diff
