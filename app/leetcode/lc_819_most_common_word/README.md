# 819. Most Common Word
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_819_most_common_word/README.md)

## Problem Description

Given a string `paragraph` and a string array of the banned words `banned`, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in `paragraph` are case-insensitive and the answer should be returned in lowercase.

Note that words can not contain punctuation symbols.

### Example 1

```text
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation:
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph.
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"),
and that "hit" isn't the answer even though it occurs more because it is banned.
```

### Example 2

```text
Input: paragraph = "a.", banned = []
Output: "a"
```

### Constraints

```text
1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
```

## Boilerplate

```python
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
```

## English (Interview Answer)

To solve the Most Common Word problem, I first normalize the paragraph so punctuation does not stay attached to words. Then I count every lowercase word and keep track of the most frequent word that is not in the banned list.

1. I replace each punctuation symbol with a space.
2. I convert the paragraph to lowercase and split it into words.
3. For each word, I update its frequency in a dictionary.
4. If the word is not banned and its frequency is greater than the current maximum, I update the answer.
5. At the end, I return the most frequent non-banned word.

The time complexity is O(n + m), where `n` is the length of `paragraph` and `m` is the number of parsed words, because the paragraph is scanned and each word is counted. The space complexity is O(k), where `k` is the number of distinct words stored in the dictionary.

## Espanol

Para resolver el problema Most Common Word, primero normalizo el parrafo para que los signos de puntuacion no queden unidos a las palabras. Luego cuento cada palabra en minusculas y mantengo la palabra mas frecuente que no este en la lista de palabras prohibidas.

1. Reemplazo cada signo de puntuacion por un espacio.
2. Convierto el parrafo a minusculas y lo divido en palabras.
3. Para cada palabra, actualizo su frecuencia en un diccionario.
4. Si la palabra no esta prohibida y su frecuencia es mayor que el maximo actual, actualizo la respuesta.
5. Al final, devuelvo la palabra no prohibida mas frecuente.

La complejidad temporal es O(n + m), donde `n` es la longitud de `paragraph` y `m` es el numero de palabras procesadas, porque se escanea el parrafo y se cuenta cada palabra. La complejidad espacial es O(k), donde `k` es el numero de palabras distintas guardadas en el diccionario.
