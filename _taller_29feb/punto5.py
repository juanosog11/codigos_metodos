import numpy as np
import interpolacion_importante_coseno as inti
import inter_RBFMN_coseno as rbf
import matplotlib.pyplot as plt

def punto5():
    # Definir los puntos x
    puntosx = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
    puntosy = (np.cos(puntosx))**10
    x_selected = np.arange(-2,2.05,0.05)

    # Calcular y = f(x)
    y_selected = (np.cos(x_selected))**10

    print("Puntos seleccionados sobre la función:", "puntos en x: ", x_selected)
    print("puntos en y: ",y_selected)


    puntosx_inti, puntosy_inti, polinomiox_, polinomioy_, Err_poli = inti.interpolacion(puntosx, puntosy)

    # Llamar a la función de interpolación con funciones de base radial (RBF)
    funcionx, funciony, interx, intery, error = rbf.rbf_interpolacion(x_selected, y_selected)

    Err = np.sqrt(np.sum((y_selected - np.log(x_selected))**2)/len(y_selected) )
    
    
    
    print("error coseno: " ,Err)
    print("error funcion radial: ", error)
    print("error de nuestro polinomio", Err_poli)


        # Graficar los resultados de la interpolación con funciones de base radial (RBF)
    plt.figure(figsize=(10, 6))
    plt.plot(puntosx, (np.cos(puntosx))**10, 'ro', label='Puntos seleccionados')
    plt.plot(x_selected, y_selected, label = 'Funcion dada')
    plt.plot(polinomiox_, polinomioy_, label='Interpolación Polinómica')
    plt.plot(interx,intery, label = "rbf")
    plt.title('Métodos de interpolación RBF vs Polinomica de f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()

    