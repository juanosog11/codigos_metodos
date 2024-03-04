import numpy as np
import interpolacion_importante as inti
import inter_RBFMN as rbf
import matplotlib.pyplot as plt

def punto5():
    # Definir los puntos x
    x_selected = np.array([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])

    # Calcular y = f(x)
    y_selected = np.cos(x_selected)**10

    print("Puntos seleccionados sobre la función:", "puntos en x: ", x_selected)
    print("puntos en y: ",y_selected)
    # for i in range(len(x_selected)):
    #     print(f"x = {x_selected[i]}, y = {y_selected[i]}")

    # Llamar a la función de interpolación polinómica
    puntosx_inti, puntosy_inti, polinomiox_, polinomioy_ = inti.interpolacion(x_selected, y_selected)

    # Llamar a la función de interpolación con funciones de base radial (RBF)
    funcionx, funciony, interx, intery = rbf.rbf_interpolacion(x_selected, y_selected)


    # Graficar los resultados de la interpolación con funciones de base radial (RBF)
    plt.figure(figsize=(10, 6))
    plt.plot(x_selected, y_selected, 'ro', label='Puntos seleccionados')
    plt.plot(x_selected, np.cos(x_selected)**10, label = 'Funcion dada')
    plt.plot(polinomiox_, polinomioy_, label='Interpolación Polinómica')
    plt.title('Métodos de interpolación RBF vs Polinomica de f(x)')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.show()