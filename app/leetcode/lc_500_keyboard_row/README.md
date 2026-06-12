# 500. Keyboard Row

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_500_keyboard_row/README.md)

## Problem Description
Given an array of strings `words`, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the American keyboard:
- the first row consists of the characters "qwertyuiop",
- the second row consists of the characters "asdfghjkl", and
- the third row consists of the characters "zxcvbnm".

**Example 1:**
Input: `words = ["Hello","Alaska","Dad","Peace"]`
Output: `["Alaska","Dad"]`

**Example 2:**
Input: `words = ["omk"]`
Output: `[]`

**Example 3:**
Input: `words = ["adsdf","sfd"]`
Output: `["adsdf","sfd"]`

**Constraints:**
- `1 <= words.length <= 20`
- `1 <= words[i].length <= 100`
- `words[i]` consists of English letters (both lowercase and uppercase).

## Boilerplate for starting
```python
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        pass
```

## English (Interview Answer)
To solve the "Keyboard Row" problem, we can use set operations in Python to efficiently check if all characters of a word belong to a single keyboard row.

1.  **Define Keyboard Rows**: First, we represent the three rows of an American keyboard as sets of characters. Using sets allows for O(1) average-time complexity for membership checks and subset operations.
2.  **Iterate through Words**: For each word in the input list:
    -   Convert the word to lowercase to handle case insensitivity.
    -   Create a set of characters present in the word.
3.  **Check Subset Property**: Check if this set of characters is a subset of any of the three keyboard row sets. Python's `<=` operator for sets provides a concise way to perform this check.
4.  **Collect Results**: If the word's characters are all contained within one row, append the original word to the result list.

The time complexity of this approach is O(N * K), where N is the number of words and K is the average length of each word, as we process each character once. The space complexity is O(1) because the size of the keyboard rows and the character set for each word (maximum 26 characters) are bounded by a constant.

## Español (Respuesta para Entrevista)
Para resolver el problema de "Keyboard Row", podemos utilizar las operaciones de conjuntos en Python para verificar de manera eficiente si todos los caracteres de una palabra pertenecen a una sola fila del teclado.

1.  **Definir las filas del teclado**: Primero, representamos las tres filas de un teclado estadounidense como conjuntos de caracteres. El uso de conjuntos permite una complejidad de tiempo promedio de O(1) para las comprobaciones de pertenencia y las operaciones de subconjunto.
2.  **Iterar a través de las palabras**: Para cada palabra en la lista de entrada:
    -   Convertimos la palabra a minúsculas para manejar la insensibilidad a mayúsculas y minúsculas.
    -   Creamos un conjunto con los caracteres presentes en la palabra.
3.  **Verificar la propiedad de subconjunto**: Comprobamos si este conjunto de caracteres es un subconjunto de cualquiera de los tres conjuntos de filas del teclado. El operador `<=` de Python para conjuntos proporciona una forma concisa de realizar esta comprobación.
4.  **Recopilar resultados**: Si todos los caracteres de la palabra están contenidos en una sola fila, añadimos la palabra original a la lista de resultados.

La complejidad temporal de este enfoque es O(N * K), donde N es el número de palabras y K es la longitud promedio de cada palabra, ya que procesamos cada carácter una vez. La complejidad espacial es O(1) porque el tamaño de las filas del teclado y el conjunto de caracteres para cada palabra (máximo 26 caracteres) están limitados por una constante.
