import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set()

# Numero de iteraciones
i = 1000

lista_puntos = np.linspace(10,3000,i)
pi=[]

# Grafica de cuarta parte de circulo de longuitud 2pi
for i in range(0,i):
    # Se crean dos arreglos x e y con i elementos cada uno
    x=np.random.rand(int(lista_puntos[i]))
    y=np.random.rand(int(lista_puntos[i]))
    # Se crea una lista donde va a contener los puntos dentro del circulo de radio r
    xcirculo=[]
    ycirculo=[]
    pcirculo=0
    # Se hace un ciclo donde se van a computar cada uno de los elementos de x e y 
    for j in range(0,int(lista_puntos[i])):
        r=((x[j]**2)+(y[j]**2))**(1/2)
       # Si la distancia que se genera del origen a los puntos x,y 
       # de los arreglos x e y respectivamente es menor a r, entonces
       # los puntos de x,y se ponen en una lista nueva, donde posteriormente
       # estos puntos se grafican 
        if r<=1:
            pcirculo=pcirculo+1
            xcirculo.append(x[j])
            ycirculo.append(y[j])
    
    plt.plot(x,y,"ro")
    plt.plot(xcirculo,ycirculo,"bo")
    plt.title("Areas Circulo y Cuadrado")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.xlim(0,1)
    plt.ylim(0,1)
    valor_pi=4*(pcirculo/lista_puntos[i])
    pi.append(valor_pi)
plt.show()

# Valor aproximado de pi
indice=np.arange(1,len(pi)+1)
pi_df = pd.DataFrame(pi, index=indice, columns=(["Valores aprox de pi"]))
print(pi_df.tail(10))

# Grafico valor de pi respecto al numero de iteraciones en el algoritmo
z=np.arange(1,i+2)
plt.plot(z,pi,".-")
plt.title("Valor de pi")
plt.xlabel("Iteraciones")
plt.ylabel("pi")
plt.xlim(0,i+1)
plt.ylim(2.8,3.4)
plt.show()
 

