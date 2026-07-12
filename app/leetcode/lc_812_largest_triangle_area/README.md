# 812. Largest Triangle Area
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_812_largest_triangle_area/README.md)

## Problem Description

Given an array of points on the X-Y plane `points` where `points[i] = [xi, yi]`, return the area of the largest triangle that can be formed by any three different points.

Answers within `10^-5` of the actual answer will be accepted.

### Example 1

```text
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the figure. The red triangle is the largest.
```

### Example 2

```text
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
```

### Constraints

```text
3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
```

## Boilerplate

```python
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
```

## English (Interview Answer)

To solve the Largest Triangle Area problem, I check every possible group of three different points and calculate the area of the triangle formed by them.

The area is calculated using the coordinate formula:

```text
area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
```

1. I initialize `s_max` with `0`.
2. I use three nested loops to choose three different points.
3. For each valid triplet, I extract the `x` and `y` coordinates.
4. I calculate the triangle area using the formula above.
5. I keep the maximum area found so far in `s_max`.
6. After checking all triplets, I return `s_max`.

The time complexity is O(n^3), because every combination of three points is checked by the nested loops. The space complexity is O(1), because only a few variables are used.

## Español (Respuesta para Entrevista)

Para resolver el problema Largest Triangle Area, reviso todos los posibles grupos de tres puntos diferentes y calculo el area del triangulo formado por ellos.

El area se calcula usando la formula de coordenadas:

```text
area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
```

1. Inicializo `s_max` con `0`.
2. Uso tres bucles anidados para escoger tres puntos diferentes.
3. Para cada tripleta valida, extraigo las coordenadas `x` e `y`.
4. Calculo el area del triangulo usando la formula anterior.
5. Mantengo el area maxima encontrada hasta el momento en `s_max`.
6. Despues de revisar todas las tripletas, devuelvo `s_max`.

La complejidad temporal es O(n^3), porque los bucles anidados revisan cada combinacion de tres puntos. La complejidad espacial es O(1), porque solo se usan algunas variables.
