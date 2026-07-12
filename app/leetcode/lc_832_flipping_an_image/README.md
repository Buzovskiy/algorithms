# 832. Flipping an Image
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_832_flipping_an_image/README.md)

## Problem Description

Given an `n x n` binary matrix `image`, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping `[1,1,0]` horizontally results in `[0,1,1]`.

To invert an image means that each `0` is replaced by `1`, and each `1` is replaced by `0`.

For example, inverting `[0,1,1]` results in `[1,0,0]`.

### Example 1

```text
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
```

### Example 2

```text
Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
```

### Constraints

```text
n == image.length
n == image[i].length
1 <= n <= 20
image[i][j] is either 0 or 1.
```

## Boilerplate

```python
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        pass
```

## English (Interview Answer)

To solve the Flipping an Image problem, I create a new matrix with the same size as the input matrix. Then I iterate through every cell of the original image.

For each value at position `image[i][j]`, I place it into the mirrored position of the same row in the new matrix: `len(image[0]) - 1 - j`. After placing the value, I invert it. If the value is `0`, I change it to `1`; otherwise, I change it to `0`.

After all rows and columns are processed, the new matrix contains the image flipped horizontally and inverted.

The time complexity is O(n * n), because every cell is processed once. The space complexity is O(n * n), because a new matrix is created for the result.

## Espanol (Respuesta para Entrevista)

Para resolver el problema Flipping an Image, creo una nueva matriz con el mismo tamano que la matriz de entrada. Luego recorro cada celda de la imagen original.

Para cada valor en la posicion `image[i][j]`, lo coloco en la posicion espejada de la misma fila dentro de la nueva matriz: `len(image[0]) - 1 - j`. Despues de colocar el valor, lo invierto. Si el valor es `0`, lo cambio a `1`; en caso contrario, lo cambio a `0`.

Despues de procesar todas las filas y columnas, la nueva matriz contiene la imagen volteada horizontalmente e invertida.

La complejidad temporal es O(n * n), porque cada celda se procesa una vez. La complejidad espacial es O(n * n), porque se crea una nueva matriz para el resultado.
