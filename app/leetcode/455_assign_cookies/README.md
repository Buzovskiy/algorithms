# 455. Assign Cookies

## English Explanation
This is a greedy problem. First, I sort both the children's greed factors and the cookie sizes. Then I use two pointers: one for the children and one for the cookies. I try to satisfy the least greedy child with the smallest cookie that is large enough. If a cookie satisfies the child, I move to the next child. Otherwise, I try a larger cookie. This greedy approach maximizes the number of satisfied children because it preserves larger cookies for greedier children.

## Explicación en Español
Este es un problema de tipo greedy. Primero ordeno tanto los factores de avaricia de los niños como los tamaños de las galletas. Después utilizo dos punteros: uno para los niños y otro para las galletas. Intento satisfacer al niño menos exigente con la galleta más pequeña que pueda satisfacerlo. Si la galleta es suficiente, avanzo al siguiente niño; si no, pruebo con una galleta más grande. Esta estrategia greedy maximiza el número de niños satisfechos porque reserva las galletas más grandes para los niños más exigentes.
