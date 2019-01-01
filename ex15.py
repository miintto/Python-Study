# -*- coding: utf-8 -*-
# 2018.12/31

import sys

print(sys.argv)

pyscript, name1, name2 = sys.argv   ### 두 개의 이름을 받아와서

f1 = open(name1, 'r')    ### 첫번째 이름의 파일을 읽기모드로 불러온 후
cont1 = f1.read()   ### 담긴 내용을 읽고
print(cont1)   ### 출력한다.
f1.close()

f2 = open(name2, 'w')   ### 두번째 이름의 파일을 쓰기모드로 불러와서
f2.write(cont1)   ### 첫번째 파일 내용을 덮어쓴다.
f2.close()

### copy 기능
