# 661. Image Smoother

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_661_image_smoother/README.md)

## Problem Description

An image smoother is a filter of size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells. If one or more surrounding cells are not present, they are not considered in the average.

Given an `m x n` integer matrix `img` representing the grayscale values of an image, return the image after applying the smoother to each cell.

### Example 1

```text
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
```

Explanation:

```text
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = 0
For the point (1,1): floor(8/9) = 0
```

### Example 2

```text
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
```

Explanation:

```text
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = 138
```

### Constraints

```text
m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
```

## Boilerplate

```python
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        pass
```

## English (Interview Answer)

To solve the Image Smoother problem, I need to compute a new value for every cell using the average of all valid cells in its 3 x 3 neighborhood. For each position, I check the eight possible neighbors and the current cell itself. If a neighbor is inside the matrix boundaries, I add its value to the sum and increase the divisor.

After checking all valid surrounding cells, I divide the sum by the number of included cells and round down by converting the result to an integer. I store each result in a separate output matrix so the original image values are still available while computing later cells.

The time complexity is O(m * n), because every cell is processed once and each cell checks a constant number of neighbors. The space complexity is O(m * n) for the output matrix.

## Espanol (Respuesta para Entrevista)

Para resolver el problema Image Smoother, necesito calcular un nuevo valor para cada celda usando el promedio de todas las celdas validas dentro de su vecindario de 3 x 3. Para cada posicion, reviso los ocho vecinos posibles y tambien la celda actual. Si un vecino esta dentro de los limites de la matriz, sumo su valor y aumento el divisor.

Despues de revisar todas las celdas vecinas validas, divido la suma entre la cantidad de celdas incluidas y redondeo hacia abajo convirtiendo el resultado a entero. Guardo cada resultado en una matriz de salida separada para que los valores originales de la imagen sigan disponibles al calcular las siguientes celdas.

La complejidad temporal es O(m * n), porque cada celda se procesa una vez y cada celda revisa una cantidad constante de vecinos. La complejidad espacial es O(m * n) por la matriz de salida.
