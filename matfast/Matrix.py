from typing import List

class Matrix:
    def __init__(self, matrix_like: List[List[float]]):
        self.shape  = (len(matrix_like), len(matrix_like[0])) # M, N
        if any([len(row) != self.shape[1] for row in matrix_like[1:]]):
            raise ValueError
        self._value = matrix_like

    def __mul__(self, other: "Matrix") -> "Matrix":
        if self.shape[0] != other.shape[1]:
            raise ValueError(f"invalid shape: {self.shape[0]}, {other.shape[1]} ?")
        return Matrix([[
                    sum([self._value[row][idx] * other._value[idx][col] for idx in range(self.shape[1])])
                for col in range(other.shape[1])]
            for row in range(self.shape[0])
        ])

    def __repr__(self) -> str:
        result = "Matrix(["
        if self.shape[0] <= 3:
            for idx, row in enumerate(self._value[0:]):
                result += str(row)
                if idx < self.shape[0] - 1:
                    result += ","
        else:
            for idx, row in enumerate(self._value[:2]+self._value[-1:]):
                if idx < 2:
                    result += str(row) + ","
                else:
                    result += "..." + str(row)

        result += "])"
        return result


if __name__ == "__main__":
    m1 = Matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    m2 = Matrix([[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]) # Permutation matrix
    print(m1 * m1)