# 697. Degree of an Array
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_697_degree_of_an_array/README.md)

## Problem Description

Given a non-empty array of non-negative integers `nums`, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a contiguous subarray of `nums` that has the same degree as `nums`.

### Example 1

Input: `nums = [1,2,2,3,1]`

Output: `2`

Explanation: The input array has a degree of 2 because both elements 1 and 2 appear twice. Of the subarrays that have the same degree, the shortest length is 2, so return 2.

### Example 2

Input: `nums = [1,2,2,3,1,4,2]`

Output: `6`

Explanation: The degree is 3 because the element 2 is repeated 3 times. So `[2,2,3,1,4,2]` is the shortest subarray, therefore returning 6.

### Constraints

- `nums.length` will be between 1 and 50,000.
- `nums[i]` will be an integer between 0 and 49,999.

## Boilerplate

```python
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        pass
```

## English (Interview Answer)

To solve this problem, I track the frequency of each number and identify the degree of the whole array, which is the highest frequency among all numbers. At the same time, I store indexes for each number so I can later calculate the length between its first and last occurrence.

While iterating through `nums`, I update the frequency in `degrees`. If a number reaches or exceeds the current maximum degree, I store its current index. When a number becomes the new maximum degree, I reset the candidate set and keep only that number. If another number has the same maximum degree, I add it to the candidate set.

After the loop, every number in `num_set` has the same degree as the full array. For each of those numbers, I calculate the subarray length from its first stored index to its last stored index. The answer is the minimum of those lengths.

The time complexity is O(n), because the array is traversed once and then only the maximum-degree candidates are checked. The space complexity is O(n), because dictionaries and sets are used to store frequencies, indexes, and candidate numbers.

## Español (Respuesta para Entrevista)

Para resolver este problema, guardo la frecuencia de cada número e identifico el grado del arreglo completo, que es la frecuencia más alta entre todos los números. Al mismo tiempo, guardo índices para cada número para poder calcular después la longitud entre su primera y su última aparición.

Mientras recorro `nums`, actualizo la frecuencia en `degrees`. Si un número alcanza o supera el grado máximo actual, guardo su índice actual. Cuando un número se convierte en el nuevo grado máximo, reinicio el conjunto de candidatos y dejo solo ese número. Si otro número tiene el mismo grado máximo, lo agrego al conjunto de candidatos.

Después del recorrido, cada número en `num_set` tiene el mismo grado que el arreglo completo. Para cada uno de esos números, calculo la longitud del subarreglo desde su primer índice guardado hasta su último índice guardado. La respuesta es el mínimo de esas longitudes.

La complejidad temporal es O(n), porque se recorre el arreglo una vez y luego solo se revisan los candidatos con grado máximo. La complejidad espacial es O(n), porque se usan diccionarios y conjuntos para guardar frecuencias, índices y números candidatos.
