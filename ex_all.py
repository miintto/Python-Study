# -*- coding: utf-8 -*-
# 2019.01/14


class Complex:
    '''Complex Class Definition'''
    def __init__(self, x=0, y=0):
        self.re = x
        self.im = y

    def add(self, z):
        x = self.re + z.re
        y = self.im + z.im
        return Complex(x, y)

    def __add__(self, z):
        x = self.re + z.re
        y = self.im + z.im
        return Complex(x, y)

    def __mul__(self, z):
        x = self.re*z.re - self.im*z.im
        y = self.re*z.im + self.im*z.re
        return Complex(x, y)

    def __str__(self):
        if self.im < 0:
            sgn = ' - '
            y = -self.im
        else:
            sgn = ' + '
            y = self.im
        return '{0}{1}{2}i'.format(self.re, sgn, y)

    def show(self, arg):
        if self.im < 0:
            sgn = ' - '
            y = -self.im
        else:
            sgn = ' + '
            y = self.im
        print(arg, end=' ')
        print(str(self.re)+sgn+str(y)+'i')
        return self


class Vector:
    '''Define Vector'''
    def __init__(self, *comps):
        cnt = 0
        self.vec = []
        for val in comps:
            self.vec.append(float(val))
            cnt += 1
        self.dim = cnt

    def SetVector(self, src):
        self.dim = len(src)
        self.vec = src
        return self

    def GetVector(self):
        return self.vec

    def show(self, comment):
        print(comment, end=' ')
        print(self.vec)
        print('(dim=%d)' % self.dim)
        return self


class Triangle:
    def __init__(self, v0=None, v1=None, v2=None, nvec=None):
        self.vertex = {0:v0, 1:v1, 2:v2}
        self.normal = nvec

    def show(self, arg):
        print(arg)
        for i, v in self.vertex.items():
            print('v'+str(i)+'-> %r' % v)
        print('n->', self.normal)
        return self

    def SetVector(self, offset, val):
        try:
            self.vertex[offset] = val.vec
        except ValueError:
            print('No $d-th vertex' % offset)
        return self

    def SetNormal(self, n=None):
        if n != None:
            self.normal = n
        else:
            pass
#            self.normal = Cross()    미완...


class MyTriagle(Triangle):   ### 상속 클래스
    def __init__(self, v0_vec, v1_vec, v2_vec, n_vec):
        self.area = 0
        v0 = v0_vec.GetVector()
        v1 = v1_vec.GetVector()
        v2 = v2_vec.GetVector()
        n = n_vec.GetVector()
        super(MyTriagle, self).__init__(v0, v1, v2, n)  ### 상위 클래스를 불러서 해당 변수를 집어넣어준다.



if __name__ == '__main__':
    print('It Work')
    a = Complex(1, 2)
    a.show('a = ')
    b = Complex(3, 4)
    b.show('b = ')

    y1 = a.add(b)
    y2 = a+b
    y1.show('a add to b : ')
    y2.show('a + b : ')
    y3 = a*b
    y3.show('a * b = ')
    print(y3)


v1 = Vector(1, 2, 3)
v1.show('v1 =')

v2 = Vector().SetVector([1, -1, 0]).show('v2 =')
v3 = Vector().SetVector([1, 1, 0]).show('v3 =')
v4 = Vector().SetVector([0, 1, -1]).show('v4 =')

T1 = Triangle(v1.GetVector(), v2.GetVector(), v3.GetVector(), v4.GetVector()).show('Triangle : ')
T2 = MyTriagle(v1, v2, v3, v4).show('MyMy')
