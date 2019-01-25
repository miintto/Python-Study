#-*- coding: utf-8 -*-

import sys
import math
import functools

# classes

class ComPlex:
    '''Complex Class Definition'''
    def __init__(self, x=0, y=0):
        self.re = x;
        self.im = y;

    def Real(self): return self.re;

    def Imag(self): return self.im;

    def Conjugate(self):
        return ComPlex(self.re, -self.im);

    def Modulus(self):
        return math.sqrt(self.re*self.re + self.im*self.im);

    def __add__(self, z):
        x = self.re + z.re;
        y = self.im + z.im;
        return ComPlex(x, y);

    def __mul__(self, z):
        x = self.re*z.re - self.im*z.im;
        y = self.re*z.im + self.im*z.re;
        return ComPlex(x, y);

    def __truediv__(self, z):
        d2 = z.re*z.re + z.im*z.im;
        w = self*z.Conjugate();
        w.re /= d2;
        w.im /= d2;

        return w;

    def __str__(self):
        if self.im < 0:
            sgn = ' - ';
            y = -self.im;
        else:
            sgn = ' + ';
            y = self.im;
        return '{0}{1}{2}i'.format(self.re, sgn, y);

    def Show(self, arg=''):
        if self.im < 0:
            sgn = ' - ';
            y = -self.im;
        else:
            sgn = ' + ';
            y = self.im;

        print(arg, end=' ');
        print( str(self.re)+sgn+str(y)+' i' );
        return self;

class Vector:
    '''Define Vectors'''
    def __init__(self,*comps):
        self.vec = [];
        for val in comps:
            self.vec.append(float(val));

        self.dim = len(comps);

    def SetVector(self, vsrc):
        self.dim = len(vsrc);
        self.vec = vsrc;
        return self;

    def GetVector(self):
        return self.vec;

    def Coordinate(self, k):
        if k < self.dim:
            return self.vec[k];
        else:
            return 0;

    def Norm(self):
        d = 0;
        for vk in self.vec:
            d += vk*vk;

        return math.sqrt(d);

    def Scalar(self, scl):
        v = [scl*vk for vk in self.vec];

        return Vector().SetVector(v);

    def __add__(self, rvec):
        v = [vk for vk in self.vec];
        for k in range(self.dim):
            v[k] += rvec.Coordinate(k);

        return Vector().SetVector(v);

    def __sub__(self, rvec):
        v = [vk for vk in self.vec];
        for k in range(self.dim):
            v[k] -= rvec.Coordinate(k);

        return Vector().SetVector(v);

    def __mul__(self, rvec):
        only = 3;
        v = [self.Coordinate(k) for k in range(only)];
        w = [rvec.Coordinate(k) for k in range(only)];
        vxw = [ 0 for k in range(only)];
        for k in range(only):
            k1 = (k+1)%only;
            k2 = (k+2)%only;
            vxw[k] = v[k1]*w[k2] - v[k2]*w[k1];

        return Vector().SetVector(vxw);

    def __str__(self):
        pstr = self.StringVector();
        return pstr;

    def __call__(self, cmnt=''):
        print(cmnt,self);

    def StringVector(self):
        vstr = '<';
        for vk in self.vec:
            vstr += ' '+str(vk)+' ';
        vstr += '>';
        return vstr;

    def Dot(self, rvec):
        inner = 0;
        for k in range(self.dim):
            inner += self.Coordinate(k)*rvec.Coordinate(k);
        return inner;

    def Unitary(self):
        d = self.Norm();
        unit = self.Scalar(1/d);

        return unit;

    def Projector(self, plane0):
        n0 = plane0.Unitary();
        xonp = self - n0.Scalar(self.Dot(n0));

        return xonp;

    def Show(self,comment):
        print(comment, end=' ');
        print('(dim=%d)' % self.dim)
        print(self.vec);
        return self;

