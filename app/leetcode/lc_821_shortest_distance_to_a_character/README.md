# 821. Shortest Distance to a Character
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_821_shortest_distance_to_a_character/README.md)

## Problem Description

Given a string `s` and a character `c` that occurs in `s`, return an array of integers `answer` where `answer.length == s.length` and `answer[i]` is the distance from index `i` to the closest occurrence of character `c` in `s`.

The distance between two indices `i` and `j` is `abs(i - j)`, where `abs` is the absolute value function.

### Example 1

```text
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
```

### Example 2

```text
Input: s = "aaab", c = "b"
Output: [3,2,1,0]
```

### Constraints

```text
1 <= s.length <= 10^4
s[i] and c are lowercase English letters.
It is guaranteed that c occurs at least once in s.
```

## Boilerplate

```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
```

## English (Interview Answer)

To solve the Shortest Distance to a Character problem, I compute the closest distance from both directions and combine the results.

1. I create an `output` array and a `left_to_right` array.
2. During the left-to-right pass, I keep the most recent index where `c` appeared. If there has been no occurrence yet, I store `None`; otherwise, I store the distance to that most recent occurrence.
3. During the right-to-left pass, I keep the closest occurrence of `c` on the right side and store that distance in `right_to_left`.
4. For every index, I compare the left distance and the right distance. If one side does not exist, I use the other side. If both exist, I take the minimum.
5. The final `output` array contains the distance from each index to the nearest occurrence of `c`.

The time complexity is O(n), where `n` is the length of `s`, because the string is scanned twice. The space complexity is O(n), because the algorithm stores the left-to-right distances, right-to-left distances, and output array.

## Espanol (Respuesta para Entrevista)

Para resolver el problema Shortest Distance to a Character, calculo la distancia mas cercana desde ambas direcciones y combino los resultados.

1. Creo un arreglo `output` y un arreglo `left_to_right`.
2. Durante el recorrido de izquierda a derecha, mantengo el indice mas reciente donde aparecio `c`. Si todavia no hubo ninguna aparicion, guardo `None`; si ya hubo una, guardo la distancia hasta esa aparicion mas reciente.
3. Durante el recorrido de derecha a izquierda, mantengo la aparicion mas cercana de `c` por el lado derecho y guardo esa distancia en `right_to_left`.
4. Para cada indice, comparo la distancia desde la izquierda y la distancia desde la derecha. Si un lado no existe, uso el otro. Si ambos existen, tomo el minimo.
5. El arreglo final `output` contiene la distancia desde cada indice hasta la aparicion mas cercana de `c`.

La complejidad temporal es O(n), donde `n` es la longitud de `s`, porque el string se recorre dos veces. La complejidad espacial es O(n), porque el algoritmo guarda las distancias de izquierda a derecha, las distancias de derecha a izquierda y el arreglo de salida.
