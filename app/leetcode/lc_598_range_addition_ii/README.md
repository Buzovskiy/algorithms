# 598. Range Addition II

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_598_range_addition_ii/README.md)

## Problem Description

You are given an `m x n` matrix `M` initialized with all `0`'s and an array of operations `ops`, where `ops[i] = [ai, bi]` means `M[x][y]` should be incremented by one for all `0 <= x < ai` and `0 <= y < bi`.

Count and return *the number of maximum integers in the matrix after performing all the operations*.

**Example 1:**
- **Input:** `m = 3, n = 3, ops = [[2,2],[3,3]]`
- **Output:** `4`
- **Explanation:** The maximum integer in `M` is `2`, and there are four of it in `M`. So return `4`.

**Example 2:**
- **Input:** `m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]`
- **Output:** `4`

**Example 3:**
- **Input:** `m = 3, n = 3, ops = []`
- **Output:** `9`

**Constraints:**
- `1 <= m, n <= 4 * 10^4`
- `0 <= ops.length <= 10^4`
- `ops[i].length == 2`
- `1 <= ai <= m`
- `1 <= bi <= n`

## Boilerplate

```python
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        pass
```

## English (Interview Answer)

To solve the **Range Addition II** problem, we need to find the number of maximum integers in an `m x n` matrix after several increment operations.

The key observation is that every operation `[ai, bi]` starts from the top-left corner `(0, 0)` and covers all cells `(x, y)` where `0 <= x < ai` and `0 <= y < bi`. Since every operation includes the cell `(0, 0)`, this cell will always have the maximum value. Any other cell that is part of every single operation will also have this same maximum value.

The set of cells that are included in every operation is the intersection of all rectangles defined by `ops`. This intersection is itself a rectangle with dimensions equal to the minimum `ai` and the minimum `bi` across all operations.

1. We initialize `min_row` as `m` and `min_col` as `n`.
2. We iterate through each operation `[ai, bi]` in `ops`.
3. For each operation, we update `min_row = min(min_row, ai)` and `min_col = min(min_col, bi)`.
4. If `ops` is empty, the maximum value (0) is present in all `m * n` cells.
5. The number of maximum integers is simply the area of this intersection: `min_row * min_col`.

**Complexity:**
- **Time Complexity:** `O(k)`, where `k` is the number of operations, as we iterate through `ops` once.
- **Space Complexity:** `O(1)`, as we only store two variables for the minimum dimensions.

## Español (Respuesta para Entrevista)

Para resolver el problema de **Range Addition II**, necesitamos encontrar la cantidad de enteros máximos en una matriz de `m x n` después de varias operaciones de incremento.

La observación clave es que cada operación `[ai, bi]` comienza desde la esquina superior izquierda `(0, 0)` y cubre todas las celdas `(x, y)` donde `0 <= x < ai` y `0 <= y < bi`. Dado que cada operación incluye la celda `(0, 0)`, esta celda siempre tendrá el valor máximo. Cualquier otra celda que forme parte de cada una de las operaciones también tendrá este mismo valor máximo.

El conjunto de celdas que se incluyen en cada operación es la intersección de todos los rectángulos definidos por `ops`. Esta intersección es en sí misma un rectángulo con dimensiones iguales al `ai` mínimo y al `bi` mínimo de todas las operaciones.

1. Inicializamos `min_row` como `m` y `min_col` como `n`.
2. Iteramos a través de cada operación `[ai, bi]` en `ops`.
3. Para cada operación, actualizamos `min_row = min(min_row, ai)` y `min_col = min(min_col, bi)`.
4. Si `ops` está vacío, el valor máximo (0) está presente en todas las celdas `m * n`.
5. El número de enteros máximos es simplemente el área de esta intersección: `min_row * min_col`.

**Complejidad:**
- **Complejidad Temporal:** `O(k)`, donde `k` es el número de operaciones, ya que recorremos `ops` una vez.
- **Complejidad Espacial:** `O(1)`, ya que solo almacenamos dos variables para las dimensiones mínimas.
