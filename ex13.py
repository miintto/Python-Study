# -*- coding: utf-8 -*-
# 2018.12/31

import sys

print(sys.argv)
### type : 리스트
###    -> 커맨드창에서 인자를 받아올 수 있도록 한다, 띄어쓰기로 구분하는듯
### ex)
### >>> python3 ex13.py name1 name2 ...  이런 식으로 사용할 수 있음
### sys.argv = ['ex13.py', 'name1', 'name2', ..]   이렇게 리스트형태로 저장된다.
### 리스트에서 제일 처음은 실행시키는 파일 이름, 그 뒤는 입력받은 문자를 포함하는 리스트

pyscript, first, second, third = sys.argv

print(pyscript) ### 실행한 python 파일 이름
print(first, type(first))   ### 무조건 스트링으로 처리한다.
print(second, type(second))
print(third, type(third))

print(int(first)+int(second)+int(third))   ### 이렇게 할 수도 있음
