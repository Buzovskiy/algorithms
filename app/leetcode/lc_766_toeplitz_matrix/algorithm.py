from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i, row in enumerate(matrix):
            if i - 1 < 0:
                continue
            for j, num in enumerate(row):
                if j - 1 < 0:
                    continue
                if num != matrix[i-1][j-1]:
                    return False
        return True
