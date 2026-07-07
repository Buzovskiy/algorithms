# 746. Min Cost Climbing Stairs
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_746_min_cost_climbing_stairs/README.md)

## Problem Description

You are given an integer array `cost` where `cost[i]` is the cost of `ith` step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index `0`, or the step with index `1`.

Return the minimum cost to reach the top of the floor.

### Example 1

```text
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
```

### Example 2

```text
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
```

### Constraints

```text
2 <= cost.length <= 1000
0 <= cost[i] <= 999
```

## Boilerplate

```python
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
```

## English (Interview Answer)

To solve the Min Cost Climbing Stairs problem, I use dynamic programming from the end of the staircase toward the beginning. For each step, I calculate the minimum total cost needed if I start from that step.

I create a `dp` array with the same length as `cost`. The last step costs `cost[-1]`, and the second-to-last step costs `cost[-2]`, because from either of those positions I can reach the top directly after paying that step's cost.

Then I move backward through the remaining steps. For each index `ii`, the cost is `cost[ii]` plus the minimum between the cost of moving to the next step, `dp[ii+1]`, and the cost of jumping two steps, `dp[ii+2]`.

At the end, since I am allowed to start at either index `0` or index `1`, I return `min(dp[0], dp[1])`.

The time complexity is O(n), because each step is processed once. The space complexity is O(n), because the algorithm stores the dynamic programming result for every step.

## Espanol (Respuesta para Entrevista)

Para resolver el problema Min Cost Climbing Stairs, uso programacion dinamica desde el final de la escalera hacia el principio. Para cada escalon, calculo el costo total minimo necesario si empiezo desde ese escalon.

Creo un arreglo `dp` con la misma longitud que `cost`. El ultimo escalon cuesta `cost[-1]`, y el penultimo escalon cuesta `cost[-2]`, porque desde cualquiera de esas posiciones puedo llegar directamente a la cima despues de pagar el costo de ese escalon.

Luego recorro hacia atras los escalones restantes. Para cada indice `ii`, el costo es `cost[ii]` mas el minimo entre avanzar al siguiente escalon, `dp[ii+1]`, y saltar dos escalones, `dp[ii+2]`.

Al final, como se permite empezar en el indice `0` o en el indice `1`, devuelvo `min(dp[0], dp[1])`.

La complejidad temporal es O(n), porque cada escalon se procesa una vez. La complejidad espacial es O(n), porque el algoritmo guarda el resultado de programacion dinamica para cada escalon.
