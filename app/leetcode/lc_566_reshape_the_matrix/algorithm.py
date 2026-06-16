from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        output = []
        inner = []
        i_max = len(mat) - 1
        j_max = len(mat[0]) - 1
        i = j = 0
        for row in range(r):
            for col in range(c):
                if j > j_max:
                    j = 0
                    i += 1
                inner.append(mat[i][j])
                j += 1
            output.append(inner)
            inner = []
        return output
