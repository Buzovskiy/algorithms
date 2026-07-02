# 706. Design HashMap
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_706_design_hashmap/README.md)

## Problem Description

Design a HashMap without using any built-in hash table libraries.

Implement the `MyHashMap` class:

`MyHashMap()` initializes the object with an empty map.

`void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the key already exists in the map, update the corresponding value.

`int get(int key)` returns the value to which the specified key is mapped, or `-1` if this map contains no mapping for the key.

`void remove(key)` removes the key and its corresponding value if the map contains the mapping for the key.

### Example 1

```text
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]
```

### Explanation

```text
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
```

### Constraints

```text
0 <= key, value <= 10^6
At most 10^4 calls will be made to put, get, and remove.
```

## Boilerplate

```python
class MyHashMap:

    def __init__(self):

    def put(self, key: int, value: int) -> None:

    def get(self, key: int) -> int:

    def remove(self, key: int) -> None:


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
```

## English (Interview Answer)

To solve the Design HashMap problem, I implement a hash table manually using an array of buckets. Each bucket stores `[key, value]` pairs whose keys map to the same index.

1. In the constructor, I create `1000` empty buckets.
2. For each operation, I calculate the bucket index using `key % self.size`.
3. In `put`, I scan the bucket. If the key already exists, I update its value. If it does not exist, I append a new `[key, value]` pair.
4. In `get`, I scan the bucket and return the value when I find the key. If the key is not found, I return `-1`.
5. In `remove`, I scan the bucket and delete the pair if its key matches the requested key.

This approach uses separate chaining to handle collisions. The time complexity for `put`, `get`, and `remove` is O(k), where `k` is the number of pairs in the selected bucket. The space complexity is O(n + m), where `n` is the number of stored pairs and `m` is the number of buckets.

## Español (Respuesta para Entrevista)

Para resolver el problema Design HashMap, implemento una tabla hash manualmente usando un arreglo de buckets. Cada bucket guarda pares `[key, value]` cuyas claves caen en el mismo índice.

1. En el constructor, creo `1000` buckets vacíos.
2. Para cada operación, calculo el índice del bucket usando `key % self.size`.
3. En `put`, recorro el bucket. Si la clave ya existe, actualizo su valor. Si no existe, agrego un nuevo par `[key, value]`.
4. En `get`, recorro el bucket y devuelvo el valor cuando encuentro la clave. Si no la encuentro, devuelvo `-1`.
5. En `remove`, recorro el bucket y elimino el par si su clave coincide con la clave solicitada.

Este enfoque usa encadenamiento separado para manejar colisiones. La complejidad temporal de `put`, `get` y `remove` es O(k), donde `k` es la cantidad de pares en el bucket seleccionado. La complejidad espacial es O(n + m), donde `n` es la cantidad de pares guardados y `m` es la cantidad de buckets.
