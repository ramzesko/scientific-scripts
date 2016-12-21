import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as opt

def linear_fun(x,A,B):
    return A*x+B

file=r'ścieżka-do-pliku'

xdata=[]
ydata=[]
xfitdata=[]
yfitdata=[]
with open(file, 'r') as f:
    for line in f.readlines():
        try:

        #if type(line[0])==float:
           # if float(line.split()[0])>22:
            #    xfitdata.append(float(line.split()[0]))
             #   yfitdata.append(float(line.split()[1]))
            #if float(line.split()[0])<14:
            #    xdata.append(float(line.split()[0])+11)
            #else:
            xdata.append(float(line.split()[0]))
            ydata.append(float(line.split()[1]))
        except: pass
xerr=[0.01*x+0.2 for x in xdata]
yerr=[0.005*y for y in ydata]

#popt1, pcov1 = opt(linear_fun,xfitdata,yfitdata)
#perr1 = np.sqrt(np.diag(pcov1))
#print('A=',popt1[0],'+/-',perr1[0],'x0=',popt1[1],'+/-',perr1[1])
#x=np.linspace(20,max(xfitdata),50000)
#y1=linear_fun(x,*popt1)

#rysowanie i wyświetlenie wykresu
fig=plt.figure()
ax=fig.add_subplot(111)
#ax.errorbar(xdata,ydata,yerr=yerr,xerr=xerr, fmt='.')
ax.plot(xdata,ydata)
#ax.plot(x,y1)
ax.grid(True)
ax.set_title('Tytuł')
ax.set_xlabel('Dlugosc fali [nm]')
ax.set_ylabel('Intensywnosc')
#plt.annotate(s='653.87(4) nm',xy=(653.877,2500),xytext=(653,2500),arrowprops={'arrowstyle':'-|>'})
#plt.annotate('653.70(4) nm',xy=(653.700,1300),xytext=(653.4,2200),arrowprops={'arrowstyle':'-|>'})
#plt.annotate('653.50(4) nm',xy=(653.5,1700),xytext=(653,1600),arrowprops={'arrowstyle':'-|>'})
plt.show()
#plt.savefig('pm100.eps')