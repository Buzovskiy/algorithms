# 717. 1-bit and 2-bit Characters
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_717_1_bit_and_2_bit_characters/README.md)

## Problem Description

We have two special characters:

The first character can be represented by one bit `0`.
The second character can be represented by two bits (`10` or `11`).

Given a binary array `bits` that ends with `0`, return `true` if the last character must be a one-bit character.

### Example 1

```text
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
```

### Example 2

```text
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
```

### Constraints

```text
1 <= bits.length <= 1000
bits[i] is either 0 or 1.
```

## Boilerplate

```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
```

## English (Interview Answer)

To solve the 1-bit and 2-bit Characters problem, I simulate reading the encoded bits from left to right.

1. I start at index `0`.
2. If the current bit is `0`, then the current character is a one-bit character, so I move one step forward and mark the latest character as one-bit.
3. If the current bit is `1`, then the current character must be a two-bit character, so I move two steps forward and mark the latest character as not one-bit.
4. When the scan finishes, I return whether the last decoded character was a one-bit character.

Because each character moves the index forward by either one or two positions, the time complexity is O(n). The space complexity is O(1), because only the index and a boolean flag are stored.

## Espanol (Respuesta para Entrevista)

Para resolver el problema 1-bit and 2-bit Characters, simulo la lectura de los bits codificados de izquierda a derecha.

1. Empiezo en el indice `0`.
2. Si el bit actual es `0`, entonces el caracter actual es de un bit, avanzo una posicion y marco que el ultimo caracter visto es de un bit.
3. Si el bit actual es `1`, entonces el caracter actual debe ser de dos bits, avanzo dos posiciones y marco que el ultimo caracter visto no es de un bit.
4. Cuando termina el recorrido, devuelvo si el ultimo caracter decodificado fue de un bit.

Como cada caracter hace avanzar el indice una o dos posiciones, la complejidad temporal es O(n). La complejidad espacial es O(1), porque solo se guardan el indice y una bandera booleana.
