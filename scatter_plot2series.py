# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as opt
import matplotlib.patches as mpatches

def linear_fun(x,A,B):
    return A*x+B

file=r'scieżka-do-pliku'

xdata=[]
y1data=[]
y2data=[]
y1err=[]
y2err=[]
with open(file, 'r') as f:
    for line in f.readlines():
        if line[0]!='#':
            xdata.append(float(line.split()[4]))
            y1data.append(float(line.split()[0]))
            y2data.append(float(line.split()[2]))
            y1err.append(float(line.split()[1]))
            y2err.append(float(line.split()[3]))

xerr=[0.7 for x in xdata]
#yerr=[0.005*y+0.02 for y in ydata]

popt1, pcov1 = opt(linear_fun,xdata,y1data)
perr1 = np.sqrt(np.diag(pcov1))
print('A=',popt1[0],'+/-',perr1[0],'x0=',popt1[1],'+/-',perr1[1])

popt2, pcov2 = opt(linear_fun,xdata,y2data)
perr2 = np.sqrt(np.diag(pcov2))
print('A=',popt2[0],'+/-',perr2[0],'x0=',popt2[1],'+/-',perr2[1])
#próbkowanie rozkładu przed wykreśleniem
x=np.linspace(1,max(xdata),50000)
y1=linear_fun(x,*popt1)
y2=linear_fun(x,*popt2)

#rysowanie i wyświetlenie wykresu
fig=plt.figure()
ax=fig.add_subplot(111)
y1l=ax.errorbar(xdata,y1data,yerr=y1err,xerr=xerr,fmt='.')
y2l=ax.errorbar(xdata,y2data,yerr=y2err,xerr=xerr,fmt='.')
ax.plot(x,y1, color='red')
ax.plot(x,y2, color='green')
ax.plot(x,y1/y2, color='purple')
ax.grid(True)
ax.set_title('Pomiar kata rozbieznosci wiazki')
ax.set_xlabel('Odleglosc [mm]')
ax.set_ylabel('Szerokosc wiazki [px]')
#fig.legend((y1l,y2l),('prostopadła','równoległa'),'upper right')
stos = mpatches.Patch(color='purple', label='Stosunek szerokosci')
perpendicular = mpatches.Patch(color='red', label='Skladowa prostopadla')
parallel = mpatches.Patch(color='green', label='Skladowa rownolegla')
ax.legend(handles=[stos, parallel, perpendicular], loc='upper left')
#plt.annotate(s='11.842(47) mm',xy=(popt[1],ymax),xytext=(6,1.3),arrowprops={'arrowstyle':'-|>'})
#plt.annotate('5.423(49) mm',xy=(left_border,y5),xytext=(4.5,0.4),arrowprops={'arrowstyle':'-|>'})
#plt.annotate('18.261(49) mm',xy=(right_border,y5),xytext=(16.5,0.4),arrowprops={'arrowstyle':'-|>'})
plt.show()
#plt.savefig('katrozbieznosci.eps')