from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = 0
        xz = 0
        max_size = 0
        for i in range(len(grid)):
            xz += max(grid[i])
            if len(grid[i]) > max_size:
                max_size = len(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    xy += 1
        yz = 0
        for i in range(max_size):
            data = []
            for row in range(len(grid)):
                data.append(grid[row][i])
            yz += max(data)
        print(xy, xz, yz)
        return xz + xy + yz

        # max(grid[0][0], grid[1,0])
        # max(grid[0][1], grid[1,1])
