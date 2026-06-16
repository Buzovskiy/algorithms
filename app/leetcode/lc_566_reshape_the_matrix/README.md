# 566. Reshape the Matrix

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_566_reshape_the_matrix/README.md)

## Description

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

### Example 1:
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

### Example 2:
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

### Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 100
- -1000 <= mat[i][j] <= 1000
- 1 <= r, c <= 300

## Boilerplate
```python
from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        pass
```

## English (Interview Answer)

To solve the "Reshape the Matrix" problem, we first need to verify if the requested reshape is valid. A reshape is possible if and only if the total number of elements in the original matrix (m * n) equals the total number of elements in the target matrix (r * c).

If it's not possible, we return the original matrix as per the problem requirements.

If it is possible, I follow these steps:
1. I initialize an empty `output` list and a temporary `inner` list for the current row.
2. I use two pointers or indices (let's call them `i` and `j`) to keep track of the current element in the original matrix.
3. I iterate through the desired number of rows `r` and columns `c`.
4. For each cell in the new matrix, I fetch the element from `mat[i][j]`.
5. I increment the column index `j`. If `j` reaches the end of a row in the original matrix, I reset it to 0 and increment the row index `i`.
6. I append the element to the `inner` row list. After filling `c` elements, I append the `inner` list to the `output` matrix.

The time complexity is O(r * c), which is also O(m * n), because we visit each element exactly once. The space complexity is O(r * c) to store the result matrix.

## Español (Respuesta para Entrevista)

Para resolver el problema "Reshape the Matrix", primero debemos verificar si la redistribución solicitada es válida. Un cambio de forma es posible si y solo si el número total de elementos en la matriz original (m * n) es igual al número total de elementos en la matriz de destino (r * c).

Si no es posible, devolvemos la matriz original según los requisitos del problema.

Si es posible, sigo estos pasos:
1. Inicializo una lista vacía `output` y una lista temporal `inner` para la fila actual.
2. Utilizo dos punteros o índices (`i` y `j`) para realizar el seguimiento del elemento actual en la matriz original.
3. Itero a través del número deseado de filas `r` y columnas `c`.
4. Para cada celda en la nueva matriz, obtengo el elemento de `mat[i][j]`.
5. Incremento el índice de columna `j`. Si `j` llega al final de una fila en la matriz original, lo reinicio a 0 e incremento el índice de fila `i`.
6. Añado el elemento a la lista de fila `inner`. Después de completar `c` elementos, añado la lista `inner` a la matriz `output`.

La complejidad temporal es O(r * c), que es equivalente a O(m * n), ya que visitamos cada elemento exactamente una vez. La complejidad espacial es O(r * c) para almacenar la matriz resultante.
