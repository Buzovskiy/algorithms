# 896. Monotonic Array
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_896_monotonic_array/README.md)

## Problem Description

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array `nums` is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `true` if the given array is monotonic, or `false` otherwise.

### Example 1

```text
Input: nums = [1,2,2,3]
Output: true
```

### Example 2

```text
Input: nums = [6,5,4,4]
Output: true
```

### Example 3

```text
Input: nums = [1,3,2]
Output: false
```

### Constraints

```text
1 <= nums.length <= 10^5
-10^5 <= nums[i] <= 10^5
```

## Boilerplate

```python
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
```

## English (Interview Answer)

To solve the Monotonic Array problem, I track whether the array has shown an increasing direction or a decreasing direction while scanning it from left to right.

1. I start with two flags, `decreasing` and `increasing`, both set to `False`.
2. For each pair of adjacent values, I compare `nums[i]` with `nums[i-1]`.
3. If the current value is greater, I mark the array as increasing. If it was already marked as decreasing, the array cannot be monotonic, so I return `False`.
4. If the current value is smaller, I mark the array as decreasing. If it was already marked as increasing, I return `False`.
5. Equal adjacent values do not change the direction, so I continue.
6. If the scan finishes without finding both directions, I return `True`.

The time complexity is O(n), where `n` is the length of `nums`, because the array is traversed once. The space complexity is O(1), because only two boolean flags are used.

## Espanol (Respuesta para Entrevista)

Para resolver el problema Monotonic Array, mantengo dos indicadores para saber si el arreglo ha mostrado una direccion creciente o una direccion decreciente mientras lo recorro de izquierda a derecha.

1. Empiezo con dos variables, `decreasing` e `increasing`, ambas en `False`.
2. Para cada par de valores adyacentes, comparo `nums[i]` con `nums[i-1]`.
3. Si el valor actual es mayor, marco el arreglo como creciente. Si ya estaba marcado como decreciente, el arreglo no puede ser monotonico, asi que devuelvo `False`.
4. Si el valor actual es menor, marco el arreglo como decreciente. Si ya estaba marcado como creciente, devuelvo `False`.
5. Los valores adyacentes iguales no cambian la direccion, asi que continuo.
6. Si el recorrido termina sin encontrar ambas direcciones, devuelvo `True`.

La complejidad temporal es O(n), donde `n` es la longitud de `nums`, porque el arreglo se recorre una sola vez. La complejidad espacial es O(1), porque solo se usan dos variables booleanas.
