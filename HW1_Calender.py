# -*- coding: utf-8 -*-
# 2018.12/31

month = input('해당 월 : ')
wkday = input('해당 요일 : ')
last_day = input('마지막 날짜 : ')

print('\n      '+month+'월 달력\n')
print('일 월 화 수 목 금 토')

n = '일월화수목금토'.find(wkday)
print('   '*n, end = '')

for i in range(int(last_day)):
    if i<9:
        print(' %d' % (i+1), end=' ')
    else:
        print('%d' % (i+1), end=' ')
    if i%7==(6-n):
        print('')
print('')
