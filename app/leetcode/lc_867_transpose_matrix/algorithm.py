from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        cols_count = len(matrix)
        rows_count = len(matrix[0])
        transposed = [[0 for col in range(cols_count)] for row in range(rows_count)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                transposed[j][i] = matrix[i][j]
        return transposed
