# 804. Unique Morse Code Words
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_804_unique_morse_code_words/README.md)

## Problem Description

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

- `'a'` maps to `".-"`
- `'b'` maps to `"-..."`
- `'c'` maps to `"-.-."`, and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

```text
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
```

Given an array of strings `words` where each word can be written as a concatenation of the Morse code of each letter.

For example, `"cab"` can be written as `"-.-..--..."`, which is the concatenation of `"-.-."`, `".-"`, and `"-..."`. We will call such a concatenation the transformation of a word.

Return the number of different transformations among all words we have.

### Example 1:
**Input:** `words = ["gin","zen","gig","msg"]`  
**Output:** `2`  
**Explanation:** The transformation of each word is:
- `"gin"` -> `"--...-."`
- `"zen"` -> `"--...-."`
- `"gig"` -> `"--...--."`
- `"msg"` -> `"--...--."`

There are 2 different transformations: `"--...-."` and `"--...--."`.

### Example 2:
**Input:** `words = ["a"]`  
**Output:** `1`

### Constraints:
- `1 <= words.length <= 100`
- `1 <= words[i].length <= 12`
- `words[i]` consists of lowercase English letters.

## Boilerplate

```python
from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        pass
```

## English (Interview Answer)

To solve the Unique Morse Code Words problem, I transform each word from the input list into its Morse code representation and then count how many unique transformations exist.

1. I use a predefined list containing the Morse code for each of the 26 lowercase English letters.
2. For each word in the input, I iterate through its characters. For each character, I calculate its index in the alphabet (e.g., `'a'` is 0, `'b'` is 1) using the `ord()` function and retrieve the corresponding Morse code.
3. I concatenate these Morse codes to form the complete transformation of the word.
4. I store all these transformations in a list (or directly in a set).
5. Finally, I use a set to filter out duplicate transformations and return its size.

The time complexity is O(N * L), where N is the number of words and L is the average length of each word, as I must process every character of every word. The space complexity is also O(N * L) in the worst case to store the transformed strings.

## Español (Respuesta para Entrevista)

Para resolver el problema de las Palabras Únicas en Código Morse, transformo cada palabra de la lista de entrada a su representación en código morse y luego cuento cuántas transformaciones únicas existen.

1. Utilizo una lista predefinida que contiene el código Morse de cada una de las 26 letras minúsculas del alfabeto inglés.
2. Para cada palabra en la entrada, recorro sus caracteres. Para cada carácter, calculo su índice en el alfabeto (por ejemplo, 'a' es 0, 'b' es 1) usando la función `ord()` y obtengo el código Morse correspondiente.
3. Concateno estos códigos Morse para formar la transformación completa de la palabra.
4. Almaceno todas estas transformaciones en una lista (o directamente en un conjunto).
5. Finalmente, utilizo un conjunto (set) para filtrar las transformaciones duplicadas y devuelvo su tamaño.

La complejidad temporal es O(N * L), donde N es el número de palabras y L es la longitud promedio de cada palabra, ya que debo procesar cada carácter de cada palabra. La complejidad espacial también es O(N * L) en el peor caso para almacenar las cadenas transformadas.
