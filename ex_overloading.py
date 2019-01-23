#-*- coding: utf-8 -*-

import sys

# __getitem__, __setitem__ and for-loop

class Contents:
    def __init__(self, cnts = None):
        if cnts == None:
            self.data = [];
        else:
            self.data = list(cnts);

    def __getitem__(self, offset):
        # self의 offset번째 값을 가져오고 싶을 때 사용
        if isinstance(offset, int):
            # isinstance -> data type이 정수인가를 판별
            return self.data[offset];
        else:
            return self.data[slice(offset.start, offset.stop, offset.step)];

        # slicing -> a[3 : 5]에서 [3 : 5]
        # a[2 : 10 : 3] -> 2, 5, 8번째 값 출력

    def __setitem__(self, offset, value):
        # self의 offset번째에 value를 지정
        self.data[offset] = value;

# iterator

class Iteration:
    def __init__(self, start = 0, stop = 0):
        self.start = start;
        self.stop = stop;
        self.begin = start; # Save
        self.rens = [];

    def SetFunctions(self, fs):
        self.runs = fs;
        # self.runs[ : ] = fs;

    def __iter__(self):
        return self;

    def __next__(self):
        if self.start >= self.stop:
            self.start = self.begin;
            raise StopIteration;

        self.start += 1;
        return self.runs[self.start - 1];


def f1(x):
    return x;

def f2(x):
    return x * x;

def f3(x):
    return x * x * x;


def YieldIter(start, stop):
    while True:
        if start < stop:
            yield start
            start += 1
        else:
            return None


if __name__ == '__main__':

    X = Contents([2, 4, 8]);
    print(X.data)
    print(X[:6]);
    print(X[0::2]); # slice

    X[1:5] = [10, 20, 30, 40];
    print(X[:]);
    print(X[::-1])

    sum = 0;
    for v in X:  ### in 은 __next__를 불러온다.
        sum += v; # sufficient role as an iterator
    print(sum);

    Y = Iteration(0, 3);
    Y.SetFunctions([f1, f2, f3]);

    for fun in Y:
        print(fun(5));

    for i in YieldIter(0, 5):
        print(i, '번째')
