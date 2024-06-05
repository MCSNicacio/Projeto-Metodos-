### Projeto B Métodos 
# Nicácio de Mattos(RA:218335) e Vitor de Oliveira (RA:206649)

import numpy as np 
import matplotlib.pyplot as plt

#n_i = número de iterações
#N = tamanho da imagem
def Mandelbrot(n_i, N):

    x_in = np.linspace(-2, 2, N)
    y_in = np.linspace(-2, 2, N)
    [a, b] = np.meshgrid(x_in, y_in * 1j)
    z = a+b
    c =a+b
    div_array = np.zeros([N,N])
   
    for p in range(n_i):
        div_ind = np.abs(z) < 2
        div_array[div_ind] = div_array[div_ind]+1
        z= z**2 + c

    plt.figure(figsize = (10, 10))
    plt.pcolormesh(x_in, y_in, div_array, cmap = "tab20b")

Mandelbrot(100,1000) #mudar primeiro parâmetro para reduzir iterações no teste de convergência
    

