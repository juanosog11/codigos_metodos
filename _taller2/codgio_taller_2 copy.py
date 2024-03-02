import numpy as np
import matplotlib.pyplot as plt


Ardat = np.loadtxt('_taller2\dat_log.txt')
buscar = np.loadtxt('_taller2\_buscar.txt')



datos = Ardat.shape  #me trae la fila y columnas (F,C)
print(datos)

if(datos[1] > 2):
    print("los datos no estan organizados en la segunda dimensión")
    exit()

polinomio = datos[0]-1
valoresX = Ardat[:,0]
valoresY = Ardat[:,1]

print(valoresX)
print(valoresY)
print(polinomio)

coeficientes = np.polyfit(valoresX,valoresY, polinomio)
#La función polyfit devuelve los coeficientes del polinomio en orden descendente de potencias,
#es decir, desde el coeficiente del término de mayor grado hasta el coeficiente del término constante.
# te permite encontrar un polinomio que mejor se ajuste a un conjunto de datos


print("Coeficientes del polinomio interpolante:", coeficientes)
# Coeficientes contiene los coeficientes del polinomio interpolante


filaYcolumnas = buscar.shape
cant= filaYcolumnas[0]
print(buscar)
polinomio_interpolante = np.poly1d(coeficientes)
interpolaciones = []
valores_input = []

for i in range(0,cant):
    valores_input.append(buscar[i])
    interpolaciones.append(polinomio_interpolante(buscar[i]))

print(valores_input)
print(interpolaciones)


plt.scatter(valoresX,valoresY)
plt.plot(valoresX, polinomio_interpolante(valoresX))
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title("Interpolación")
plt.show()