# 747. Largest Number At Least Twice of Others
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_747_largest_number_at_least_twice_of_others/README.md)

## Problem Description

You are given an integer array `nums` where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return `-1` otherwise.

### Example 1

```text
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer.
For every other number in the array x, 6 is at least twice as big as x.
The index of value 6 is 1, so we return 1.
```

### Example 2

```text
Input: nums = [1,2,3,4]
Output: -1
Explanation: 4 is less than twice the value of 3, so we return -1.
```

### Constraints

```text
2 <= nums.length <= 50
0 <= nums[i] <= 100
The largest element in nums is unique.
```

## Boilerplate

```python
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        pass
```

## English (Interview Answer)

To solve this problem, I first find the largest number and remember its index. Since the problem states that the largest number is unique, this index is the only possible answer.

Then I make a second pass through the array to find the largest number that is not equal to the maximum. While doing that, I check whether the maximum is smaller than twice this second-largest value. If that happens, the largest number is not at least twice every other number, so I return `-1`.

If the check never fails, the largest number satisfies the condition, and I return its index.

The time complexity is O(n), because the array is traversed twice. The space complexity is O(1), because only a few variables are used.

## Español (Respuesta para Entrevista)

Para resolver este problema, primero busco el número más grande y guardo su índice. Como el enunciado dice que el número más grande es único, ese índice es la única respuesta posible.

Después hago una segunda pasada por el arreglo para encontrar el número más grande que no sea igual al máximo. Mientras hago eso, compruebo si el máximo es menor que dos veces este segundo valor más grande. Si eso ocurre, el número más grande no es al menos el doble de todos los demás números, así que devuelvo `-1`.

Si la comprobación nunca falla, el número más grande cumple la condición y devuelvo su índice.

La complejidad temporal es O(n), porque el arreglo se recorre dos veces. La complejidad espacial es O(1), porque solo se usan unas pocas variables.
