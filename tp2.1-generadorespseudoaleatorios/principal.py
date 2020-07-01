import generadores
import pruebas
import graficas
from math import pow
import numpy as np



#numeroMediaCuadrados = generadores.media_de_los_cuadrados(12121212,1000)
numerosGCL = generadores.generadorgcl(1234,134775813, 1, pow(2, 32),1000)
numerosNumpy = generadores.generarNumpy(10000)
numBologna = generadores.generadorgcl(3298876,134775813,1,2**32,1000)
#Prueba kolmogorov
print(pruebas.Kolmogorov(numerosGCL, 0.05)) # Numeros, alpha

#Prueba ChiCuadrado
#print(pruebas.ChiCuadrado(numerosGCL, 0.95, 9)) #Numeros, int confianza, grados libertad

#Prueba Paridad
#resultado_paridad_Numpy = pruebas.Paridad(numerosNumpy)
#resultados_paridad_GCL = pruebas.Paridad(numerosGCL)
#graficas.graficoCircular(resultado_paridad_Numpy[0], resultado_paridad_Numpy[1])
#graficas.graficoCircular(resultados_paridad_GCL[0], resultados_paridad_GCL[1], 'Generador GCL')


#Prueba Corrida
#print('numpy',pruebas.PruenaDeCorrida(numerosNumpy, 0.05))
#print('glc',pruebas.PruenaDeCorrida(numerosGCL, 0.05))

#Histograma
#graficas.GraficoFrecuecias(numerosGCL)
#graficas.GraficoFrecuecias(numerosNumpy)