class Tri3D:
    '''Triangle in 3D'''

    num = 3;

    def __init__(self, v0=None, v1=None, v2=None, nvec=None):
        self.vertex = {0:v0, 1:v1, 2:v2};
        self.normal = nvec;

    def __str__(self):
        pstr = ['','','',''];
        for k in range(self.num):
            pstr[k] += 'v'+str(k)+'=';
            pstr[k] += self.GetVertex(k).StringVector();
        pstr[self.num] += 'n='+self.GetNormal().StringVector();

        return '\n'.join(pstr);

    def __call__(self, closed=True):
        yield self[0];
        yield self[1];
        yield self[2];
        if closed == True:
            yield self[0];

    def __getitem__(self, offs):
        return self.vertex[offs];

    def __setitem__(self, offs, value):
        self.vertex[offs] = value;

    def SetVertex(self, offset, vector):
        try:
            self.vertex[offset] = vector.vec;
        except ValueError:
            print('No %d-th vertex' % offset);

        return self;

    def GetVertex(self, offset):
        if offset < 3:
            return Vector().SetVector(self.vertex[offset]);
        else:
            return Vector().SetVector([0,0,0]);

    def SetNormal(self, nvec=None):
        if nvec == None:
            vec0 = self.GetVertex(0);
            vec1 = self.GetVertex(1);
            vec2 = self.GetVertex(2);
            nv = ( vec1-vec0 )*( vec2-vec0 );
            self.normal = nv.Unitary().GetVector();
        else:
            self.normal = nvec.Unitary().GetVector();

        return self;

    def GetNormal(self):
        return Vector().SetVector(self.normal);

    def CalArea(self):
        x0 = self.GetVertex(0);
        x1 = self.GetVertex(1);
        x2 = self.GetVertex(2);
        vxw = ( x1-x0 )*( x2-x0 );
        return vxw.Norm()/2;

    def Show(self, cmnt):
        print(cmnt);
        self.GetVertex(0)('v0=');
        self.GetVertex(1)('v1=');
        self.GetVertex(2)('v2=');
        self.GetNormal()('n=');

        return self;

    def Dump(self, name, beam=None):
        with open(name,'w+') as output:
            '''
            close를 쓰지 않아도 됨
            열고 있는동안 아래 내용 실행, 끝나면 자동으로 close
            '''
            headline = '# light beam = '+str(beam)+'\n';
            output.write(headline);
            for k, v in self.vertex.items():
                svec = [ '  '+str(vk)+'  ' for vk in v ];
                pt = ' '.join(svec);
                output.write('%s\n' % pt);
            svec = [ '  '+str(vk)+'  ' for vk in self.vertex[0] ];
            output.write('%s\n' % ' '.join(svec) );
            output.write('\n');

        return self;

class AugTri3D(Tri3D):
    def __init__(self, vec0=None, vec1=None, vec2=None, vecn=None):
        self.area = 0;
        if vec0 != None: v0 = vec0.GetVector();
        else: v0 = [];
        if vec1 != None: v1 = vec1.GetVector();
        else: v1 = [];
        if vec2 != None: v2 = vec2.GetVector();
        else: v2 = [];
        if vecn != None:
            unit = vecn.Unitary();
            n = unit.GetVector();
        else: n = [];

        super(AugTri3D,self).__init__(v0,v1,v2,n);

    def SetArea(self):
        self.area = self.CalArea();

        return self;

    def GetArea(self):
        return self.area;

    def CalProj(self, beam):
        w = {};
        for k in range(self.num):
            w[k] = self.GetVertex(k).Projector(beam);

        return AugTri3D(w[0],w[1],w[2], beam);

if __name__ == '__main__':

    v0 = Vector(1,0,0);
    v1 = Vector(0,1,0);
    v2 = Vector(0,0,1);
    n = Vector(1,1,1);
    v0('v0 = '); v1('v1 = '); v2('v2 = '); n('n = ');
    T0 = AugTri3D().SetVertex(0, v2).SetVertex(1, v1).SetVertex(2, v0).SetNormal(n);

    print(T0[0])

    v0.SetVector([4,0,0]);
    v1.SetVector([0,2,0]);
    v2.SetVector([4,0,3]);
    T1 = AugTri3D(v0,v1,v2).SetNormal();

    T0.Show('T0: ')
    T0.Dump('T0.out');
    print('|T0| = ',T0.SetArea().GetArea());


    T1.Show('T1: ')
    T1.Dump('T1.out');
    print('|T1| = ',T1.SetArea().GetArea());

    light = Vector(1,1,1);

    projT0 = T0.CalProj(light);
    print('|projT0| = ',projT0.SetArea().GetArea());
    projT0.Dump('projT0.out',light);

    projT1 = T1.CalProj(light);
    print('|pT1| = ',projT1.SetArea().GetArea());
    projT1.Dump('projT1.out',light);
