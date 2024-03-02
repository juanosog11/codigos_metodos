import numpy as np
import matplotlib.pyplot as plt

#definimos dominio
xm=1
n=20

x=np.linspace(-xm,xm,n)

nc=5
c=np.linspace(0,10,nc) # parametro de forma
m=1 

#funcion multicuadrica
def mq(r,c):
    print(c)
    f=np.sqrt(r**2+c**2)
    return f

r= np.abs(x) #vector radar r



#grafico

for i in range(nc):
    print(c[i])
    fmq=mq(r,c[i])
    plt.plot(x,fmq)

plt.xlabel("x")
plt.ylabel("y")
plt.show()

