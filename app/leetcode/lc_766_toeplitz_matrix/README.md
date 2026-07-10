# 766. Toeplitz Matrix
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_766_toeplitz_matrix/README.md)

## Problem Description

Given an `m x n` matrix, return `true` if the matrix is Toeplitz. Otherwise, return `false`.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

### Example 1

```text
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
```

### Example 2

```text
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
```

### Constraints

```text
m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99
```

## Boilerplate

```python
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        pass
```

## English (Interview Answer)

To solve Toeplitz Matrix, I compare each cell with the cell directly up and to the left of it. If a matrix is Toeplitz, every value on a top-left to bottom-right diagonal must match the previous value on that same diagonal.

I iterate through each row with its index. For the first row there is no previous row, so I skip it. Inside each remaining row, I iterate through each value with its column index. For the first column there is no previous column, so I skip it as well.

For every other cell, I compare `matrix[i][j]` with `matrix[i-1][j-1]`. If they are different, the diagonal is not consistent, so I return `False` immediately. If all comparisons pass, I return `True`.

This approach has a time complexity of O(m * n), because each matrix cell is visited at most once. The space complexity is O(1), because no extra data structure is used.

## Espanol (Respuesta para Entrevista)

Para resolver Toeplitz Matrix, comparo cada celda con la celda que esta directamente arriba y a la izquierda. Si una matriz es Toeplitz, cada valor en una diagonal de arriba-izquierda hacia abajo-derecha debe coincidir con el valor anterior en esa misma diagonal.

Recorro cada fila con su indice. Para la primera fila no existe una fila anterior, asi que la omito. Dentro de cada fila restante, recorro cada valor con su indice de columna. Para la primera columna no existe una columna anterior, asi que tambien la omito.

Para cualquier otra celda, comparo `matrix[i][j]` con `matrix[i-1][j-1]`. Si son diferentes, la diagonal no es consistente, asi que devuelvo `False` inmediatamente. Si todas las comparaciones pasan, devuelvo `True`.

Este enfoque tiene una complejidad temporal de O(m * n), porque cada celda de la matriz se visita como maximo una vez. La complejidad espacial es O(1), porque no se usa ninguna estructura de datos adicional.
