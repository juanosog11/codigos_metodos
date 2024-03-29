#En este ejercicio se le dan directamente los valores que se quieren evaluar en el polinomio
# El polinomio de interpolación
import numpy as np
import sympy as sym #Para crear la expresion del polinomio
import matplotlib.pyplot as plt

# Ingreso de datos, pero acá están presentados como listas

def interpolacion_oroginal(x,y):

  # Procedimiento, pasamos a convertirlos en arreglos
  xi = np.array(x)
  fi = np.array(y)
  B = np.copy (y)

  #Matriz
  n = len(xi) #Tamaño de la matriz
  D = np.zeros((n,n),dtype=float) #Matriz, llena de ceros
  ultima = n-1

  #Para llenar las casillas
  i = 0 #Fila cero
  for i in range(0,n,1): #mover el valor de i, en el rango desde la primera hasta la ultima
    for j in range(0,n,1): #mover el valor de j, en el rango desde la primera hasta la ultima
      potencia = ultima -j #Se calcula el valor de la exponente
      D[i,j] = xi[i] **potencia #Posicion en la matriz

  # Calculo de coeficientes del polinomio,mediante algebra lineal
  coeficientes = np.linalg.solve(D,B)

  #Polinomio de Interpolación
  x = sym.Symbol('x') # X va a ser tomada como un simbolo
  polinomio = 0 #Comenzamos con polinomio vacío
  for i in range(0,n,1):
    potencia = (n-1)-i #Es relativo al valor de la ultima posición
    termino = coeficientes[i]*(x**potencia)
    polinomio = polinomio + termino

  #Para facilitar la evaluación del polinomio
  px = sym.lambdify(x,polinomio)

  #Evaluar polinomio
  muestras = 51
  a = np.min(xi) #Minimo
  b= np.max(xi) #Máximo
  pxi = np.linspace(a,b,muestras) #Serie de puntos muestreados
  pfi = px(pxi) #puntos de la función,usando la forma numerica del polinomio


  #Salida
  print ('Matriz')
  print ('D')
  print ('Coeficientes:')
  print (coeficientes)
  print ('polinomio: ')
  print (polinomio)
  print ("evaluado en 1.5: ",px(1.5))
  print ("evaluado en 5,7: ",px(5.7))
  #crearemos una grafica
  plt.plot(xi,fi,'o', label='puntos')
  plt.plot(pxi,pfi, label='polinomio') #Trazamos la linea de los puntos
  plt.legend() #Mostrar todas las etiquetas
  plt.xlabel('xi') #Añadimos una etiqueta
  plt.ylabel('fi') #Añadimos una etiqueta
  plt.title('Polinomio de Interpolación')#Añadimos un titulo
  plt.show() #Para ver la gráfica

  