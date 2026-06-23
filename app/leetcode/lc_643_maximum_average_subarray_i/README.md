# 643. Maximum Average Subarray I

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_643_maximum_average_subarray_i/README.md)

## Problem Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than `10^-5` will be accepted.

**Example 1:**
- **Input:** `nums = [1,12,-5,-6,50,3], k = 4`
- **Output:** `12.75000`
- **Explanation:** Maximum average is `(12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75`

**Example 2:**
- **Input:** `nums = [5], k = 1`
- **Output:** `5.00000`

**Constraints:**
- `n == nums.length`
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Boilerplate

```python
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        pass
```

## English (Interview Answer)

To solve **Maximum Average Subarray I**, I check every contiguous subarray of length `k` and keep the largest average found.

For the first window, I calculate the sum by iterating through the first `k` elements. For every next window, I reuse the previous sum by subtracting the element that leaves the window and adding the new element that enters the window. Then I divide the current sum by `k` to get the average and update the answer if this average is greater than the current best value.

This works because all candidate subarrays must have exactly length `k`, so each valid answer is represented by one sliding window.

**Complexity:**
- **Time Complexity:** O(N), because each window is processed once after the initial sum.
- **Space Complexity:** O(1), because only a few variables are used.

## Español (Respuesta para Entrevista)

Para resolver **Maximum Average Subarray I**, reviso cada subarreglo contiguo de longitud `k` y guardo el promedio más grande encontrado.

Para la primera ventana, calculo la suma recorriendo los primeros `k` elementos. Para cada ventana siguiente, reutilizo la suma anterior restando el elemento que sale de la ventana y sumando el nuevo elemento que entra. Después divido la suma actual entre `k` para obtener el promedio y actualizo la respuesta si este promedio es mayor que el mejor valor actual.

Esto funciona porque todos los subarreglos candidatos deben tener exactamente longitud `k`, así que cada respuesta válida está representada por una ventana deslizante.

**Complejidad:**
- **Complejidad Temporal:** O(N), porque cada ventana se procesa una vez después de la suma inicial.
- **Complejidad Espacial:** O(1), porque solo se usan unas pocas variables.
