# Pi-Monte-Carlo
El método Monte Carlo es un método en el que por medio de la estadística y la probabilidad podemos determinar valores o soluciones de ecuaciones que calculados con exactitud son muy complejas, pero que mediante este método resulta sencillo calcular una aproximación al resultado que buscamos.

## Método 
El uso del método de Monte Carlo para aproximar el valor de Pi consiste en dibujar un cuadrado de lado L, y dentro de ese cuadrado dibujar un círculo con diámetro L, después se mapean puntos de manera aleatoria sobre ambas figuras, distinguiendo los puntos trazados en el cuadrado y en el círculo. Los puntos que están fuera del círculo y los que están dentro, sirven como estimadores de las áreas internas y externas del círculo.


![image](https://user-images.githubusercontent.com/103619172/163489569-0387dad3-95d3-49c4-bc74-4a400e7e79d6.png)

El área del caudrado está dada como:
A_cuadrado = 4r^2

El áre de la circunferencia es:
A_circ = pi*r^2 

Obtenemos la relación entre ambas areas:
A_cuadrado/A_circ = (4r^2)/(pi*r^2)

Por lo tanto:
pi = 4(A_circ/A_cuadrado)
