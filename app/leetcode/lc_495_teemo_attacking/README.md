# 495. Teemo Attacking
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_495_teemo_attacking/README.md)

## English (Interview Answer)

To solve the Teemo Attacking problem, we need to calculate the total time Ashe is poisoned. The key observation is that if the time between two consecutive attacks is less than the poison `duration`, the first attack's effect is cut short by the second attack. Otherwise, the full `duration` is applied.

1. I iterate through the `timeSeries` array from the first attack to the second-to-last attack.
2. For each pair of consecutive attacks, I calculate the time elapsed between them (`timeSeries[i+1] - timeSeries[i]`).
3. The poisoned time contributed by the current attack is the minimum of the `duration` and the time until the next attack.
4. Finally, I add the full `duration` for the very last attack, as there are no subsequent attacks to reset the timer.

This approach has a time complexity of O(n) as we traverse the array once, and a space complexity of O(1) since we only use a single variable to accumulate the total time.

## Español (Respuesta para Entrevista)

Para resolver el problema de Teemo Attacking, debemos calcular el tiempo total que Ashe permanece envenenada. La observación clave es que si el tiempo entre dos ataques consecutivos es menor que la `duración` del veneno, el efecto del primer ataque se ve interrumpido por el segundo. De lo contrario, se aplica la `duración` completa.

1. Recorro el arreglo `timeSeries` desde el primer ataque hasta el penúltimo.
2. Para cada par de ataques consecutivos, calculo el tiempo transcurrido entre ellos (`timeSeries[i+1] - timeSeries[i]`).
3. El tiempo de envenenamiento aportado por el ataque actual es el mínimo entre la `duración` y el tiempo hasta el siguiente ataque.
4. Finalmente, sumo la `duración` completa para el último ataque, ya que no hay ataques posteriores que reinicien el temporizador.

Este enfoque tiene una complejidad temporal de O(n), ya que recorremos el arreglo una vez, y una complejidad espacial de O(1), ya que solo utilizamos una variable para acumular el tiempo total.
