from typing import List

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        total = 0
        for i, row in enumerate(grid):
            for j, cube in enumerate(row):
                square = 2 * (1 if cube > 0 else 0) * 1 + 1 * cube * 4
                if i-1 >= 0:
                    if grid[i-1][j] >= cube:
                        square -= 1 * cube
                    else:
                        square -= 1 * grid[i-1][j]
                
                if j+1 <= len(row) - 1:
                    if grid[i][j+1] >= cube:
                        square -= 1 * cube
                    else:
                        square -= 1 * grid[i][j+1]

                if i+1 <= len(grid)-1:
                    if grid[i+1][j] >= cube:
                        square -= 1 * cube
                    else:
                        square -= 1 * grid[i+1][j]
                    
                if j-1 >= 0:
                    if grid[i][j-1] >= cube:
                        square -= 1 * cube
                    else:
                        square -= 1 * grid[i][j-1]
                
                total += square
        return total
