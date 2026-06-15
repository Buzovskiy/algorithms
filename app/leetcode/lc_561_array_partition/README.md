# 561. Array Partition

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_561_array_partition/README.md)

## Problem Description
Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `min(ai, bi)` for all `i` is maximized. Return the maximized sum.

**Example 1:**
Input: `nums = [1,4,3,2]`
Output: `4`
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. `(1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3`
2. `(1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3`
3. `(1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4`
So the maximum possible sum is 4.

**Example 2:**
Input: `nums = [6,2,6,5,1,2]`
Output: `9`
Explanation: The optimal pairing is `(2, 1), (2, 5), (6, 6)`. `min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9`.

**Constraints:**
- `1 <= n <= 10^4`
- `nums.length == 2 * n`
- `-10^4 <= nums[i] <= 10^4`

## Boilerplate for starting
```python
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        pass
```

## English (Interview Answer)

To maximize the sum of the minimums of pairs, we want to pair numbers that are close to each other. This ensures that when we take the minimum of a pair, we don't "waste" a very large number by pairing it with a very small one.

1.  **Sort the Array**: By sorting the array in ascending order, we group the smallest available numbers together.
2.  **Form Pairs**: Once sorted, the optimal pairs are consecutive elements: `(nums[0], nums[1]), (nums[2], nums[3]), ...`.
3.  **Sum the Minimums**: The minimum of each pair `(nums[i], nums[i+1])` will always be `nums[i]` (the element at the even index).
4.  **Calculate Result**: We iterate through the sorted array, jumping by 2, and add the element at each even index to our total sum.

The time complexity is **O(n log n)** because of the sorting. The space complexity is **O(1)** or **O(n)** depending on the sorting implementation's space requirements.

## Español (Respuesta para Entrevista)

Para maximizar la suma de los mínimos de los pares, queremos agrupar números que estén cerca el uno del otro. Esto asegura que al tomar el mínimo de un par, no "desperdiciemos" un número muy grande al emparejarlo con uno muy pequeño.

1.  **Ordenar el arreglo**: Al ordenar el arreglo en orden ascendente, agrupamos los números más pequeños disponibles.
2.  **Formar pares**: Una vez ordenados, los pares óptimos son los elementos consecutivos: `(nums[0], nums[1]), (nums[2], nums[3]), ...`.
3.  **Sumar los mínimos**: El mínimo de cada par `(nums[i], nums[i+1])` siempre será `nums[i]` (el elemento en el índice par).
4.  **Calcular el resultado**: Iteramos a través del arreglo ordenado, saltando de 2 en 2, y sumamos el elemento en cada índice par a nuestra suma total.

La complejidad temporal es **O(n log n)** debido a la ordenación. La complejidad espacial es **O(1)** u **O(n)**, dependiendo de los requisitos de espacio de la implementación del algoritmo de ordenación.
