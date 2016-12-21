import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as opt
'''
Dopasowuje funkcję Gaussa do punktów pomiarowych wczytywanych z pliku tekstowego
'''
#tutaj ścieżka do pliku z danymi
file=r'ścieżka-do-pliku-z-danymi'
#definicja parametru różnicowego
param=13
#definicja funkcji Gaussa
def Gauss(x,A,x0,sigma):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))
#########################
#wczytywanie punktów pomiarowych z pliku
xdata=[]
ydata=[]
with open(file, 'r') as f:
    last=float(f.readline().split()[2])
    for line in f.readlines():
        if line[0]!='#':
            if np.abs(float(line.split()[2])-last)<param:
                xdata.append(float(line.split()[0]))
                ydata.append(float(line.split()[2]))
                last=float(line.split()[2])
########################################
#definicja niepewności pomiarowych - opcjonalne
#xerr=[0.1 for x in xdata]
#yerr=[0.005*y+2 for y in ydata]
#################################
#dopasowanie funkcji Gaussa i wypisanie parametrów dopasowania
popt, pcov = opt(Gauss,xdata,ydata)
perr = np.sqrt(np.diag(pcov))
print('A=',popt[0],'+/-',perr[0],'x0=',popt[1],'+/-',perr[1],'sigma=',popt[2],'+/-',perr[2])
#############################################################
#próbkowanie rozkładu przed wykreśleniem
x=np.linspace(min(xdata),max(xdata),50000)
y=Gauss(x,*popt)
########################################

#rysowanie i wyświetlenie wykresu
plt.errorbar(xdata,ydata, fmt='.')
plt.plot(x,y)
plt.show()
########################################
