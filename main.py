import numpy as np
import sympy as sym #Para crear la expresion del polinomio
import matplotlib.pyplot as plt
import interpolacion_importante as inti
import inter_RBFMN as rbf




datos= np.loadtxt('./datos_importantes.txt')

xi = datos[:,0]
fi = datos[:,1]
ultimo_dato = xi[-1]



puntosx_inti,puntosy_inti,polinomiox_inti,polinomioy_inti = inti.interpolacion(xi,fi)




# plt.xlabel('xi') #Añadimos una etiqueta
# plt.ylabel('fi') #Añadimos una etiqueta

inicio = 0.4
fin = ultimo_dato+1
cantidad_numeros_deseados = len(polinomiox_inti)
paso = (fin - inicio) / (cantidad_numeros_deseados - 1)
x = np.arange(inicio, fin + paso, paso)


print(np.log(x))

Err = np.sqrt(np.sum((polinomioy_inti - np.log(x))**2)/len(polinomioy_inti))
print("error de nuestro polinomio", Err)

funcionx,funciony,interx,intery = rbf.rbf_interpolacion(xi,fi)


plt.plot(funcionx, funciony, label = 'Funcion dada')
plt.plot(interx,intery, label = 'Interpolacion RBF')
plt.plot(xi,fi , 'or' , label = 'datos')
plt.plot(puntosx_inti,puntosy_inti,'o', label='puntos')
plt.plot(polinomiox_inti,polinomioy_inti, label='polinomio') #Trazamos la linea de los puntos
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend() #Mostrar todas las etiquetas
plt.title('interpolacion con funciones de base radial')



plt.show() #Para ver la gráfica

#Quinto punto del taller de interpolación 

# Definir los puntos x
x_selected = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])

# Calcular y = f(x)
y_selected = np.cos(x_selected)**10
