import numpy as np
import matplotlib.pyplot as plt
# Crear dos arrays vacíos
x = []
y = []

# Pedir al usuario que ingrese los datos para el primer arra
polinomio = int(input("Ingrese el grado del polinomio:  "))
for i in range(polinomio+1):
    dato = int(input(f"Ingrese la el valor de x en la posicion {i + 1} : "))
    x.append(dato)

for i in range(polinomio+1):
    dato = float(input(f"Ingrese la el valor de x en la posicion {i + 1} : "))
    y.append(dato)

coeficientes = np.polyfit(x, y, polinomio)
#La función polyfit devuelve los coeficientes del polinomio en orden descendente de potencias,
#es decir, desde el coeficiente del término de mayor grado hasta el coeficiente del término constante.
# te permite encontrar un polinomio que mejor se ajuste a un conjunto de datos

# Coeficientes contiene los coeficientes del polinomio interpolante
print("Coeficientes del polinomio interpolante:", coeficientes)

# Crea una función polinómica a partir de los coeficientes
polinomio_interpolante = np.poly1d(coeficientes)
print("(X=1.5, Y:",polinomio_interpolante(1.5),")")
print("(X=5.7, Y:",polinomio_interpolante(5.7),")")

plt.scatter(x, y)
plt.plot(x, polinomio_interpolante(x))
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title("Interpolación")
plt.show()