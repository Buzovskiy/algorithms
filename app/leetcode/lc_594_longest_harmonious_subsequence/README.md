# 594. Longest Harmonious Subsequence

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_594_longest_harmonious_subsequence/README.md)

## Problem Description

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible subsequences.

**Example 1:**
Input: `nums = [1,3,2,2,5,2,3,7]`
Output: `5`
Explanation: The longest harmonious subsequence is `[3,2,2,2,3]`.

**Example 2:**
Input: `nums = [1,2,3,4]`
Output: `2`
Explanation: The longest harmonious subsequences are `[1,2]`, `[2,3]`, and `[3,4]`, all of which have a length of 2.

**Example 3:**
Input: `nums = [1,1,1,1]`
Output: `0`
Explanation: No harmonic subsequence exists.

**Constraints:**
- `1 <= nums.length <= 2 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

## Boilerplate for starting
```python
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        pass
```

## English (Interview Answer)

To solve the Longest Harmonious Subsequence problem, we need to find the length of the longest subsequence where the difference between the maximum and minimum values is exactly 1.

1.  **Count Frequencies**: I use a dictionary to store the frequency of each number in the input array `nums`. This allows us to quickly access the count of any number.
2.  **Iterate and Check**: I iterate through the unique numbers in our frequency dictionary.
3.  **Find Harmonious Pairs**: For each number `num`, I check if `num + 1` also exists in the dictionary. If it does, it means we can form a harmonious subsequence using all occurrences of `num` and `num + 1`.
4.  **Update Maximum**: The length of this harmonious subsequence is the sum of the counts of `num` and `num + 1`. I keep track of the maximum length found during the iteration.
5.  **Return Result**: Finally, I return the maximum length. If no such pair exists, the result remains 0.

This approach has a time complexity of **O(n)** because we traverse the list to build the dictionary and then iterate over the dictionary. The space complexity is **O(n)** to store the frequencies in the dictionary.

## Español (Respuesta para Entrevista)

Para resolver el problema de la Subsecuencia Armoniosa Más Larga (Longest Harmonious Subsequence), necesitamos encontrar la longitud de la subsecuencia más larga donde la diferencia entre los valores máximo y mínimo sea exactamente 1.

1.  **Contar Frecuencias**: Utilizo un diccionario para almacenar la frecuencia de cada número en el arreglo de entrada `nums`. Esto nos permite acceder rápidamente al conteo de cualquier número.
2.  **Iterar y Verificar**: Recorro los números únicos presentes en nuestro diccionario de frecuencias.
3.  **Encontrar Pares Armoniosos**: Para cada número `num`, verifico si `num + 1` también existe en el diccionario. Si existe, significa que podemos formar una subsecuencia armoniosa utilizando todas las ocurrencias de `num` y `num + 1`.
4.  **Actualizar el Máximo**: La longitud de esta subsecuencia armoniosa es la suma de los conteos de `num` y `num + 1`. Mantengo un registro de la longitud máxima encontrada durante la iteración.
5.  **Retornar el Resultado**: Finalmente, retorno la longitud máxima. Si no existe tal par, el resultado permanece en 0.

Este enfoque tiene una complejidad temporal de **O(n)** porque recorremos la lista para construir el diccionario y luego iteramos sobre el diccionario. La complejidad espacial es **O(n)** para almacenar las frecuencias en el diccionario.
