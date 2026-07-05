# 733. Flood Fill
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_733_flood_fill/README.md)

## Problem Description

You are given an image represented by an `m x n` grid of integers `image`, where `image[i][j]` represents the pixel value of the image. You are also given three integers `sr`, `sc`, and `color`. Your task is to perform a flood fill on the image starting from the pixel `image[sr][sc]`.

To perform a flood fill:

1. Begin with the starting pixel and change its color to `color`.
2. Perform the same process for each pixel that is directly adjacent, horizontally or vertically, and shares the same color as the starting pixel.
3. Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
4. The process stops when there are no more adjacent pixels of the original color to update.

Return the modified image after performing the flood fill.

### Example 1

```text
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1), all pixels connected by a path of the same color as the starting pixel are colored with the new color. The bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.
```

### Example 2

```text
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.
```

### Constraints

```text
m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 2^16
0 <= sr < m
0 <= sc < n
```

## Boilerplate

```python
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pass
```

## English (Interview Answer)

To solve Flood Fill, I first store the original color of the starting pixel `image[sr][sc]`. Then I use a recursive depth-first search from the starting position.

For each cell, I stop if the position is outside the image, if the cell does not have the original color, or if the cell already has the target `color`. Otherwise, I change the current cell to `color` and recursively apply the same process to its four neighbors: up, right, down, and left.

This works because flood fill only affects pixels that are connected horizontally or vertically to the starting pixel and have the same original color.

The time complexity is O(m * n), because in the worst case every pixel can be visited once. The space complexity is O(m * n) in the worst case due to the recursion stack.

## Espanol (Respuesta para Entrevista)

Para resolver Flood Fill, primero guardo el color original del pixel inicial `image[sr][sc]`. Despues uso una busqueda en profundidad recursiva desde la posicion inicial.

Para cada celda, me detengo si la posicion esta fuera de la imagen, si la celda no tiene el color original, o si la celda ya tiene el `color` objetivo. En caso contrario, cambio la celda actual a `color` y aplico recursivamente el mismo proceso a sus cuatro vecinos: arriba, derecha, abajo e izquierda.

Esto funciona porque flood fill solo afecta los pixeles conectados horizontal o verticalmente al pixel inicial y que tienen el mismo color original.

La complejidad temporal es O(m * n), porque en el peor caso cada pixel puede visitarse una vez. La complejidad espacial es O(m * n) en el peor caso por la pila de recursion.
