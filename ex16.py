# -*- coding: utf-8 -*-
# 2018.12/31

import sys

print(sys.argv)

pyscript, name = sys.argv   ### 파일 이름을 받아와서

f1 = open(name, 'r')   ### 해당 이름의 파일을 연 후

line = f1.readline()   ### 한줄씩 읽는다.
print('%r (%d)' % (line, len(line)))   ### 내용과 길이 출력
line = f1.readline()
print('%r (%d)' % (line, len(line)))
line = f1.readline()
print('%r (%d)' % (line, len(line)))
line = f1.readline()
print('%r (%d)' % (line, len(line)))
line = f1.readline()
print('%r (%d)' % (line, len(line)))
line = f1.readline()
print('%r (%d)' % (line, len(line)))
line = f1.readline()
print('%r (%d)' % (line, len(line)))
### 마지막까지 다 읽어온 후 계속 작업을 시키면 공백 ''만 받아온다. (길이는 0)
f1.close

print('Test')
f2 = open(name)
line = f2.readline()

print('%r' % line)
### 'Good Morning!\n'
print(line)   ### = 
print('%s' % line)
### Good Morning!
###
### 두 개의 차이 알아두자!!
