class Matrix:
    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2
    def __add__(self):
        matrix = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
        for i in range(len(self.l1)):
            for j in range(len(self.l2[i])):
                matrix[i][j] = self.l1[i][j] + self.l2[i][j]
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))
    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in strmatrix]))
strmatrix = Matrix([[1,2,3],[4,5,6], [7,8,9]],[[10,11,12], [13,14,15],[16,17,18]])
print(strmatrix.__add__())