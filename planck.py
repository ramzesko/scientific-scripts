import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

h=6.626e-34
c=3.0e+8
k=1.38e-23

def Planck_distribution(x,T):
    A=2.0*h*c**2
    B=h*c/(x*k*T)
    return A/((x**5)*(np.exp(B)-1.0))


x=np.arange(1e-9, 3e-6, 1e-9)
y2_7=Planck_distribution(x,2.7)
y300=Planck_distribution(x,300)
y2800=Planck_distribution(x,2800)
y4000=Planck_distribution(x,4000)
y6000=Planck_distribution(x,6000)
plt.hold(True)
plt.grid(True)
plt.plot(x*1e9,y6000, color='green')
#plt.plot(x*1e9,y300*1000000, color='red')
plt.plot(x*1e9,y2800, color='red')
plt.plot(x*1e9,y4000, color='purple')
#plt.plot(x*1e9,y6000)
plt.xlabel('Wavelenght [nm]')
plt.ylabel('Intensity')
t1 = mpatches.Patch(color='red', label='2800 K')
t2 = mpatches.Patch(color='green', label='6000 K ')
t3 = mpatches.Patch(color='purple', label='4000 K ')
plt.legend(handles=[t1,t2,t3], loc='upper right')
plt.show()
