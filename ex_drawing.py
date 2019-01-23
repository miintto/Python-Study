#-*- coding: utf-8 -*-

import sys, math

class Canvas:
    def __init__(self, width, height):
        self.width = width;
        self.height = height;
        self.data = [[' '] * width for i in range(height)];

    def setpixel(self, row, col):
        self.data[row][col] = '*';

    def getpixel(self, row, col):
        return self.data[row][col];

    def display(self):
        drawing = '+' + '-' * self.width + '+\n';
        drawing += '\n'.join(['|' + ''.join(row) + '|' for row in self.data]);
        drawing += '\n+' + '-' * self.width + '+';
        print(drawing);

class Shape:
    def paint(self, canvas): pass;

class Circle(Shape):
    def __init__(self, x, y, r):
        self.x = x;
        self.y = y;
        self.r = r;

    def paint(self, canvas):

        for t in range(0.0, 2 * math.pi, 0.1):
            u = int(self.x + self.r * math.cos(t));
            v = self.y + self.r * math.sin(t);
            canvas.setpixel(u, v);

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x;
        self.y = y;
        self.w = w;
        self.h = h;

    def paint(self, canvas):
        for k in range(self.x, self.x + self.w + 1):
            canvas.setpixel(self.y, k);
            canvas.setpixel(self.y + self.h, k);
        for k in range(self.y, self.y + self.h + 1):
            canvas.setpixel(k, self.x);
            canvas.setpixel(k, self.x + self.w);

class Square(Rectangle):
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size);

class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes;

    def paint(self, canvas):
        for s in self.shapes:
            s.paint(canvas);

if __name__ == '__main__':
    panel_1 = Canvas(30, 20);

    r1 = Rectangle(2, 3, 4, 5);
    sq1 = Square(5, 6, 5);
    # cir1 = Circle(8, 8, 10);
    shapes = [r1, sq1];

    mine = CompoundShape(shapes);
    mine.paint(panel_1);
    panel_1.display();
