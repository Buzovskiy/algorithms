# 599. Minimum Index Sum of Two Lists

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_599_minimum_index_sum_of_two_lists/README.md)

## Problem Description

Given two arrays of strings `list1` and `list2`, find the common strings with the least index sum.

A common string is a string that appeared in both `list1` and `list2`.

A common string with the least index sum is a common string such that if it appeared at `list1[i]` and `list2[j]` then `i + j` should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

**Example 1:**
- **Input:** `list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]`
- **Output:** `["Shogun"]`
- **Explanation:** The only common string is "Shogun".

**Example 2:**
- **Input:** `list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]`
- **Output:** `["Shogun"]`
- **Explanation:** The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

**Example 3:**
- **Input:** `list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]`
- **Output:** `["sad","happy"]`
- **Explanation:** There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".

**Constraints:**
- `1 <= list1.length, list2.length <= 1000`
- `1 <= list1[i].length, list2[i].length <= 30`
- `list1[i]` and `list2[i]` consist of spaces ' ' and English letters.
- All the strings of `list1` are unique.
- All the strings of `list2` are unique.
- There is at least a common string between `list1` and `list2`.

## Boilerplate

```python
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pass
```

## English (Interview Answer)

To solve the **Minimum Index Sum of Two Lists** problem, we need to find common elements between two lists that have the smallest combined index sum.

1.  **Use a Hash Map:** First, I store all elements of one list (e.g., `list2`) in a hash map where the keys are the strings and the values are their corresponding indices. This allows for O(1) average-time lookups.
2.  **Iterate and Calculate:** I then iterate through the first list (`list1`). For each element, I check if it exists in the hash map.
3.  **Track the Minimum Sum:**
    *   If a common element is found, I calculate the sum of its indices from both lists.
    *   If this sum is smaller than the current `least_sum`, I clear the previous results and add this element as the new best candidate.
    *   If the sum equals the `least_sum`, I simply add it to the result list.
4.  **Efficiency:** This approach ensures we find all elements with the minimum index sum in a single pass through the first list.

**Complexity:**
*   **Time Complexity:** O(N + M), where N and M are the lengths of `list1` and `list2`. We iterate through each list once.
*   **Space Complexity:** O(M) to store the elements of `list2` in the hash map.

## Español (Respuesta para Entrevista)

Para resolver el problema de **Suma Mínima de Índices de Dos Listas**, debemos encontrar los elementos comunes entre dos listas que tengan la menor suma combinada de sus índices.

1.  **Usar un Mapa Hash:** Primero, almaceno todos los elementos de una lista (por ejemplo, `list2`) en un mapa hash donde las claves son las cadenas y los valores son sus índices correspondientes. Esto permite búsquedas en tiempo promedio O(1).
2.  **Iterar y Calcular:** Luego, recorro la primera lista (`list1`). Para cada elemento, verifico si existe en el mapa hash.
3.  **Rastrear la Suma Mínima:**
    *   Si se encuentra un elemento común, calculo la suma de sus índices en ambas listas.
    *   Si esta suma es menor que la `least_sum` actual, vacío los resultados anteriores y agrego este elemento como el nuevo mejor candidato.
    *   Si la suma es igual a la `least_sum`, simplemente lo agrego a la lista de resultados.
4.  **Eficiencia:** Este enfoque garantiza que encontremos todos los elementos con la suma de índices mínima en una sola pasada por la primera lista.

**Complejidad:**
*   **Complejidad Temporal:** O(N + M), donde N y M son las longitudes de `list1` y `list2`. Recorremos cada lista una vez.
*   **Complejidad Espacial:** O(M) para almacenar los elementos de `list2` en el mapa hash.
