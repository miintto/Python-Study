# -*- coding: utf-8 -*-
# 2019.01/04


list_a = [10, 'a', [1, 2, 3], 'Happy New Year!', 3.14, 'anything']
print('current list_a : %r ' % list_a)
print()

print('0-th : %r' % list_a[0])
print('1-th : %r' % list_a[1])
print('2-th : %r' % list_a[2])
print('(-1)-th : %r' % list_a[-1])
print('(-3)-th : %r' % list_a[-3])
print()

content = list_a.pop()   ### default는 맨 마지막
print('popped element : %r' % content)
print('current list_a : %r' % list_a)

content = list_a.pop(2)
print('popped element : %r' % content)
print('current list_a : %r' % list_a)

list_a[-1] = 1.256
print('changed list_a : %r' % list_a)

list_a.append(100)
print('changed list_a : %r' % list_a)
list_a.append('sin(x)')
print('changed list_a : %r' % list_a)

print(id(list_a))
list_a.insert(2, 'Hi')   ### 이렇게 도중에 삽입할 수고 있다.
print('changed list_a : %r' % list_a)
print(id(list_a))

elm = 'Hi'
try:
    where = list_a.index(elm)
    print('%r is located %d-th' %(elm, where))
except ValueError:
    print('The value is not in the list.')
except RuntimeError:
    print('Runtime error!')
except NameError:
    print('Name error!')
except OSError:
    print('OS error!')
except:
    print('There occurs another error!')
finally:
    print('Done\n')

print('changed list_a : %r' % list_a)
print('list_a[:3] : ', list_a[:3])
print('list_a[2:] : ', list_a[2:])
print('list_a[2:5] : ', list_a[2:5])
print('Length of list : ', len(list_a))

del(list_a[2])   ### 제거
print('current list_a : %r' % list_a)
print()

list_b = ['tiger', '2', 'banana', '0', 'monkey', 'dragon']
print('current list_b : %r' % list_b)
sss = ' '.join(list_b)   ### ' '을 사이에 끼워넣어서 리스트를 스트링으로 변환
print('%r' % sss)
sss = '\n%'.join(list_b)
print('%r' % sss)
print('%s' % sss)
