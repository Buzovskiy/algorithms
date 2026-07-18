# 888. Fair Candy Swap

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_888_fair_candy_swap/README.md)

## Problem Description
Alice and Bob have a different total number of candies. You are given two integer arrays `aliceSizes` and `bobSizes` where `aliceSizes[i]` is the number of candies of the `ith` box of candy that Alice has and `bobSizes[j]` is the number of candies of the `jth` box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array `answer` where `answer[0]` is the number of candies in the box that Alice must exchange, and `answer[1]` is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.

**Example 1:**
Input: `aliceSizes = [1,1], bobSizes = [2,2]`
Output: `[1,2]`

**Example 2:**
Input: `aliceSizes = [1,2], bobSizes = [2,3]`
Output: `[1,2]`

**Example 3:**
Input: `aliceSizes = [2], bobSizes = [1,3]`
Output: `[2,3]`

**Constraints:**
- `1 <= aliceSizes.length, bobSizes.length <= 10^4`
- `1 <= aliceSizes[i], bobSizes[j] <= 10^5`
- Alice and Bob have a different total number of candies.
- There will be at least one valid answer for the given input.

## Boilerplate for starting
```python
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        pass
```

## English (Interview Answer)
To solve the "Fair Candy Swap" problem, we need to find one box from Alice and one box from Bob such that swapping them makes both total candy counts equal.

The algorithm first calculates Alice's total, Bob's total, and their combined total. The target after the swap is half of the combined total. Then it identifies which person currently has the smaller total and which person has the larger total. For each box from the smaller side, it calculates the exact box size needed from the larger side so that the smaller side reaches the target total after giving away that box and receiving the other one.

If the needed box exists in the larger side's list, the algorithm returns the answer in Alice/Bob order. When Bob has the larger total, the result is `[box_from_alice, box_from_bob]`. When Alice has the larger total, the calculated pair is reversed before returning.

**Complexity Analysis**:
- **Time Complexity**: O(n * m) in the worst case, because checking `diff in maxSize` scans the larger list for each box in the smaller list.
- **Space Complexity**: O(1), excluding the input arrays, because only a few variables are used.

## Español (Respuesta para Entrevista)
Para resolver el problema "Fair Candy Swap", necesitamos encontrar una caja de Alice y una caja de Bob de forma que, al intercambiarlas, ambos terminen con la misma cantidad total de caramelos.

El algoritmo primero calcula el total de Alice, el total de Bob y el total combinado. El objetivo despues del intercambio es la mitad del total combinado. Luego identifica que persona tiene el total menor y que persona tiene el total mayor. Para cada caja del lado con menor total, calcula el tamano exacto de caja que necesita recibir del lado con mayor total para llegar al objetivo despues de entregar esa caja.

Si esa caja necesaria existe en la lista del lado con mayor total, el algoritmo devuelve la respuesta en el orden Alice/Bob. Cuando Bob tiene el total mayor, el resultado es `[caja_de_alice, caja_de_bob]`. Cuando Alice tiene el total mayor, el par calculado se invierte antes de devolverlo.

**Analisis de complejidad**:
- **Complejidad temporal**: O(n * m) en el peor caso, porque la comprobacion `diff in maxSize` recorre la lista mayor por cada caja de la lista menor.
- **Complejidad espacial**: O(1), sin contar los arreglos de entrada, porque solo se usan unas pocas variables.
