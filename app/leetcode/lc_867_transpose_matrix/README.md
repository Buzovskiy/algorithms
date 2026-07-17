# 867. Transpose Matrix
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_867_transpose_matrix/README.md)

## Problem Description

Given a 2D integer array `matrix`, return the transpose of `matrix`.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

### Example 1

```text
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```

### Example 2

```text
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```

### Constraints

```text
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 10^5
-10^9 <= matrix[i][j] <= 10^9
```

## Boilerplate

```python
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
```

## English (Interview Answer)

To solve the Transpose Matrix problem, we need to create a new matrix where rows become columns and columns become rows. If the original matrix has `m` rows and `n` columns, the transposed matrix must have `n` rows and `m` columns.

1. I get the number of original rows with `len(matrix)` and the number of original columns with `len(matrix[0])`.
2. I create a result matrix filled with zeroes, sized as `n x m`.
3. I iterate through every cell `matrix[i][j]` in the original matrix.
4. For each value, I place it into `transposed[j][i]`, which swaps the row and column indices.
5. Finally, I return the transposed matrix.

This approach has a time complexity of O(m * n), because every element is visited once, and a space complexity of O(m * n), because we create a new matrix for the answer.

## Español (Respuesta)

Para resolver el problema Transpose Matrix, debemos crear una nueva matriz donde las filas se convierten en columnas y las columnas se convierten en filas. Si la matriz original tiene `m` filas y `n` columnas, la matriz transpuesta debe tener `n` filas y `m` columnas.

1. Obtengo el número de filas originales con `len(matrix)` y el número de columnas originales con `len(matrix[0])`.
2. Creo una matriz de resultado llena de ceros, con tamaño `n x m`.
3. Recorro cada celda `matrix[i][j]` de la matriz original.
4. Para cada valor, lo coloco en `transposed[j][i]`, intercambiando los índices de fila y columna.
5. Finalmente, devuelvo la matriz transpuesta.

Este enfoque tiene una complejidad temporal de O(m * n), porque visitamos cada elemento una vez, y una complejidad espacial de O(m * n), porque creamos una nueva matriz para la respuesta.
