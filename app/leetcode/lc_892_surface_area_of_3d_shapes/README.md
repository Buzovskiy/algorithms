# 892. Surface Area of 3D Shapes
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_892_surface_area_of_3d_shapes/README.md)

## Problem Description

You are given an `n x n` grid where you have placed some `1 x 1 x 1` cubes. Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of cell `(i, j)`.

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.

### Example 1

```text
Input: grid = [[1,2],[3,4]]
Output: 34
```

### Example 2

```text
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
```

### Example 3

```text
Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
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
    def surfaceArea(self, grid: List[List[int]]) -> int:
```

## English (Interview Answer)

To solve the Surface Area of 3D Shapes problem, I calculate the contribution of every tower independently and subtract the faces hidden by neighboring towers.

1. For each cell, if the tower height is greater than zero, it contributes one top face and one bottom face.
2. The four vertical sides contribute `4 * cube`, where `cube` is the height of the current tower.
3. For each directly adjacent neighbor, I subtract the smaller height between the current tower and that neighbor, because those faces are glued together and no longer visible.
4. I add the remaining visible area for each cell to the total and return it.

This approach has a time complexity of O(n * n), because every grid cell is inspected once and each cell checks four neighbors. The space complexity is O(1), because only a few variables are used.

## Español (Respuesta)

Para resolver el problema Surface Area of 3D Shapes, calculo la contribución de cada torre de forma independiente y resto las caras que quedan ocultas por las torres vecinas.

1. Para cada celda, si la altura de la torre es mayor que cero, aporta una cara superior y una cara inferior.
2. Los cuatro lados verticales aportan `4 * cube`, donde `cube` es la altura de la torre actual.
3. Para cada vecino directamente adyacente, resto la menor altura entre la torre actual y ese vecino, porque esas caras quedan pegadas y ya no son visibles.
4. Sumo el área visible restante de cada celda al total y la devuelvo.

Este enfoque tiene una complejidad temporal de O(n * n), porque se inspecciona cada celda de la matriz una vez y cada celda revisa cuatro vecinos. La complejidad espacial es O(1), porque solo se usan unas pocas variables.
