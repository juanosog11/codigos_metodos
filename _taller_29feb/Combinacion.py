import numpy as np
import sympy as sym 
import matplotlib.pyplot as plt

def combinacion(x1,y):
    #Primero vamos a calcular el polinomio de interpolación
    # Ingreso de datos, pero acá están presentados como listas
    xi = x1
    fi = y

    # Procedimiento, pasamos a convertirlos en arreglos
    xi = np.array(xi)
    fi = np.array(fi)
    B = np.copy (fi)

    #Matriz
    n = len(xi) #Tamaño de la matriz
    D = np.zeros((n,n),dtype=float) #Matriz, llena de ceros
    for i in range(n):
        for j in range(n):
            D[i, j] = xi[i] ** (n - 1 - j)


    # Calculo de coeficientes del polinomio,mediante algebra lineal
    coeficientes = np.linalg.solve(D, fi)

    #Polinomio de Interpolación
    x = sym.Symbol('x')
    polinomio = sum(coeficientes[i] * (x ** (n - 1 - i)) for i in range(n))

    #Para facilitar la evaluación del polinomio
    px = sym.lambdify(x,polinomio)
    #Evaluar polinomio
    muestras = 51
    a = np.min(xi) #Minimo
    b= np.max(xi) #Máximo
    pxi = np.linspace(a,b,muestras) #Serie de puntos muestreados
    pfi = px(pxi) #puntos de la función,usando la forma numerica del polinomio

    #Información de Entrada
    
    xdat = x1
    ydat = y
    c = 50

    #Construimos la función para evaluar funciones de base radial, multicuadrica
    def rbffunction(xev,xdat,c):
        rbfv = np.sqrt((xev - xdat)*2 + c*2)
        return rbfv

    #Construimos la matriz de interpolación
    def interpmat(xdat,c):
        nd = len(xdat)
        mat1 = np.zeros((nd,nd),float)
        for i in range (nd):
            for j in range (nd):
                mat1[i,j] = rbffunction(xdat[i], xdat[j],c)
        return mat1

    #Llamar la función de matriz de interpolación
    matint = interpmat(xdat,c)

    #coeficientes de la interpolación
    coef = np.linalg.solve(matint,ydat)

    #Superposición de funciones de base radial
    def rbfsuperposition(x,coef,xdat,c):
        y = np.zeros((len(x)))
        for i in range (len(x)):
            for j in range (len(xdat)):
                y[i] = y[i] + coef[j] * rbffunction (x[i], xdat[j],c)
        return y

    #evaluacion de la superposicion sobre un intervalo
    x = np.arange(0.2,8.05 , 0.05)
    yinterp = rbfsuperposition(x,coef,xdat,c)

    #Cálculo del error RMS entre la interpolación y la función dada
    Err = np.sqrt(np.sum((yinterp - np.log(x))**2)/len(yinterp)) #la raiz cuadrada dela sumatoria de los valores tanto aproximados como verdaderos
    print('Parámetro de forma: ', c) # Establecer el valor del parametro
    print('Error RMS de la aproximación:' , Err)

    #Halla el valor de cada interpolación en 𝑥 = 1.5 y 𝑥 = 5.7.
    print('Valor de la interpolación en x=1.5:', px(1.5))
    print('Valor de la interpolación en x=5.7:', px(5.7))

    #Halla el valor de cada interpolación en FBR 𝑥 = 1.5 y 𝑥 = 5.7.
    x_eval = np.array([1.5, 5.7])
    y_eval = rbfsuperposition(x,coef,xdat,c)
    print('Evaluación de x=', x_eval[0], ':', y_eval[0])
    print('Evaluación de x=', x_eval[1], ':', y_eval[1])


    #Grafica
    plt.figure()
    plt.plot(xi, fi, 'o', label='Puntos del polinomio')
    plt.plot(pxi, pfi, label='Polinomio de interpolación')
    plt.plot(x, np.log(x), label = 'Funcion dada')
    plt.plot(x, yinterp, label = 'Interpolacion RBF')
    plt.plot(xdat,ydat , 'or' , label = 'datos')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.title('Interpolación combinando polinomio y RBF')
    plt.legend()
    plt.show()