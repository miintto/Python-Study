# -*- coding: utf-8 -*-
# 2018.12/31

import sys
from os.path import exists   ### 해당 파일이 존재하는지 여부 파악

print(sys.argv)

pyscript, name = sys.argv   ### 이름을 입력받아

print('File exist : %r' % exists(name))   ### 해당 파일의 존재여부 확인

f1 = open(name, 'r')   ### 그 파일을 읽기모드로 실행

another = input('Name : ')   ### 다른 이름을 입력받아서
f2 = open(another, 'w')   ### 쓰기 형식으로 파일을 열고 (혹은 새로 반들고)
line = '\n'
while len(line)>0:
    line = f1.readline()   ### 첫번째 파일을 한줄씩 읽어서
    f2.write()   ### 두번째 파일에 입력
f2.close()
