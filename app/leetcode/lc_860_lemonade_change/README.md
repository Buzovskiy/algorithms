# 860. Lemonade Change
[README on GitHub](https://github.com/Buzovskiy/algorithms/blob/main/app/leetcode/lc_860_lemonade_change/README.md)

## Problem Description

At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time in the order specified by `bills`. Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the `i`th customer pays, return `true` if you can provide every customer with the correct change, or `false` otherwise.

### Example 1

```text
Input: bills = [5,5,5,10,20]
Output: true
Explanation:
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
```

### Example 2

```text
Input: bills = [5,5,10,10,20]
Output: false
Explanation:
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
```

## Boilerplate

```python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
```

## English (Interview Answer)

To solve the Lemonade Change problem, I track how many `$5` and `$10` bills I currently have, because those are the only bills useful for making change.

1. I start with `five = 0` and `ten = 0`.
2. When a customer pays with `$5`, no change is needed, so I increase `five`.
3. When a customer pays with `$10`, I must give one `$5` bill back. If I do not have a `$5` bill, I return `False`; otherwise, I decrease `five` and increase `ten`.
4. When a customer pays with `$20`, I need to give `$15` in change. I first try to use one `$10` and one `$5`, because that keeps more `$5` bills for future customers. If that is not possible, I try to use three `$5` bills. If neither option is possible, I return `False`.
5. If every customer receives correct change, I return `True`.

The time complexity is O(n), where `n` is the number of bills, because each bill is processed once. The space complexity is O(1), because only two counters are stored.

## Espanol (Respuesta para Entrevista)

Para resolver el problema Lemonade Change, mantengo cuantas billetes de `$5` y `$10` tengo en cada momento, porque son los unicos billetes que sirven para dar cambio.

1. Empiezo con `five = 0` y `ten = 0`.
2. Cuando un cliente paga con `$5`, no hace falta dar cambio, asi que incremento `five`.
3. Cuando un cliente paga con `$10`, debo devolver un billete de `$5`. Si no tengo un billete de `$5`, devuelvo `False`; si lo tengo, decremento `five` e incremento `ten`.
4. Cuando un cliente paga con `$20`, debo devolver `$15` de cambio. Primero intento usar un billete de `$10` y uno de `$5`, porque asi conservo mas billetes de `$5` para futuros clientes. Si eso no es posible, intento usar tres billetes de `$5`. Si ninguna opcion es posible, devuelvo `False`.
5. Si todos los clientes reciben el cambio correcto, devuelvo `True`.

La complejidad temporal es O(n), donde `n` es el numero de billetes, porque cada billete se procesa una sola vez. La complejidad espacial es O(1), porque solo se guardan dos contadores.
