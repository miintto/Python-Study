# -*- coding: utf-8 -*-
# 2019.01/07

import numpy as np


class Vec3D:
    """3차원에서의 벡터 정의"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return '['+str(self.x)+', '+str(self.y)+', '+str(self.z)+']'

    def __add__(self, arg):
        if type(arg) == Vec3D:
            x = self.x + arg.x
            y = self.y + arg.y
            z = self.z + arg.z
            return Vec3D(x, y, z)
        else:
            return Vec3D(self.x+arg, self.y+arg, self.z+arg)

    def __sub__(self, arg):
        if type(arg) == Vec3D:
            x = self.x - arg.x
            y = self.y - arg.y
            z = self.z - arg.z
            return Vec3D(x, y, z)
        else:
            return Vec3D(self.x-arg, self.y-arg, self.z-arg)

    def __mul__(self, arg):
        '''inner product'''
        if type(arg) == Vec3D:
            x = self.x * arg.x
            y = self.y * arg.y
            z = self.z * arg.z
            return x+y+z
        else:
            return Vec3D(self.x*arg, self.y*arg, self.z*arg)

    def __truediv__(self, arg):
        return Vec3D(self.x/arg, self.y/arg, self.z/arg)

    def __neg__(self):
        return Vec3D(-self.x, -self.y, -self.z)

    def __abs__(self):
        '''2-norm 을 계산'''
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def cross(self, vec):
        i = self.y*vec.z-self.z*vec.y
        j = self.z*vec.x-self.x*vec.z
        k = self.x*vec.y-self.y*vec.x
        return Vec3D(i, j, k)
