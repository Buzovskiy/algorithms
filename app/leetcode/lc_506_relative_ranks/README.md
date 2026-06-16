# 506. Relative Ranks

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_506_relative_ranks/README.md)

## Problem Description
You are given an integer array `score` of size `n`, where `score[i]` is the score of the `ith` athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

- The 1st place athlete's rank is "Gold Medal".
- The 2nd place athlete's rank is "Silver Medal".
- The 3rd place athlete's rank is "Bronze Medal".
- For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array `answer` of size `n` where `answer[i]` is the rank of the `ith` athlete.

**Example 1:**
Input: `score = [5,4,3,2,1]`
Output: `["Gold Medal","Silver Medal","Bronze Medal","4","5"]`
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

**Example 2:**
Input: `score = [10,3,8,9,4]`
Output: `["Gold Medal","5","Bronze Medal","Silver Medal","4"]`
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].

**Constraints:**
- `n == score.length`
- `1 <= n <= 10^4`
- `0 <= score[i] <= 10^6`
- All the values in `score` are unique.

## Boilerplate for starting
```python
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pass
```

## English (Interview Answer)
To solve the "Relative Ranks" problem, we need to assign ranks to athletes based on their scores in descending order.

1.  **Sort the Scores**: First, we create a sorted version of the scores in descending order to determine the placement of each athlete.
2.  **Map Scores to Ranks**: We iterate through the sorted scores. For the first three athletes, we assign the special labels: "Gold Medal", "Silver Medal", and "Bronze Medal". For all subsequent athletes, their rank is simply their placement number (index + 1) converted to a string. We store these mappings in a hash map (dictionary) for quick lookup.
3.  **Construct the Result**: Finally, we iterate through the original `score` array and use our map to retrieve the corresponding rank for each athlete's score, maintaining the original order.

The time complexity is **O(n log n)** due to the sorting step, where n is the number of athletes. The space complexity is **O(n)** to store the ranks in the hash map and the result array.

## Español (Respuesta para Entrevista)
Para resolver el problema de "Relative Ranks" (Rangos Relativos), debemos asignar rangos a los atletas basándonos en sus puntuaciones en orden descendente.

1.  **Ordenar las puntuaciones**: Primero, creamos una versión ordenada de las puntuaciones en orden descendente para determinar la posición de cada atleta.
2.  **Mapear puntuaciones a rangos**: Iteramos a través de las puntuaciones ordenadas. Para los tres primeros atletas, asignamos las etiquetas especiales: "Gold Medal", "Silver Medal" y "Bronze Medal". Para todos los atletas posteriores, su rango es simplemente su número de posición (índice + 1) convertido a cadena de texto. Almacenamos estos mapeos en un mapa hash (diccionario) para una búsqueda rápida.
3.  **Construir el resultado**: Finalmente, recorremos el arreglo `score` original y usamos nuestro mapa para recuperar el rango correspondiente para la puntuación de cada atleta, manteniendo el orden original.

La complejidad temporal es **O(n log n)** debido al paso de ordenación, donde n es el número de atletas. La complejidad espacial es **O(n)** para almacenar los rangos en el mapa hash y el arreglo de resultados.
