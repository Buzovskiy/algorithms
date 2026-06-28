# 704. Binary Search
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_704_binary_search/README.md)

## Problem Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with O(log n) runtime complexity.

### Example 1

```text
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

### Example 2

```text
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

### Constraints

```text
1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.
```

## Boilerplate

```python
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass
```

## English (Interview Answer)

To solve Binary Search, I use the fact that the input array is already sorted in ascending order. I keep two pointers, `left` and `right`, representing the current search interval.

On each iteration, I calculate the middle index. If `nums[mid]` is equal to `target`, I return `mid`. If `nums[mid]` is smaller than `target`, then the target can only be on the right side, so I move `left` to `mid + 1`. Otherwise, the target can only be on the left side, so I move `right` to `mid - 1`.

The loop continues while `left <= right`. If the interval becomes empty, the target is not present in the array, so I return `-1`.

This approach has a time complexity of O(log n), because each step removes half of the remaining search space. The space complexity is O(1), because only a few variables are used.

## Espanol (Respuesta para Entrevista)

Para resolver Binary Search, uso el hecho de que el arreglo de entrada ya esta ordenado de forma ascendente. Mantengo dos punteros, `left` y `right`, que representan el intervalo actual de busqueda.

En cada iteracion, calculo el indice medio. Si `nums[mid]` es igual a `target`, devuelvo `mid`. Si `nums[mid]` es menor que `target`, entonces el objetivo solo puede estar a la derecha, asi que muevo `left` a `mid + 1`. De lo contrario, el objetivo solo puede estar a la izquierda, asi que muevo `right` a `mid - 1`.

El bucle continua mientras `left <= right`. Si el intervalo queda vacio, el objetivo no esta presente en el arreglo, asi que devuelvo `-1`.

Este enfoque tiene una complejidad temporal de O(log n), porque en cada paso elimina la mitad del espacio de busqueda restante. La complejidad espacial es O(1), porque solo se usan unas pocas variables.
