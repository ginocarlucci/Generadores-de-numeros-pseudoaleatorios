import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def graficoCircular(par, impar):
   #plt.title(str(titulo))
   par = par
   impar = impar
   variables = [par, impar]
   nombres = ["Pares", "Impares"]
   plt.pie(variables, labels=nombres, autopct='%1.1f%%', shadow=True)
   plt.axis("equal")
   plt.legend(loc='lower right')
   plt.show()

def GraficoFrecuecias(numeros):
   plt.hist(numeros, bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
   plt.grid(True)
   plt.show()

"""
def graficaKolmogorov(numeros):
   plt.hist(numeros, bins=30, density=True, histtype='step',
                           cumulative=True, label='Empirical')
   uniforme = stats.uniform.cdf
   plt.show()
"""
