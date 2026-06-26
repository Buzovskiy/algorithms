# 645. Set Mismatch

[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_645_set_mismatch/README.md)

## Problem Description
You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: `nums = [1,2,2,4]`
Output: `[2,3]`

**Example 2:**
Input: `nums = [1,1]`
Output: `[1,2]`

**Constraints:**
- `2 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^4`

## Boilerplate for starting
```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        pass
```

## English (Interview Answer)
To solve the "Set Mismatch" problem, I use a dictionary to count how many times each number appears in the input array.

1. I iterate through `nums` and store the frequency of each number in `nums_dict`.
2. While counting, if a number reaches frequency `2`, that number is the duplicated value, so I append it to the output.
3. Then I iterate from `1` to `len(nums)` because the original set should contain every number in that range.
4. The first number from this range that is not present in `nums_dict` is the missing value, so I append it and return the output.

The time complexity is O(n), because the array is traversed once and the range from `1` to `n` is checked once. The space complexity is O(n), because the dictionary stores the numbers seen in the input.

## Espanol (Respuesta para Entrevista)
Para resolver el problema "Set Mismatch", uso un diccionario para contar cuantas veces aparece cada numero en el arreglo de entrada.

1. Recorro `nums` y guardo la frecuencia de cada numero en `nums_dict`.
2. Mientras cuento, si un numero llega a frecuencia `2`, ese numero es el valor duplicado, asi que lo agrego a la salida.
3. Despues recorro desde `1` hasta `len(nums)`, porque el conjunto original deberia contener todos los numeros en ese rango.
4. El primer numero de ese rango que no esta presente en `nums_dict` es el valor faltante, asi que lo agrego y devuelvo la salida.

La complejidad temporal es O(n), porque se recorre el arreglo una vez y tambien se revisa una vez el rango de `1` a `n`. La complejidad espacial es O(n), porque el diccionario guarda los numeros vistos en la entrada.
