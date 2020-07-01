import numpy as np


def media_de_los_cuadrados(seed, i):
    semilla = []
    valor = []
    semilla.append(seed)
    for i in range(i):
        num = int(str(semilla[i] * semilla[i]).zfill(8)[2:6])
        semilla.append(num)
        valor.append(semilla[i] * semilla[i])
        #print('Semilla: ',semilla[i],'\t- valor: ',valor[i])
    return valor

def generadorgcl(seed, a, c, m, n):
    #Args:
    #seed = Semilla del generador
    #a = cte multiplicativa
    #c = cte aditiva
    #m = modulo

    numeros = []
    numeros_0y1 = []

    numeros.append(seed)
    for i in range(n):
        num  =  ((a * numeros[i - 1]) + c) % m
        numeros.append(num)
        numeros_0y1.append(num/m) #Lo dividimos por m para que devuelva un generador uniforme (0;1)
    return numeros_0y1

def generarNumpy(n):
#Generador de python
   numeros = []
   for i in range(n):
       numeros.append(np.random.uniform(0, 1))
   return numeros
