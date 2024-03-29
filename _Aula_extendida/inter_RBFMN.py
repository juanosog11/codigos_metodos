import numpy as np
import matplotlib.pyplot as plt
datos = np.loadtxt('_Aula_extendida\dat_log.txt', encoding='utf-8')  # Reemplaza 'utf-8' con la codificación real del archivo


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

xdat = datos[:,0]
ydat = datos[:,1]
c=50 # Parametro de forma

#matriz de interpolacion
matint = interpmat(xdat,c)
#coeficientes de la interpolacion
coef = np.linalg.solve(matint,ydat)


#evaluacion de la superposicion sobre un intervalo
x = np.arange(0.2,8.05 , 0.05)
yinterp = rbfsuperposit(x,coef,xdat,c)


#calculo del error RMS entre la interpolacion y la funcion dada
Err = np.sqrt(np.sum((yinterp -np.log(x))**2)/len(yinterp) )
print("parametro de forma: ", c)
print("error RMS de la aproximacion: ", Err)

#graficas
plt.figure()
plt.plot(x, np.log(x), label = 'Funcion dada')
plt.plot(x, yinterp, label = 'Interpolacion RBF')
plt.plot(xdat,ydat , 'or' , label = 'datos')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('interpolacion con funciones de base radial')

plt.show()
