from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        print(m, n)
        output = []
        for i in range(m):
            output.append([])
            for j in range(n):
                cell_sum = 0
                divide = 0
                if i-1 >= 0 and j-1 >= 0:
                    cell_sum += img[i-1][j-1]
                    divide += 1
                if i-1 >= 0:
                    cell_sum += img[i-1][j]
                    divide += 1
                if i-1 >= 0 and j+1 <= n-1:
                    cell_sum += img[i-1][j+1]
                    divide += 1
                if j+1 <= n-1:
                    # print(i, j)
                    cell_sum += img[i][j+1]
                    divide += 1
                if i+1 <= m-1 and j+1 <= n-1:
                    cell_sum += img[i+1][j+1]
                    divide += 1
                if i+1 <= m-1:
                    cell_sum += img[i+1][j]
                    divide += 1
                if i+1 <= m-1 and j-1 >= 0:
                    cell_sum += img[i+1][j-1]
                    divide += 1
                if j-1 >= 0:
                    divide += 1
                    cell_sum += img[i][j-1]
                cell_sum += img[i][j]
                divide += 1
                output[i].append(int(cell_sum/divide))
        return output
