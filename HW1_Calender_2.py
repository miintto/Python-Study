# -*- coding: utf-8 -*-
# 2018.12/31

'''
    - 해당 월과 요일을 입력하면 자동으로 달력을 생성
    - 월은 1 ~ 12사이에서만 입력받음
    - 요일은 일 ~ 토 사이에서 입력받음
        ('목', '목요일' 두 형식 모두 무방함)
    - 월을 입력하면 일수는 자동으로 조정
        (2월일 때만 입력받음)
'''

month = input('해당 월 : ')
while(int(month) not in range(1, 13)):
    month = input('1~12 에서 선택하시오 : ')
    
wkday = input('해당 요일 : ')
while(wkday[0] not in '일월화수목금토'):
    wkday = input('월~일 에서 선택하시오 : ')

if int(month) == 2:
    last_day = input('마지막 날짜 : ')
elif int(month) in [1, 3, 5, 7, 8, 10, 12]:
    last_day = 31
else:
    last_day = 30

print('\n      '+month+'월 달력\n')
print('일 월 화 수 목 금 토')

n = '일월화수목금토'.find(wkday[0])
print('   '*n, end = '')

for i in range(int(last_day)):
    if i<9:
        print(' %d' % (i+1), end=' ')
    else:
        print('%d' % (i+1), end=' ')
    if i%7==(6-n):
        print('')
print('')
