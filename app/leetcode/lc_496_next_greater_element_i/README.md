# 496. Next Greater Element I
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_496_next_greater_element_i/README.md)

## English (Interview Answer)

To solve the "Next Greater Element I" problem efficiently, we use a monotonic stack and a hash map. The goal is to find the first greater element to the right for each number in `nums1`, which is a subset of `nums2`.

1. I iterate through `nums2` and maintain a stack of elements for which I haven't yet found a "next greater element".
2. For each new number in `nums2`, if it's greater than the top of the stack, it means this number is the "next greater element" for the stack's top. I pop the element from the stack and store this mapping in a hash map.
3. After processing all elements in `nums2`, any elements remaining in the stack don't have a next greater element, so I map them to -1.
4. Finally, I construct the result for `nums1` by looking up each element in the hash map.

This approach has a time complexity of **O(n + m)**, where n is the length of `nums2` and m is the length of `nums1`, because each element is pushed and popped from the stack at most once. The space complexity is **O(n)** to store the hash map and the stack.

## Español (Respuesta para Entrevista)

Para resolver el problema "Next Greater Element I" de manera eficiente, utilizamos una pila monotónica y un mapa hash. El objetivo es encontrar el primer elemento mayor a la derecha para cada número en `nums1`, que es un subconjunto de `nums2`.

1. Recorro `nums2` y mantengo una pila de elementos para los cuales aún no he encontrado un "siguiente elemento mayor".
2. Para cada nuevo número en `nums2`, si es mayor que el tope de la pila, significa que este número es el "siguiente elemento mayor" para el tope de la pila. Saco el elemento de la pila y guardo esta relación en un mapa hash.
3. Después de procesar todos los elementos en `nums2`, cualquier elemento que permanezca en la pila no tiene un siguiente elemento mayor, por lo que los mapeo a -1.
4. Finalmente, construyo el resultado para `nums1` buscando cada elemento en el mapa hash.

Este enfoque tiene una complejidad temporal de **O(n + m)**, donde n es la longitud de `nums2` y m es la longitud de `nums1`, porque cada elemento se inserta y se saca de la pila como máximo una vez. La complejidad espacial es **O(n)** para almacenar el mapa hash y la pila.
