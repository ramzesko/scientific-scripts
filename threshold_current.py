import numpy as np
import matplotlib.pyplot as plt

file=r'ścieżka-do-pliku'
k=2.45
R=100
xdata=[]
ydata=[]
with open(file, 'r') as f:
    for line in f.readlines():
        if line[0]!='#':
            xdata.append(float(line.split()[0]))
            ydata.append(float(line.split()[1]))

xerr=[0.1 for x in xdata]
yerr=[0.005*y+0.02 for y in ydata]

#rysowanie i wyświetlenie wykresu
fig=plt.figure()
ax=fig.add_subplot(111)
#ax.errorbar(xdata,ydata,yerr=yerr,xerr=xerr, fmt='.')
ax.plot(xdata,ydata, 'o')
ax.grid(True)
#ax.set_title('Laser ThorLabs LPSC-1550-FC 1554.5 nm')
#ax.set_xlabel('Pozycja [mm]')
#ax.set_ylabel('Napiecie [V]')
#plt.annotate(s='11.842(47) mm',xy=(popt[1],ymax),xytext=(6,1.3),arrowprops={'arrowstyle':'-|>'})
#plt.annotate('5.423(49) mm',xy=(left_border,y5),xytext=(4.5,0.4),arrowprops={'arrowstyle':'-|>'})
#plt.annotate('18.261(49) mm',xy=(right_border,y5),xytext=(16.5,0.4),arrowprops={'arrowstyle':'-|>'})
plt.show()
