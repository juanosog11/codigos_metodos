import numpy as np
import sympy as sym #Para crear la expresion del polinomio
import matplotlib.pyplot as plt
import interpolacion_importante as inti
import inter_RBFMN as rbf
import interpolacion_importante_original as init_original
import inter_RBFMN_Origina as rbf_original
import punto5 as punto5

datos= np.loadtxt('_taller_29feb\datos_importantes.txt')
terminar = 0
xi = datos[:,0]
fi = datos[:,1]
ultimo_dato = xi[-1]

while(terminar == 0):
    hacer = int(input("Que quieres hacer? \n 1:Metodo normal \n 2: metodo RBFMN \n 3: Union de los dos metodos \n 4: punto 5 \n 5: salir \n ingrese el numero: "))

    if(hacer == 1):
        init_original.interpolacion_oroginal(xi,fi)
    elif(hacer == 2):
        rbf_original.rbf_interpolacion(xi,fi)
    elif(hacer == 3):
        puntosx_inti,puntosy_inti,polinomiox_inti,polinomioy_inti = inti.interpolacion(xi,fi)
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
    elif(hacer == 4):
        punto5.punto5()
    elif(hacer == 5):
        terminar = 1

