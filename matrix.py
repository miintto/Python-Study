import math


class Matrix:
    '''Matrix Class'''
    def __init__(self, mat_list = None):
        self.matrix = mat_list
        self.len_row = 0
        self.len_col = 0
        self.set_len()

    def set_len(self):
        '''
        행렬의 차원 계산
        list의 길이를  row의 길이로 설정
        sublist 마다 길이를 비교해서 모두 같으면 그 길이를 column의 길이로 설정
        '''
        if self.matrix is not None:

            if type(self.matrix[0]) != list:
                self.matrix = [self.matrix]

            self.len_row = len(self.matrix)
            len_col = len(self.matrix[0])
            for i in range(1, self.len_row):
                if len(self.matrix[i]) != len_col:
                    raise ValueError('행렬의 차원이 서로 다릅니다.')
            self.len_col = len_col


    def __str__(self):
        '''
        (m x n)
         [ MATRIX ] 형태로 출력
        '''
        mat_line = '('+str(self.len_row)+'x'+str(self.len_col)+')\n'
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
        '''
        같은 차원의 행렬간 덧셈 정의
        서로 차원이 다르면 ValueError
        '''
        if (self.len_row != matrix.len_row) | (self.len_col != matrix.len_col):
            raise ValueError('행렬의 차원이 서로 다릅니다.')

        mat_list =[]
        for row in range(self.len_row):
            mat_list.append([self.Item(row, col)+matrix.Item(row, col) for col in range(self.len_col)])
        return Matrix(mat_list)


    def __sub__(self, matrix):
        '''
        같은 차원의 행렬간 뺄셈 정의
        서로 차원이 다르면 ValueError
        '''
        if (self.len_row != matrix.len_row) | (self.len_col != matrix.len_col):
            raise ValueError('행렬의 차원이 서로 다릅니다.')

        mat_list =[]
        for row in range(self.len_row):
            mat_list.append([self.Item(row, col)-matrix.Item(row, col) for col in range(self.len_col)])
        return Matrix(mat_list)


    def __mul__(self, arg):
        '''
        상수를 곱하면 모든 원소를 상수배
        행렬을 곱할시 행렬 곱 정의 (차원이 맞지 않으면 ValueError)
        '''
        if type(arg) != Matrix:
            mat_list = []
            for line in self.matrix:
                mat_list.append([elm*arg for elm in line])
            return Matrix(mat_list)

        else:
            if self.len_col != arg.len_row:
                raise ValueError('곱할 수 없는 행렬입니다.')

            mat_list = []
            for row in range(self.len_row):
                row_mat = []
                for col in range(self.len_col):
                    row_mat.append(sum([self.Item(row, i)*arg.Item(i, col) for i in range(self.len_col)]))
                mat_list.append(row_mat)
            return Matrix(mat_list)


    def __truediv__(self, num):
        pass


    def Item(self, row, col):
        '''(row, col) 원소 출력'''
        return self.matrix[row][col]


    def Transpose(self):
        '''행렬을 대각으로 대칭'''
        mat_list = []
        for col in range(self.len_col):
            mat_list.append([self.Item(row, col) for row in range(self.len_row)])
        return Matrix(mat_list)


    def Trace(self):
        '''trace'''
        diag = [self.Item(i, i) for i in range(self.len_col)]
        return sum(diag)


    def Det(self):
        '''determinant'''
        matrix = self.upper_tri()
        det = 1
        for elm in [matrix.Item(i, i) for i in range(self.len_col)]:
            det *= elm
        return det


    def Upper_tri(self):
        '''행렬의 upper triangular matrix를 출력'''
        new_mat = [row for row in self.matrix]
        dim = self.len_col
        for j in range(dim-1):
            for idx in range(j+1, dim):
                k = new_mat[idx][j]/new_mat[j][j]
                new_mat[idx] = [new_mat[idx][i] - new_mat[j][i]*k for i in range(dim)]

        return Matrix(new_mat)


    def Inverse(self):
        '''역함수 계산 (square가 아니면 ValueError)'''
        if self.len_row != self.len_col:
            raise ValueError('정사각 행렬이 아닙니다.')





class IMatrix(Matrix):
    '''Identity Matrix'''
    def __init__(self, dim):
        self.identical(dim)
        super().__init__(self.mat_list)


    def identical(self, dim):
        mat_list = [[0]*dim for _ in range(dim)]
        for i in range(dim):
            mat_list[i][i] = 1
        self.mat_list = mat_list





if __name__=='__main__':
    print('##### 리스트를 행렬로 변환 #####')
    mat_list = [[1, 2, 3, 4, 5], [10, 20, 30, 40, 50], [15, 101, 0, 47, 4]]
    print('list :', mat_list)
    mat = Matrix(mat_list)
    print('matrix :\n', mat)
    print()

    print('##### 연산 정의 #####')
    A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print('A :', A)
    B = Matrix([[0, 2, 1], [2, 3, 1], [4, 0, 2]])
    print('B :', B)

    print('A+B :', A+B)
    print('A-B :', A-B)    
    print('Transpose of A : ', A.Transpose())
    print('A*B :', A*B)
    print('A*10 :', A*10)
