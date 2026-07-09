# 748. Shortest Completing Word

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_748_shortest_completing_word/README.md)

## Problem Description
Given a string `licensePlate` and an array of strings `words`, find the shortest completing word in `words`.

A completing word is a word that contains all the letters in `licensePlate`. Ignore numbers and spaces in `licensePlate`, and treat letters as case insensitive. If a letter appears more than once in `licensePlate`, then it must appear in the word the same number of times or more.

For example, if `licensePlate = "aBc 12c"`, then it contains letters `'a'`, `'b'` (ignoring case), and `'c'` twice. Possible completing words are `"abccdef"`, `"caaacab"`, and `"cbca"`.

Return the shortest completing word in `words`. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in `words`.

**Example 1:**
Input: `licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]`
Output: `"steps"`
Explanation: `licensePlate` contains letters `'s'`, `'p'`, `'s'` (ignoring case), and `'t'`.
`"step"` contains `'t'` and `'p'`, but only contains 1 `'s'`.
`"steps"` contains `'t'`, `'p'`, and both `'s'` characters.
`"stripe"` is missing an `'s'`.
`"stepple"` is missing an `'s'`.
Since `"steps"` is the only word containing all the letters, that is the answer.

**Example 2:**
Input: `licensePlate = "1s3 456", words = ["looks","pest","stew","show"]`
Output: `"pest"`
Explanation: `licensePlate` only contains the letter `'s'`. All the words contain `'s'`, but among these `"pest"`, `"stew"`, and `"show"` are shortest. The answer is `"pest"` because it is the word that appears earliest of the 3.

## Boilerplate for starting
```python
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        pass
```

## English (Interview Answer)
To solve the "Shortest Completing Word" problem, I first extract the letters from `licensePlate`, ignore digits and spaces, convert everything to lowercase, and count how many times each required letter appears.

Then I build a frequency dictionary for each word in `words`, also in lowercase. After that, I iterate through these word counts and check whether every required letter from the license plate exists in the current word with at least the needed frequency.

When a word satisfies all required counts, it is a completing word. I keep it as the current answer only if there is no previous answer or if it is shorter than the current answer. Since I do not replace the answer when the lengths are equal, the algorithm naturally keeps the first shortest completing word from the original list.

The time complexity is O(L + W * K), where L is the length of `licensePlate`, W is the number of words, and K is the average length of a word. The space complexity is O(W * A) for the stored word frequency dictionaries, where A is the number of distinct letters in a word.

## Espanol (Respuesta para Entrevista)
Para resolver el problema "Shortest Completing Word", primero extraigo las letras de `licensePlate`, ignoro los numeros y espacios, convierto todo a minusculas y cuento cuantas veces aparece cada letra requerida.

Despues construyo un diccionario de frecuencias para cada palabra en `words`, tambien en minusculas. Luego recorro esos conteos y verifico que cada letra requerida por la matricula exista en la palabra actual con al menos la frecuencia necesaria.

Cuando una palabra cumple todos los conteos requeridos, es una palabra completadora. La guardo como respuesta actual solo si todavia no hay respuesta o si es mas corta que la respuesta actual. Como no reemplazo la respuesta cuando las longitudes son iguales, el algoritmo conserva naturalmente la primera palabra completadora mas corta segun el orden original de la lista.

La complejidad temporal es O(L + W * K), donde L es la longitud de `licensePlate`, W es la cantidad de palabras y K es la longitud promedio de una palabra. La complejidad espacial es O(W * A) por los diccionarios de frecuencias almacenados para las palabras, donde A es la cantidad de letras distintas en una palabra.
