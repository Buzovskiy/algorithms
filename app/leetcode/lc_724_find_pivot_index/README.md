# 724. Find Pivot Index
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_724_find_pivot_index/README.md)

## Problem Description

Given an array of integers `nums`, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return `-1`.

### Example 1

```text
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
```

### Example 2

```text
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```

### Example 3

```text
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
```

### Constraints

```text
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
```

## Boilerplate

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
```

## English (Interview Answer)

To solve the Find Pivot Index problem, I use the total sum of the array and maintain a running sum of the elements on the left side.

1. First, I calculate `total`, the sum of all numbers in `nums`.
2. I initialize `left_sum` as `0`, because there are no elements to the left of the first index.
3. For each index, I calculate the right sum as `total - left_sum - num`.
4. If `left_sum` is equal to `right_sum`, the current index is the pivot index, so I return it immediately.
5. If not, I add the current number to `left_sum` and continue.
6. If no pivot index is found, I return `-1`.

Because I scan the array from left to right and return immediately when the condition is met, the returned index is the leftmost pivot index. The time complexity is O(n), and the space complexity is O(1).

## Español (Respuesta para Entrevista)

Para resolver el problema Find Pivot Index, uso la suma total del arreglo y mantengo una suma acumulada de los elementos que están a la izquierda.

1. Primero calculo `total`, la suma de todos los números en `nums`.
2. Inicializo `left_sum` como `0`, porque no hay elementos a la izquierda del primer índice.
3. Para cada índice, calculo la suma derecha como `total - left_sum - num`.
4. Si `left_sum` es igual a `right_sum`, el índice actual es el índice pivote, así que lo devuelvo inmediatamente.
5. Si no son iguales, agrego el número actual a `left_sum` y continúo.
6. Si no encuentro ningún índice pivote, devuelvo `-1`.

Como recorro el arreglo de izquierda a derecha y devuelvo el resultado apenas encuentro la condición, el índice devuelto es el pivote más a la izquierda. La complejidad temporal es O(n), y la complejidad espacial es O(1).
