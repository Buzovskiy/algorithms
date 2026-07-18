# 883. Projection Area of 3D Shapes
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_883_projection_area_of_3d_shapes/README.md)

## Problem Description

You are given an `n x n` grid where we place some `1 x 1 x 1` cubes that are axis-aligned with the x, y, and z axes.

Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of the cell `(i, j)`.

We view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.

### Example 1

```text
Input: grid = [[1,2],[3,4]]
Output: 17
Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
```

### Example 2

```text
Input: grid = [[2]]
Output: 5
```

### Example 3

```text
Input: grid = [[1,0],[0,2]]
Output: 8
```

### Constraints

```text
n == grid.length == grid[i].length
1 <= n <= 50
0 <= grid[i][j] <= 50
```

## Boilerplate

```python
from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
```

## English (Interview Answer)

To solve the Projection Area of 3D Shapes problem, we need to calculate the visible area from three views: top, front, and side.

1. For the xy projection, I count every grid cell that has at least one cube, because from the top it contributes one square.
2. For the xz projection, I take the maximum value in each row, because from one side only the tallest tower in that row is visible.
3. For the yz projection, I take the maximum value in each column, because from the other side only the tallest tower in that column is visible.
4. Finally, I return the sum of these three projection areas.

This approach has a time complexity of O(n * n), because we inspect the grid cells and columns, and a space complexity of O(n), because the algorithm temporarily stores one column while calculating the yz projection.

## Español (Respuesta)

Para resolver el problema Projection Area of 3D Shapes, debemos calcular el área visible desde tres vistas: superior, frontal y lateral.

1. Para la proyección xy, cuento cada celda de la matriz que tiene al menos un cubo, porque desde arriba aporta un cuadrado.
2. Para la proyección xz, tomo el valor máximo de cada fila, porque desde un lado solo se ve la torre más alta de esa fila.
3. Para la proyección yz, tomo el valor máximo de cada columna, porque desde el otro lado solo se ve la torre más alta de esa columna.
4. Finalmente, devuelvo la suma de estas tres áreas de proyección.

Este enfoque tiene una complejidad temporal de O(n * n), porque inspeccionamos las celdas y las columnas de la matriz, y una complejidad espacial de O(n), porque el algoritmo guarda temporalmente una columna mientras calcula la proyección yz.
