# 628. Maximum Product of Three Numbers

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_628_maximum_product_of_three_numbers/README.md)

## Problem Description

Given an integer array `nums`, find three numbers whose product is maximum and return the maximum product.

**Example 1:**
- **Input:** `nums = [1,2,3]`
- **Output:** `6`

**Example 2:**
- **Input:** `nums = [1,2,3,4]`
- **Output:** `24`

**Example 3:**
- **Input:** `nums = [-1,-2,-3]`
- **Output:** `-6`

**Constraints:**
- `3 <= nums.length <= 10^4`
- `-1000 <= nums[i] <= 1000`

## Boilerplate

```python
from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pass
```

## English (Interview Answer)

To solve the **Maximum Product of Three Numbers** problem, I sort the array first. After sorting, the maximum product can come from one of two cases:

1.  The three largest numbers in the array.
2.  The two smallest numbers and the largest number, because two negative numbers can produce a large positive product.

The algorithm sorts `nums`, then calculates `first_triplet` using the last three elements and `second_triplet` using the first two elements with the last element. The answer is the maximum of these two products.

**Complexity:**
*   **Time Complexity:** O(N log N), because the array is sorted.
*   **Space Complexity:** O(1) extra space, ignoring the space used internally by the sorting implementation.

## Español (Respuesta para Entrevista)

Para resolver el problema **Producto Máximo de Tres Números**, primero ordeno el arreglo. Después de ordenar, el producto máximo puede venir de uno de dos casos:

1.  Los tres números más grandes del arreglo.
2.  Los dos números más pequeños y el número más grande, porque dos números negativos pueden producir un producto positivo grande.

El algoritmo ordena `nums`, luego calcula `first_triplet` usando los últimos tres elementos y `second_triplet` usando los dos primeros elementos junto con el último elemento. La respuesta es el máximo entre esos dos productos.

**Complejidad:**
*   **Complejidad Temporal:** O(N log N), porque se ordena el arreglo.
*   **Complejidad Espacial:** O(1) de espacio extra, sin contar el espacio usado internamente por la implementación del ordenamiento.

## Українська (Відповідь для співбесіди)

Щоб розв'язати задачу **Maximum Product of Three Numbers**, я спочатку сортую масив. Після сортування максимальний добуток може утворитися в одному з двох випадків:

1.  Три найбільші числа в масиві.
2.  Два найменші числа і найбільше число, тому що два від'ємні числа можуть дати великий додатний добуток.

Алгоритм сортує `nums`, потім обчислює `first_triplet` за допомогою трьох останніх елементів і `second_triplet` за допомогою двох перших елементів разом з останнім елементом. Відповіддю є максимум із цих двох добутків.

**Складність:**
*   **Часова складність:** O(N log N), тому що масив сортується.
*   **Просторова складність:** O(1) додаткової пам'яті, якщо не враховувати пам'ять, яку внутрішньо використовує реалізація сортування.
