import math


class Matrix:
    def __init__(self, mat_list = None):
        self.matrix = mat_list
        if type(self.matrix[0]) != list:
            self.matrix = [self.matrix]
        self.len_raw = 0
        self.len_col = 0
        self.set_len()
        
    def set_len(self):
        if self.matrix is not None:            
            self.len_raw = len(self.matrix)
            len_col = len(self.matrix[0])
            for i in range(1, self.len_raw):
                if len(self.matrix[i]) != len_col:
                    raise ValueError('행렬의 차원이 서로 다릅니다.')
            self.len_col = len_col

    def __str__(self):
        mat_line = '('+str(self.len_raw)+'x'+str(self.len_col)+')\n'
        for line in self.matrix:
            mat_line += ' ['
            for elm in line:
                if elm<10:
                    mat_line += '  '+str(elm)+' '
                elif elm<100:
                    mat_line += ' '+str(elm)+' '
                else:
                    mat_line += str(elm)+' '
            mat_line += ']\n'
        return mat_line

    def __add__(self, matrix):
        if (self.len_raw != matrix.len_raw) | (self.len_col != matrix.len_col):
            raise ValueError('행렬의 차원이 서로 다릅니다.')
        mat_list =[]
        for raw in range(self.len_raw):
            mat_list.append([self.item(raw, col)+matrix.item(raw, col) for col in range(self.len_col)])
        return Matrix(mat_list)

    def __sub__(self, matrix):
        if (self.len_raw != matrix.len_raw) | (self.len_col != matrix.len_col):
            raise ValueError('행렬의 차원이 서로 다릅니다.')
        mat_list =[]
        for raw in range(self.len_raw):
            mat_list.append([self.item(raw, col)-matrix.item(raw, col) for col in range(self.len_col)])
        return Matrix(mat_list)

    def __mul__(self):
        pass

    def item(self, raw, col):
        return self.matrix[raw][col]

    def transpose(self):
        mat_list = []
        for col in range(self.len_col):
            mat_list.append([self.item(raw, col) for raw in range(self.len_raw)])
        return Matrix(mat_list)

    def inverse(self):
        pass


if __name__=='__main__':
    mat_list = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [15, 101, 0, 0, 4], [15, 74, 333, 14, 5]]
    mat = Matrix(mat_list)
    print(mat)

    A = Matrix([[1, 2, 3], [4, 5, 6]])
    print('A =', A)
    B = Matrix([[2, 3, 4], [1, 3, 4]])
    print('B =', B)

    print('A+B =', A+B)
    print('Transpose of A = ', A.transpose())