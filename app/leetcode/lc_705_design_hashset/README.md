# 705. Design HashSet
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_705_design_hashset/README.md)

## Problem Description

Design a HashSet without using any built-in hash table libraries.

Implement `MyHashSet` class:

`void add(key)` Inserts the value `key` into the HashSet.

`bool contains(key)` Returns whether the value `key` exists in the HashSet or not.

`void remove(key)` Removes the value `key` in the HashSet. If `key` does not exist in the HashSet, do nothing.

### Example 1

```text
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]
```

### Explanation

```text
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)
```

### Constraints

```text
0 <= key <= 10^6
At most 10^4 calls will be made to add, remove, and contains.
```

## Boilerplate

```python
class MyHashSet:

    def __init__(self):

    def add(self, key: int) -> None:

    def remove(self, key: int) -> None:

    def contains(self, key: int) -> bool:


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
```

## English (Interview Answer)

To solve the Design HashSet problem, I implement my own hash table using an array of buckets. Each bucket is a list that stores the keys whose hash value maps to the same index.

1. In the constructor, I create `1000` empty buckets.
2. For every key, I calculate its bucket index using `key % self.size`.
3. In `add`, I first scan the bucket to check whether the key already exists. If it exists, I do nothing. Otherwise, I append it to the bucket.
4. In `remove`, I scan the bucket and delete the key if I find it.
5. In `contains`, I scan the bucket and return `True` if the key is present, otherwise `False`.

This approach uses separate chaining to handle collisions. The time complexity for `add`, `remove`, and `contains` is O(k), where `k` is the number of elements in the selected bucket. The space complexity is O(n + m), where `n` is the number of stored keys and `m` is the number of buckets.

## Español (Respuesta para Entrevista)

Para resolver el problema Design HashSet, implemento mi propia tabla hash usando un arreglo de buckets. Cada bucket es una lista que guarda las claves cuyo valor hash cae en el mismo índice.

1. En el constructor, creo `1000` buckets vacíos.
2. Para cada clave, calculo el índice del bucket usando `key % self.size`.
3. En `add`, primero recorro el bucket para verificar si la clave ya existe. Si existe, no hago nada. Si no existe, la agrego al bucket.
4. En `remove`, recorro el bucket y elimino la clave si la encuentro.
5. En `contains`, recorro el bucket y devuelvo `True` si la clave está presente; de lo contrario, devuelvo `False`.

Este enfoque usa encadenamiento separado para manejar colisiones. La complejidad temporal de `add`, `remove` y `contains` es O(k), donde `k` es la cantidad de elementos en el bucket seleccionado. La complejidad espacial es O(n + m), donde `n` es la cantidad de claves guardadas y `m` es la cantidad de buckets.
