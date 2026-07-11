# 806. Number of Lines To Write String
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_806_number_of_lines_to_write_string/README.md)

## Problem Description

You are given a string `s` of lowercase English letters and an array `widths` denoting how many pixels wide each lowercase English letter is. Specifically, `widths[0]` is the width of `'a'`, `widths[1]` is the width of `'b'`, and so on.

You are trying to write `s` across several lines, where each line is no longer than `100` pixels. Starting at the beginning of `s`, write as many letters on the first line such that the total width does not exceed `100` pixels. Then, from where you stopped in `s`, continue writing as many letters as you can on the second line. Continue this process until you have written all of `s`.

Return an array `result` of length `2` where:

`result[0]` is the total number of lines.
`result[1]` is the width of the last line in pixels.

### Example 1

```text
Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explanation: You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.
```

### Example 2

```text
Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
Output: [2,4]
Explanation: You can write s as follows:
bbbcccdddaa  // 98 pixels wide
a            // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.
```

### Constraints

```text
widths.length == 26
2 <= widths[i] <= 10
1 <= s.length <= 1000
s contains only lowercase English letters.
```

## Boilerplate

```python
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
```

## English (Interview Answer)

To solve the Number of Lines To Write String problem, I simulate writing the string from left to right while tracking the width of the current line.

1. I start with `line_number = 1` and `current_width = 0`.
2. For each letter in `s`, I calculate its index with `ord(letter) - ord('a')` and use that index to get the letter width from `widths`.
3. If adding this letter keeps the current line width at `100` pixels or less, I add it to the current line.
4. Otherwise, I start a new line, set the current width to the width of this letter, and increase the line counter.
5. At the end, I return the total number of lines and the width of the last line.

The time complexity is O(n), where `n` is the length of `s`, because each character is processed once. The space complexity is O(1), because only counters are stored.

## Espanol (Respuesta para Entrevista)

Para resolver el problema Number of Lines To Write String, simulo la escritura del string de izquierda a derecha mientras mantengo el ancho de la linea actual.

1. Empiezo con `line_number = 1` y `current_width = 0`.
2. Para cada letra en `s`, calculo su indice con `ord(letter) - ord('a')` y uso ese indice para obtener el ancho de la letra desde `widths`.
3. Si agregar esta letra mantiene el ancho de la linea actual en `100` pixeles o menos, la agrego a la linea actual.
4. Si no, empiezo una nueva linea, asigno el ancho actual al ancho de esta letra e incremento el contador de lineas.
5. Al final, devuelvo el numero total de lineas y el ancho de la ultima linea.

La complejidad temporal es O(n), donde `n` es la longitud de `s`, porque cada caracter se procesa una sola vez. La complejidad espacial es O(1), porque solo se guardan contadores.
