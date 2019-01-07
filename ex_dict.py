# -*- coding: utf-8 -*-
# 2019.01/07

### set

basket = {'apple', 'orange', 'apple', 'peach'}

print(basket)
print('apple' in basket)
print('berry' in basket)

A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}
print(A)
print(B)
print('A - B :', A - B)   ### 차집합
print('A & B :', A & B)   ### 교집합
print('A | B :', A | B)   ### 합집합
print('A ^ B :', A ^ B)   ### 대칭차집합

print({x for x in 'abcdefg' if x not in 'abc'})   ### 이런식으로 만들수도 있음

A.update('a', 'd', 'e')   ### 원소 추가 (기존에 존재하는 원소는 그대로)
print(A)
A.remove('a') ### 원소 제거
print(A)

A = set()   ### 빈 집합 (그냥 {}는 dictionary)
print(A)
A = set('abracadabra')   ### 스트링을 집어넣으면 모두 분해하여 집합 생성
print(A)
print()


### Tuple

tup = 1, 2
print(tup)
# A[0] = 3  ### 에러 (변경불가능)

a = 'string'    ### 스트링
print('a = \'string\' 이렇게 입력하면 ', type(a))
a = 'string',   ### 튜플
print('a = \'string\', 콤마를 붙이면 ', type(a))

A = (1, 2, 3)
B = (4, 5, 6)
print('A :', A)
print('B :', B)
print('A+B :', A+B)   ### 이렇게 이어붙일 순 있음
print()


### Dictionary

A = {'a':123, 'b':234, 'c':200}   ### (key : value) 쌍으로 묶여있음
print(A)

print(sorted(A))
print(list(A))
print(A.keys())
print(A.values())

A['d']=123   ### 추가 가능
del(A['a'])   ### 제거
A.pop('b')   ### 이렇게 제거할 수도 있음

A = dict([('a', 123), ('b', 234), ('c', 200)])   ### 이렇게 만들수도 있고
print(A)
A = dict(a = 123, b = 234, c = 300)   ### 이렇게 만들수도 있음
print(A)

print({x:x**2 for x in [2, 3, 4]})   ### 이렇게도 가능

A = {(1, 2):'good'}   ### key에 튜플이 들어갈 수도 있음
print(A)
print(A[(1, 2)])
A = {'a':1, 'a':2}   ### key 이름이 겹치면 안됨!!!
print(A)
### key 에 리스트나 딕셔너리는 들어갈 수 없음
### value 에는 아무거나 다 들어가도 무방


order = (1, 2, 3) < (1, 3, 0)   ### 맨 앞부더 차례로 비교한다
print(order)
order = [2, 3, 4] > [2, 3]   ### 비교할 원소가 없으면 일단 존재하는넘이 더 큼
print(order)
order = 'aB' < 'ab'   ### 문자는 ASCII 코드 순으로 비교한다.
print(order)
order = 'a'>'0'
print(order)
order = 'aAa' < 'aab' < 'ab' < 'abc'   ### 모두 성립해야 True
print(order)
order = 1 == 1.0000   ### 같은 숫자로 간주
print(order)
