from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perim = 0
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == 1:
                    perim += 4
                    # Check above
                    if i > 0 and grid[i-1][j] == 1:
                        perim -= 2
                    # check on the left
                    if j > 0 and grid[i][j-1] == 1:
                        perim -= 2

        return perim
