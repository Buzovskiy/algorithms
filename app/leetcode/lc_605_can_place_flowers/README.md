# 605. Can Place Flowers

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_605_can_place_flowers/README.md)

## Problem Description

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer `n`, return `true` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and `false` otherwise.

**Example 1:**
- **Input:** `flowerbed = [1,0,0,0,1], n = 1`
- **Output:** `true`

**Example 2:**
- **Input:** `flowerbed = [1,0,0,0,1], n = 2`
- **Output:** `false`

**Constraints:**
- `1 <= flowerbed.length <= 2 * 10^4`
- `flowerbed[i]` is `0` or `1`.
- There are no two adjacent flowers in `flowerbed`.
- `0 <= n <= flowerbed.length`

## Boilerplate

```python
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        pass
```

## English (Interview Answer)

To solve the **Can Place Flowers** problem, we need to determine if we can plant `n` additional flowers in a flowerbed without violating the rule that no two flowers can be adjacent.

1.  **Greedy Approach:** We can iterate through the flowerbed and check each empty plot (marked with `0`).
2.  **Checking Neighbors:** A flower can be planted at index `i` if:
    *   The plot itself is empty (`flowerbed[i] == 0`).
    *   The plot to the left is either out of bounds or empty.
    *   The plot to the right is either out of bounds or empty.
3.  **Updating the Flowerbed:** When we find a valid spot, we "plant" a flower there by setting `flowerbed[i] = 1` and decrementing `n`.
4.  **Early Exit:** If `n` reaches zero, we can immediately return `true`.
5.  **Final Result:** If we finish iterating and `n` is still greater than zero, we return `false`.

The provided algorithm uses a slightly different state-tracking approach with a `prev` variable to keep track of the status of the previous plot and adjust the count of possible flowers dynamically.

**Complexity:**
*   **Time Complexity:** O(N), where N is the length of the flowerbed, as we traverse the array once.
*   **Space Complexity:** O(1), as we only use a few extra variables.

## Español (Respuesta para Entrevista)

Para resolver el problema de **¿Se pueden plantar flores?**, debemos determinar si es posible plantar `n` flores adicionales en un cantero sin violar la regla de que no puede haber dos flores adyacentes.

1.  **Enfoque Voraz (Greedy):** Podemos recorrer el cantero y verificar cada parcela vacía (marcada con `0`).
2.  **Verificación de Vecinos:** Se puede plantar una flor en el índice `i` si:
    *   La parcela misma está vacía (`flowerbed[i] == 0`).
    *   La parcela a la izquierda está fuera de los límites o está vacía.
    *   La parcela a la derecha está fuera de los límites o está vacía.
3.  **Actualización del Cantero:** Cuando encontramos un lugar válido, "plantamos" una flor allí estableciendo `flowerbed[i] = 1` y decrementamos `n`.
4.  **Salida Temprana:** Si `n` llega a cero, podemos devolver `true` de inmediato.
5.  **Resultado Final:** Si terminamos de recorrer y `n` sigue siendo mayor que cero, devolvemos `false`.

El algoritmo proporcionado utiliza un enfoque de seguimiento de estado ligeramente diferente con una variable `prev` para rastrear el estado de la parcela anterior y ajustar el recuento de flores posibles de forma dinámica.

**Complejidad:**
*   **Complejidad Temporal:** O(N), donde N es la longitud del cantero, ya que recorremos el arreglo una vez.
*   **Complejidad Espacial:** O(1), ya que solo utilizamos unas pocas variables adicionales.
