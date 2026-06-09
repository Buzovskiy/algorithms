# 463. Island Perimeter
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/463_island_perimeter/README.md)

## English (Interview Answer)

My approach is to iterate through every cell in the grid. Whenever I find a land cell, I initially assume it contributes 4 edges to the perimeter.

Then, I check whether the current land cell is connected to another land cell above or to the left. If two land cells share an edge, that edge should not be counted as part of the perimeter. Since it was counted twice (once for each cell), I subtract 2 from the total perimeter for every shared edge.

By only checking the top and left neighbors, I avoid counting the same shared edge multiple times.

The algorithm visits each cell exactly once, resulting in a time complexity of O(rows × cols) and a space complexity of O(1).

## Español (Respuesta para Entrevista)

Mi enfoque consiste en recorrer todas las celdas de la matriz. Cada vez que encuentro una celda de tierra, asumo inicialmente que aporta 4 lados al perímetro.

Después, verifico si la celda actual está conectada con otra celda de tierra arriba o a la izquierda. Cuando dos celdas de tierra comparten un lado, ese lado no forma parte del perímetro exterior. Como ese lado fue contado dos veces (una por cada celda), resto 2 al perímetro total por cada borde compartido.

Al comprobar únicamente los vecinos superior e izquierdo, evito procesar el mismo borde compartido más de una vez.

El algoritmo recorre cada celda exactamente una vez, por lo que la complejidad temporal es O(filas × columnas) y la complejidad espacial es O(1).
