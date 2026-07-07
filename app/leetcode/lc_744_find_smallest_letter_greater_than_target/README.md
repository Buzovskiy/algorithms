# 744. Find Smallest Letter Greater Than Target
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_744_find_smallest_letter_greater_than_target/README.md)

## Problem Description

You are given an array of characters `letters` that is sorted in non-decreasing order, and a character `target`. There are at least two different characters in `letters`.

Return the smallest character in `letters` that is lexicographically greater than `target`. If such a character does not exist, return the first character in `letters`.

### Example 1

```text
Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
```

### Example 2

```text
Input: letters = ["c","f","j"], target = "c"
Output: "f"
Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
```

### Example 3

```text
Input: letters = ["x","x","y","y"], target = "z"
Output: "x"
Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].
```

### Constraints

```text
2 <= letters.length <= 10^4
letters[i] is a lowercase English letter.
letters is sorted in non-decreasing order.
letters contains at least two different characters.
target is a lowercase English letter.
```

## Boilerplate

```python
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        pass
```

## English (Interview Answer)

To solve Find Smallest Letter Greater Than Target, I use binary search because `letters` is already sorted in non-decreasing order. The goal is to find the first position where the character is strictly greater than `target`.

I keep two pointers, `left` and `right`, where `right` starts at `len(letters)`. On each iteration, I calculate `mid`. If `letters[mid]` is less than or equal to `target`, then that character cannot be the answer, so I move `left` to `mid + 1`. Otherwise, `letters[mid]` is a possible answer, so I move `right` to `mid`.

When the loop finishes, `left` is the insertion position for the next greater letter. If `left` reaches the length of the array, it means there is no greater character, so the answer wraps around to the first character. The expression `letters[left % len(letters)]` handles both the normal case and the wraparound case.

This approach has a time complexity of O(log n), because binary search halves the search space each step. The space complexity is O(1), because only a few variables are used.

## Espanol (Respuesta para Entrevista)

Para resolver Find Smallest Letter Greater Than Target, uso busqueda binaria porque `letters` ya esta ordenado de forma no decreciente. El objetivo es encontrar la primera posicion donde el caracter sea estrictamente mayor que `target`.

Mantengo dos punteros, `left` y `right`, donde `right` empieza en `len(letters)`. En cada iteracion, calculo `mid`. Si `letters[mid]` es menor o igual que `target`, entonces ese caracter no puede ser la respuesta, asi que muevo `left` a `mid + 1`. De lo contrario, `letters[mid]` es una posible respuesta, asi que muevo `right` a `mid`.

Cuando termina el bucle, `left` es la posicion de insercion para la siguiente letra mayor. Si `left` llega al tamano del arreglo, significa que no hay ningun caracter mayor, asi que la respuesta vuelve al primer caracter. La expresion `letters[left % len(letters)]` maneja tanto el caso normal como el caso circular.

Este enfoque tiene una complejidad temporal de O(log n), porque la busqueda binaria reduce a la mitad el espacio de busqueda en cada paso. La complejidad espacial es O(1), porque solo se usan unas pocas variables.
