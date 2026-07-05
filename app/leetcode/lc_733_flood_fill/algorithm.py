from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        color_old = image[sr][sc]
        def fill(i, j):
            if i < 0 or j < 0 or i == len(image) or j == len(image[0]) or image[i][j] != color_old or image[i][j] == color:
                return
            image[i][j] = color
            fill(i-1, j)
            fill(i, j+1)
            fill(i+1, j)
            fill(i,j-1)
        fill(sr, sc)
        return image
