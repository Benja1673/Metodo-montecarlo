import numpy as np
import matplotlib.pyplot as plt

#Sugerencia de ingresar por consola 300 o 100 iteraciones, para obtener mejores resultados.
#Se deben utilizar las librerias numpy y matplotlib.pyplot

def funcion1(n_puntos):
    puntos_x = np.random.uniform(-1, 1, n_puntos)#"Lanzar" dardos aleatorios dentro de un cuadrado de lado 2
    puntos_y = np.random.uniform(-1, 1, n_puntos)  
    distancias = np.sqrt(puntos_x**2 + puntos_y**2)#Calcular la distancia de cada dardo al origen (0,0)
    puntos_dentro_circulo = np.sum(distancias < 1)#Contador de dardos que caen dentro del circulo
    pi_aprox = 4 * puntos_dentro_circulo / n_puntos#Calcular la aproximacion de pi usando la formula del area de un circulo y un cuadrado
    print("Aproximacion de pi:", pi_aprox)#Mostrar la aproximacion de pi
    return pi_aprox


n_puntos = 17000#Primer lanzamiento de dardos

num_veces = int(input("Introduce el numero de veces que quieres ejecutar la funcion (de 100 a 300 sugeridos) : "))
i = 0
pi_aprox_list = [] #Creamos una lista para guardar las aproximaciones de pi
while i < num_veces:
    pi_aprox = funcion1(n_puntos) #Llamamos a la funcion con el valor actual de n_puntos
    pi_aprox_list.append(pi_aprox) #Agregamos la aproximacion de pi a la lista
    n_puntos += 15000 #Agregamos 15000 al valor de n_puntos por cada iteracion
    i += 1

#Funcion que grafica pi en funcion del numero de iteraciones
plt.plot(pi_aprox_list)
plt.xlabel('Numero de iteraciones')
plt.ylabel('Aproximacion de pi')
plt.title('Aproximacion de pi')
plt.show()
