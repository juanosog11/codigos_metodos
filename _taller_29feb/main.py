import numpy as np
import sympy as sym #Para crear la expresion del polinomio
import matplotlib.pyplot as plt
import interpolacion_importante as inti
import inter_RBFMN as rbf




datos= np.loadtxt('_taller_29feb\datos_importantes.txt')

xi = datos[:,0]
fi = datos[:,1]




puntosx_inti,puntosy_inti,polinomiox_inti,polinomioy_inti = inti.interpolacion(xi,fi)



plt.plot(puntosx_inti,puntosy_inti,'o', label='puntos')
plt.plot(polinomiox_inti,polinomioy_inti, label='polinomio') #Trazamos la linea de los puntos
plt.legend() #Mostrar todas las etiquetas
# plt.xlabel('xi') #Añadimos una etiqueta
# plt.ylabel('fi') #Añadimos una etiqueta

x = np.arange(0.5,8,0.05)
print(np.log(x))
print(len(x))
print(len(polinomiox_inti))
print("poli ",polinomiox_inti)


Err = np.sqrt(np.sum((polinomioy_inti - np.log(x))**2)/len(polinomioy_inti))


# plt.plot(x, np.log(x), label = 'Funcion dada')
# plt.plot(x, yinterp, label = 'Interpolacion RBF')
# plt.plot(xdat,ydat , 'or' , label = 'datos')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.title('interpolacion con funciones de base radial')
# plt.figure()


plt.show() #Para ver la gráfica
