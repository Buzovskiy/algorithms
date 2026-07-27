# 905. Sort Array By Parity
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_905_sort_array_by_parity/README.md)

## Problem Description

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

### Example 1

```text
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

### Example 2

```text
Input: nums = [0]
Output: [0]
```

### Constraints

```text
1 <= nums.length <= 5000
0 <= nums[i] <= 5000
```

## Boilerplate

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
```

## English (Interview Answer)

To solve the Sort Array By Parity problem, I use two pointers to partition the array in place.

1. I keep a `left` pointer at the position where the next even number should be placed.
2. I scan the array with a `right` pointer from the beginning to the end.
3. Whenever `nums[right]` is even, I swap it with `nums[left]`.
4. After placing an even number, I move `left` one step forward.
5. At the end, all even numbers are before all odd numbers, so I return `nums`.

The time complexity is O(n), where `n` is the length of `nums`, because each element is visited once. The space complexity is O(1), because the array is rearranged in place.

## Espanol (Respuesta)

Para resolver el problema Sort Array By Parity, uso dos punteros para particionar el arreglo en el mismo lugar.

1. Mantengo un puntero `left` en la posicion donde debe colocarse el siguiente numero par.
2. Recorro el arreglo con un puntero `right` desde el inicio hasta el final.
3. Cada vez que `nums[right]` es par, lo intercambio con `nums[left]`.
4. Despues de colocar un numero par, avanzo `left` una posicion.
5. Al final, todos los numeros pares quedan antes que todos los numeros impares, asi que devuelvo `nums`.

La complejidad temporal es O(n), donde `n` es la longitud de `nums`, porque cada elemento se visita una sola vez. La complejidad espacial es O(1), porque el arreglo se reorganiza en el mismo lugar.
