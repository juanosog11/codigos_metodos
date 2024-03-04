import numpy as np
import matplotlib.pyplot as plt



def rbf_interpolacion(x,y):

    #funcion de evaluacion de FBR multicuadrica
    def rbffuncion(xev,xdat,c):
        rbfv= np.sqrt((xev-xdat)**2+c**2)
        return rbfv

    #construccion de la matriz de interpolacion
    def interpmat(xdat,c):
        nd = len(xdat)
        mat1= np.zeros((nd,nd),float)
        for i in range (nd):
            for j in range (nd):
                mat1[i,j] = rbffuncion(xdat[i],xdat[j],c)
        return mat1


    # superposicion de funciones de base radial
    def rbfsuperposit(x,coef,xdat,c):
        y = np.zeros(len(x))
        for i in range (len(x)):
            for j in range (len(xdat)):
                y[i] = y[i] + coef[j]*rbffuncion(x[i],xdat[j],c)
        return y




    #informacion de entrada 

    xdat = x
    ydat = y
    c=50 # Parametro de forma

    #matriz de interpolacion
    matint = interpmat(xdat,c)
    #coeficientes de la interpolacion
    coef = np.linalg.solve(matint,ydat)


    #evaluacion de la superposicion sobre un intervalo
    x = np.arange(0.2,8.05 , 0.05)
    yinterp = rbfsuperposit(x,coef,xdat,c)


    #calculo del error RMS entre la interpolacion y la funcion dada
    Err = np.sqrt(np.sum((yinterp - np.log(x))**2)/len(yinterp) )
    print("parametro de forma: ", c)
    print("error RMS de la aproximacion: ", Err)
    
    # #graficas
    # plt.figure()
    # plt.plot(x, np.log(x), label = 'Funcion dada')
    # plt.plot(x, yinterp, label = 'Interpolacion RBF')
    # plt.plot(xdat,ydat , 'or' , label = 'datos')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.grid(True)
    # plt.title('interpolacion con funciones de base radial')
    x_eval = np.array([1.5, 5.7])
    y_eval = rbfsuperposit(x_eval, coef, xdat, c)
    print("Evaluación en x =", x_eval[0], ":", y_eval[0])
    print("Evaluación en x =", x_eval[1], ":", y_eval[1])




    plt.show()
    funcionx = x
    funciony = np.log(x)
    interx = x
    intery = yinterp

    return funcionx,funciony,interx,intery