from scipy.stats import kstest
import scipy.stats as stats
import numpy as np
from scipy.stats import ksone
from scipy.stats import norm
from math import sqrt

#Pruebas definidas para ver si los generadores pasan los test
#Prueba chi-cuadrado
#Prueba Kolmogorov-Smirnov.
#Prueba de paridad
#Prueba de corrida

def Kolmogorov(numeros, alpha):

#Ordenar los numeros en forma ascendente
    num_ordenados = sorted(numeros)
    tamaño = len(num_ordenados)

#Calculo D+ Y D-
    D_Mas = max(((i+1)/tamaño - num_ordenados[i]) for i in range(tamaño))
    D_Menos = min((num_ordenados[i] - (i-1)/tamaño) for i in range(tamaño))

#Obtengo el mas grande
    D = max(abs(D_Mas) ,abs(D_Menos))

#Busco el valor critico de la tabla de kolmogorov para ese nivel de significancia y lo comparo con D
#Si D es menor que el valor critico puedo decir que los datos pertenecen a una distribucion uniforme
#Para buscar los datos uso la libreria de scipy
    valor_critico = (ksone.ppf((1-alpha/2), tamaño))
    if D < valor_critico:
        resultado = True
    else:
        resultado = False

    return num_ordenados

def ChiCuadrado(numerosAleatorios,q,df):
   numeros = numerosAleatorios
   frec_obt_int = np.histogram(numeros, bins=(0,1,2,3,4,5,6,7,8,9,10))  # Frecuencia en cada intervalo
   # Frecuencia en cada rango
   suma_epic = 0
   arreglo_suma_epic = []
   cont = len(numeros) / 10
   # 3. a cada intervalo le aplico la siguiente ecuacion (Ef - Ee)^2/Ee y hago la sumatoria
   for i in range(10):
       calculo = ((frec_obt_int[0][i - 1] - cont) ** 2) / cont
       arreglo_suma_epic.append(calculo)
   suma_epic = sum(arreglo_suma_epic)
   # 5. comparo en tabla de chi cuadrado con un nivel de confianza
   # Se hace con el valor suma epic
   # Si suma_epic es mayor que el valor por tabla, se rechaza ( no es uniforme)

   #Obtengo el valor de l tabla para
   #q = intervalo de confianza
   #df  = grados de libertad
   chi_cuadrado_tabla = stats.chi2.ppf(q=q, df=df)


   if suma_epic < chi_cuadrado_tabla:
       resultado = True
   else:
       resultado = False

   return  resultado, arreglo_suma_epic, suma_epic, chi_cuadrado_tabla

def Paridad(numeros):
    pares, impares = 0, 0
    i = 1
    for i in range(len(numeros)):
        if (float(str(numeros[i])[-1]))%2==0: #Tomo solo el ultimo numero porque si no esta con formato e^-05
            pares += 1
        else:
            impares +=1
    return pares, impares

def PruenaDeCorrida(numeros, alpha):
    secuencia_signos = []
    #Asignar signo a la secuencia
    #Xi<Xi+1 entonces es +
    #Xi>Xi+1 entonces es -
    media = 0
    var = 0
    tamaño = 0
    for i in range(len(numeros)-1):
        if numeros[i]<numeros[i+1]:
            secuencia_signos.append('+')
        else:
            secuencia_signos.append('-')
    #Calcular total de corridas que resulte de la suma de terminos iguales
    a = 0
    for i in range(len(secuencia_signos)-1):
        if secuencia_signos[i] != secuencia_signos[i+1]:
            a += 1

    #Calculo media y varianza
    tamaño = len(numeros)
    media = ((2*tamaño)-1)/3
    var = ((16*tamaño)-29)/90

    #Criterio de aceptacion: Z <= Z obtenido de tabla
    #Obtengo z de la tabla
    z_tabla = norm.ppf(q=1-alpha/2)
    #Calculo mi z
    z_calculado = abs((a-media)/sqrt(var))
    #Comparo

    if z_calculado <= z_tabla:
        resultado = True
    else:
        resultado = False

    return resultado, z_calculado, z_tabla, a, media, var
