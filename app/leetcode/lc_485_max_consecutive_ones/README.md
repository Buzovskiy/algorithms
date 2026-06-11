# 485. Max Consecutive Ones
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_485_max_consecutive_ones/README.md)

## English (Interview Answer)

To find the maximum number of consecutive ones in a binary array, I iterate through the array once while keeping track of the current streak of ones and the maximum streak found so far.

1. I initialize a counter `current_number` to 0 and a result variable `output` to 0.
2. As I iterate through each number:
   - If I encounter a `1`, I increment the `current_number`.
   - If I encounter a `0`, I compare the `current_number` with the `output` to update the maximum streak if necessary, and then reset `current_number` to 0.
3. After the loop, I perform one final check to handle cases where the array ends with a streak of ones.

This approach has a time complexity of O(n) because we visit each element exactly once, and a space complexity of O(1) as we only use a few integer variables.

## Español (Respuesta para Entrevista)

Para encontrar el número máximo de unos consecutivos en un arreglo binario, recorro el arreglo una vez manteniendo un registro de la racha actual de unos y la racha máxima encontrada hasta el momento.

1. Inicializo un contador `current_number` en 0 y una variable de resultado `output` en 0.
2. Mientras recorro cada número:
   - Si encuentro un `1`, incremento el `current_number`.
   - Si encuentro un `0`, comparo el `current_number` con el `output` para actualizar la racha máxima si es necesario, y luego reinicio el `current_number` a 0.
3. Después del bucle, realizo una verificación final para manejar los casos en los que el arreglo termina con una racha de unos.

Este enfoque tiene una complejidad temporal de O(n) porque visitamos cada elemento exactamente una vez, y una complejidad espacial de O(1) ya que solo utilizamos unas pocas variables enteras.
