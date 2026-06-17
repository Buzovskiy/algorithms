# 575. Distribute Candies

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_575_distribute_candies/README.md)

## Problem Description
Alice has `n` candies, where the `ith` candy is of type `candyType[i]`. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat `n / 2` of the candies she has (`n` is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array `candyType` of length `n`, return the maximum number of different types of candies she can eat if she only eats `n / 2` of them.

**Example 1:**
Input: `candyType = [1,1,2,2,3,3]`
Output: `3`
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

**Example 2:**
Input: `candyType = [1,1,2,3]`
Output: `2`
Explanation: Alice can only eat 4 / 2 = 2 candies. Whether she eats types [1,2], [1,3], or [2,3], she still can only eat 2 different types.

**Example 3:**
Input: `candyType = [6,6,6,6]`
Output: `1`
Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.

**Constraints:**
- `n == candyType.length`
- `2 <= n <= 10^4`
- `n` is even.
- `-10^5 <= candyType[i] <= 10^5`

## Boilerplate for starting
```python
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        pass
```

## English (Interview Answer)
To solve the "Distribute Candies" problem, we need to find the maximum number of unique candy types Alice can eat, given the constraint that she can only eat half of her total candies (`n / 2`).

1.  **Count Unique Types**: First, we determine how many different types of candies are available. We can do this by converting the `candyType` array into a set, as sets only store unique elements.
2.  **Compare with Limit**: Alice's consumption is limited by two factors:
    -   The total number of unique types available (`len(set(candyType))`).
    -   The doctor's advice, which limits her to `n / 2` candies total.
3.  **Determine the Result**: The maximum number of different types she can eat is the smaller of these two values. If the number of unique types is less than `n / 2`, she can eat one of each type. If there are more unique types than `n / 2`, she is capped at `n / 2` by the doctor's advice.

**Complexity Analysis**:
-   **Time Complexity**: O(n), where n is the length of the `candyType` array. Building the set requires one pass through the array.
-   **Space Complexity**: O(n) in the worst case (when all candies are of different types) to store the set of unique candy types.

## Español (Respuesta para Entrevista)
Para resolver el problema "Distribute Candies", necesitamos encontrar el número máximo de tipos únicos de caramelos que Alice puede comer, dada la restricción de que solo puede comer la mitad de sus caramelos totales (`n / 2`).

1.  **Contar tipos únicos**: Primero, determinamos cuántos tipos diferentes de caramelos hay disponibles. Podemos hacer esto convirtiendo el arreglo `candyType` en un conjunto (set), ya que los conjuntos solo almacenan elementos únicos.
2.  **Comparar con el límite**: El consumo de Alice está limitado por dos factores:
    -   El número total de tipos únicos disponibles (`len(set(candyType))`).
    -   El consejo del médico, que le limita a un total de `n / 2` caramelos.
3.  **Determinar el resultado**: El número máximo de tipos diferentes que puede comer es el menor de estos dos valores. Si el número de tipos únicos es menor que `n / 2`, puede comer uno de cada tipo. Si hay más tipos únicos que `n / 2`, está limitada a `n / 2` por el consejo del médico.

**Análisis de complejidad**:
-   **Complejidad temporal**: O(n), donde n es la longitud del arreglo `candyType`. La creación del conjunto requiere una pasada por el arreglo.
-   **Complejidad espacial**: O(n) en el peor de los casos (cuando todos los caramelos son de tipos diferentes) para almacenar el conjunto de tipos únicos.
