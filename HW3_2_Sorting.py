# -*- coding: utf-8 -*-
# 2019.01/03


def sort_sel(lst):
    '''
    Selection Sorting
    '''
    count = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                count +=1
    print('결과 : %r\n%d 회 계산.' % (lst, count))


def sort_bub(lst):
    '''
    Bubble Sorting
    '''
    count = 0
    for i in range(len(lst))[::-1]:
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                count +=1
    print('결과 : %r\n%d 회 계산.' % (lst, count))
