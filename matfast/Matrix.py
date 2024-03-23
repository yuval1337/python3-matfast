from typing import List

class Matrix:
    def __init__(self, matrix_like: List[List[float]]):
        self._M  = len(matrix_like)
        self._N = len(matrix_like[0])
        if any([len(row) != self._N for row in matrix_like[1:]]):
            raise ValueError
        self._value = matrix_like

    @property    
    def shape(self):
        return (self._M, self._N)

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.shape != other.shape:
            raise ValueError
        return Matrix([[
                    sum([self._value[row][idx] * other._value[idx][col] for idx in range(self.shape[1])])
                for col in range(other.shape[1])]
            for row in range(self.shape[0])
        ])

    def __repr__(self) -> str:
        result = "Matrix(["
        for idx, row in enumerate(self._value):
            result += str(row)
            if idx < self.shape[0] - 1:
                result += ","
        result += "])"
        return result


if __name__ == "__main__":
    m1 = Matrix([[1,2,3],[4,5,6],[7,8,9]])
    m2 = Matrix([[0,0,1],[0,1,0],[1,0,0]]) # Permutation matrix
    print(m1 * m2)