import numpy as np
import sympy as sym #Para crear la expresion del polinomio
import matplotlib.pyplot as plt
import _taller_29feb.interpolacion_importante_coseno as inti
import inter_RBFMN as rbf
import interpolacion_importante_original as init_original
import inter_RBFMN_Origina as rbf_original
import punto5 as punto5
import Combinacion as combinacion

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
        combinacion.combinacion(xi,fi)
    elif(hacer == 4):
        punto5.punto5()
    elif(hacer == 5):
        terminar = 1

