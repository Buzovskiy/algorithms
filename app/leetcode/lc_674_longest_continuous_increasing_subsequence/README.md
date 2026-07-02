# 674. Longest Continuous Increasing Subsequence

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_674_longest_continuous_increasing_subsequence/README.md)

## Problem Description

Given an unsorted array of integers `nums`, return the length of the longest continuous increasing subsequence, also known as a subarray. The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices `l` and `r` (`l < r`) such that it is `[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]` and for each `l <= i < r`, `nums[i] < nums[i + 1]`.

**Example 1:**
- **Input:** `nums = [1,3,5,4,7]`
- **Output:** `3`
- **Explanation:** The longest continuous increasing subsequence is `[1,3,5]` with length `3`. Even though `[1,3,5,7]` is an increasing subsequence, it is not continuous because elements `5` and `7` are separated by element `4`.

**Example 2:**
- **Input:** `nums = [2,2,2,2,2]`
- **Output:** `1`
- **Explanation:** The longest continuous increasing subsequence is `[2]` with length `1`. It must be strictly increasing.

**Constraints:**
- `1 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Boilerplate

```python
from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        pass
```

## English (Interview Answer)

To solve **Longest Continuous Increasing Subsequence**, I scan the array once and keep the length of the current continuous increasing segment.

I use `last` to remember the previous number. If the current number is greater than `last`, then the current increasing segment continues, so I increment `current`. Otherwise, the sequence breaks and I reset `current` to `1`, because the current number can start a new segment. After each step, I update `output` with the maximum value between the previous answer and the current segment length.

This works because the subsequence must be continuous, so every decision only depends on the current number and the number immediately before it.

**Complexity:**
- **Time Complexity:** O(N), because the array is traversed once.
- **Space Complexity:** O(1), because only a few variables are used.

## Español (Respuesta para Entrevista)

Para resolver **Longest Continuous Increasing Subsequence**, recorro el arreglo una sola vez y mantengo la longitud del segmento creciente continuo actual.

Uso `last` para recordar el número anterior. Si el número actual es mayor que `last`, entonces el segmento creciente actual continúa, así que incremento `current`. En caso contrario, la secuencia se rompe y reinicio `current` a `1`, porque el número actual puede iniciar un nuevo segmento. Después de cada paso, actualizo `output` con el máximo entre la respuesta anterior y la longitud del segmento actual.

Esto funciona porque la subsecuencia debe ser continua, así que cada decisión depende solo del número actual y del número inmediatamente anterior.

**Complejidad:**
- **Complejidad Temporal:** O(N), porque el arreglo se recorre una sola vez.
- **Complejidad Espacial:** O(1), porque solo se usan unas pocas variables.
