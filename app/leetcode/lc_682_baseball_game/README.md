# 682. Baseball Game
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_682_baseball_game/README.md)

## Problem Description

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings `operations`, where `operations[i]` is the ith operation you must apply to the record and is one of the following:

- An integer `x`: record a new score of `x`.
- `"+"`: record a new score that is the sum of the previous two scores.
- `"D"`: record a new score that is double the previous score.
- `"C"`: invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

### Example 1

```text
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
```

### Example 2

```text
Input: ops = ["5","-2","4","C","D","9","+","+"]
Output: 27
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
```

### Example 3

```text
Input: ops = ["1","C"]
Output: 0
Explanation:
"1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.
```

### Constraints

- `1 <= operations.length <= 1000`
- `operations[i]` is `"C"`, `"D"`, `"+"`, or a string representing an integer in the range `[-3 * 10^4, 3 * 10^4]`.
- For operation `"+"`, there will always be at least two previous scores on the record.
- For operations `"C"` and `"D"`, there will always be at least one previous score on the record.

## Boilerplate

```python
from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
```

## English (Interview Answer)

To solve the Baseball Game problem, I use a stack to keep the valid scores in order. Each operation either adds a new score, removes the last score, doubles the last score, or adds the sum of the previous two scores.

1. I create an empty stack for the score record.
2. I iterate through each operation in `operations`.
3. If the operation is `"C"`, I remove the last score from the stack.
4. If the operation is `"D"`, I append double the previous score.
5. If the operation is `"+"`, I append the sum of the previous two scores.
6. Otherwise, the operation is an integer string, so I convert it to an integer and append it.
7. At the end, I return the sum of all values in the stack, or `0` if the stack is empty.

This approach has a time complexity of O(n), because each operation is processed once. The space complexity is O(n), because in the worst case every operation can add a score to the stack.

## Español (Respuesta para Entrevista)

Para resolver el problema Baseball Game, uso una pila para mantener las puntuaciones válidas en orden. Cada operación agrega una nueva puntuación, elimina la última puntuación, duplica la última puntuación o agrega la suma de las dos puntuaciones anteriores.

1. Creo una pila vacía para guardar el registro de puntuaciones.
2. Recorro cada operación en `operations`.
3. Si la operación es `"C"`, elimino la última puntuación de la pila.
4. Si la operación es `"D"`, agrego el doble de la puntuación anterior.
5. Si la operación es `"+"`, agrego la suma de las dos puntuaciones anteriores.
6. Si no, la operación es una cadena que representa un entero, así que la convierto a entero y la agrego.
7. Al final, devuelvo la suma de todos los valores en la pila, o `0` si la pila está vacía.

Este enfoque tiene una complejidad temporal de O(n), porque cada operación se procesa una sola vez. La complejidad espacial es O(n), porque en el peor caso cada operación puede agregar una puntuación a la pila.
