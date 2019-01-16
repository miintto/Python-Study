# -*- coding: utf-8 -*-
# 2019.01/14 ~ 15


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

    def __str__(self):   ### __repr__ 과의 차이점은?
        '''print 함수와 연관'''
        if self.im < 0:
            sgn = ' - '
            y = -self.im
        else:
            sgn = ' + '
            y = self.im
        return '{0}{1}{2}i'.format(self.re, sgn, y)   ### {}안에는

    def show(self, arg = ''):
        if self.im < 0:
            sgn = ' - '
            y = -self.im
        else:
            sgn = ' + '
            y = self.im
        print(arg, end=' ')
        print(str(self.re)+sgn+str(y)+'i')
        return self   ### show함수에 꼭 return self가 들어갈 필요가 있을까? #1


class Vector:
    '''Define Vector'''
    def __init__(self, *comps):
        cnt = 0
        self.vec = []
        for val in comps:
            self.vec.append(float(val))
            cnt += 1
        self.dim = cnt

    def __str__(self):
        vec = str(self.vec)
        vec = vec.replace('[', '< ').replace(']', ' >').replace(',', ' ,')
        return vec

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
            print('No %d-th vertex' % offset)
        return self

    def SetNormal(self, n=None):
        if n != None:
            self.normal = n
        else:
            pass
            #self.normal = Cross()    미완...
        return self


class MyTriagle(Triangle):   ### 상속 클래스
    def __init__(self, v0_vec, v1_vec, v2_vec, n_vec):
        self.area = 0
        v0 = v0_vec.GetVector()
        v1 = v1_vec.GetVector()
        v2 = v2_vec.GetVector()
        n = n_vec.GetVector()
        super(MyTriagle, self).__init__(v0, v1, v2, n)
            '''
            상위 클래스를 불러서 해당 변수를 집어넣어준다.
            super()안의 빈칸을 비워놔도 상관없는듯...
            '''

    def SetNormal(self, n1, n2, n3):
        '''
        상속받은 클래스에서 부모 클래스에 있는 함수와 똑같은 이름의 함수를 만들면
        상속받은 클래스의 함수가 우선적으로 적용, 부모 클래스의 함수는 작동하지 않음
        -> 오버라이딩
        '''
        self.normal = [n1, n2, n3]
        return self



print('name', __name__=='__main__')

if __name__ == '__main__':
    '''
    실행한 모듈이 메인 프로그램인지 확인하는 작업
    여기서 __name__은 자신을 포함하고 있는 모듈의 이름을 가리킨다.
    예를들어 커멘드에서 python3 ex_all.py 를 실행해보면
    __name__에는 'ex_all'라는 이름이 메인으로 지정된다.
    그래서 __name__=='__main__'는 True라는 값을 반환하게된다.

    하지만 ex_all_2.py 라는 모듈을 만들어서 ex_all을 import하여 ex_all_2.py를 실행하는 경우에는
    __name__에는 ex_all_2라는 값이 들어가게 되어
    __name__=='__main__'는 False 를 반환하게 된다.
    '''
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
    y3.show('a * b =')
    print('a * b =', y3, end='\n\n')
### 여기까지의 내용은 ex_all을 직접 실행하는 경우에만 실행이 된다.
### 이런 작업은 debugging때 주로 사용할 수 있다.


v1 = Vector(1, 2, 3)
v1.show('v1 =')
print('v1 :', v1)

v2 = Vector().SetVector([1, -1, 0]).show('v2 =')   #1 이렇게 인스턴스를 return받으면 SetVector와 show를 동시에 작성할 수 있다. 함수를 한번에 쭉 이어서 작성할 수 있음
v3 = Vector().SetVector([1, 1, 0]).show('v3 =')
v4 = Vector().SetVector([0, 1, -1]).show('v4 =')

T1 = Triangle(v1.GetVector(), v2.GetVector(), v3.GetVector(), v4.GetVector())
T1.SetNormal([-1, -2, -3]).show('T1 : ')

T2 = MyTriagle(v1, v2, v3, v4)
T2.SetNormal(-1, -2, -3).show('T2 : ')
