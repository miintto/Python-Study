# -*- coding: utf-8 -*-
# 2019.01/07


class Z:
    def __init__(self, r_val, i_val):
        self.re = r_val
        self.im = i_val

    def __add__(self, z):   ### 인스턴스 간의 '+'연산을 정의할 때 사용
        x = self.re + z.re
        y = self.im + z.im
        return Z(x, y)

    def add(self, x, y):
        self.re += x
        self.im += y
        return self

    def plus(self, z):
        self.re += z.re
        self.im += z.im
        return self

    def show(self, word=''):
        if self.im < 0:
            cc = ''
        else:
            cc = '+'
        xpyi = str(self.re)+cc+str(self.im)+'i'
        print(word+xpyi)



z = Z(1, 2)
z.show('z = ')
w = Z(3, 4)
w.show('w = ')

a = z+w   ### __add__ 로 적용시킨다.
a.show('z+w = ')

z.show('z = ')
w.show('w = ')
z.add(10, -10)
z.show('z = ')
z.plus(w).show('updated z = ')
