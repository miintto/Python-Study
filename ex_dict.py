# -*- coding: utf-8 -*-
# 2019.01/07

### set

basket = {'apple', 'orange', 'apple', 'peach'}

basket
'apple' in basket
'berry' in basket

A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}

A-B
A&B
A|B
A^B
{x for x in 'abcdef' if x not in 'abc'}

A.update('a', 'c', 'd')
A.remove('a')

A = set()   ### 빈 집합
A = set('abracadabra')



### Tuple

A = 1, 2
# A[0] = 3  ### 에러 (변경불가능)

a = 'string'    ### 스트링
a = 'string',   ### 튜플



### Dictionary

A = {'a':123, 'b':234, 'c':200}   ### key:value
print(A)

A['d']=123   ### 추가 가능
del(A['a'])   ### 제거
A.pop('a')

sorted(A)
list(A)
A.keys()
A.values()
### key 에는 리스트나 딕셔너리는 들어갈 수 없음
### value 에는 아무거나 다 들어가도 무방

A = dict([('a', 123), ('b', 234), ('c', 200)])   ### 이렇게 만들수도 있고
A = dict(a = 123, b = 234, c = 300))   ### 이렇게 만들수도 있음

{x:x**2 for x in [2, 3, 4]}

A = {'a':1, 'a':2}


order = (1, 2, 3) < (1, 3, 0)
order = [2, 3, 4] > [2, 3]
order = 'aB'>'ab'
order = 'a'>'0'
order = 'aaa'<'abb'<'abc'
order = 1 == 1.0000
