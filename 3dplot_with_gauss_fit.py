import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit as opt
'''
Dopasowuje funkcję Gaussa do punktów pomiarowych wczytywanych z pliku tekstowego
'''
#tutaj ścieżka do pliku z danymi
file1=r'ściezka-do-źródła1'
file2=r'ścieżka-do-źródła2'

#definicja funkcji Gaussa
def Gauss(x,A,x0,sigma):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))/(sigma*np.sqrt(2*np.pi))
#########################
#wczytywanie punktów pomiarowych z pliku
xdata1=[]
ydata1=[]
xdata2=[]
ydata2=[]

with open(file1, 'r') as f:
    for line in f.readlines():
        if line[0]!='#':
            xdata1.append(float(line.split()[0]))
            ydata1.append(float(line.split()[2])-75)

with open(file2, 'r') as f:
    for line in f.readlines():
        if line[0] != '#':
            xdata2.append(float(line.split()[0]))
            ydata2.append(float(line.split()[2])-55)
########################################
#definicja niepewności pomiarowych - opcjonalne
#xerr=[0.1 for x in xdata]
#yerr=[0.005*y+2 for y in ydata]
#################################
#dopasowanie funkcji Gaussa i wypisanie parametrów dopasowania
popt1, pcov1 = opt(Gauss,xdata1,ydata1,p0=(50,400,10))
perr1 = np.sqrt(np.diag(pcov1))
print('A=',popt1[0],'+/-',perr1[0],'x0=',popt1[1],'+/-',perr1[1],'sigma=',popt1[2],'+/-',perr1[2])

popt2, pcov2 = opt(Gauss,xdata2,ydata2,p0=(50,400,10))
perr2 = np.sqrt(np.diag(pcov2))
print('A=',popt2[0],'+/-',perr2[0],'x0=',popt2[1],'+/-',perr2[1],'sigma=',popt2[2],'+/-',perr2[2])
#############################################################
#próbkowanie rozkładu przed wykreśleniem
x1=np.linspace(min(xdata1),max(xdata1),50000)
y1=Gauss(x1,*popt1)

x2=np.linspace(min(xdata2),max(xdata2),50000)
y2=Gauss(x2,*popt2)

x0=popt1[1]*np.ones(len(x1))
########################################

#rysowanie i wyświetlenie wykresu
fig=plt.figure()
ax=fig.add_subplot(211, projection='3d')
#ax.errorbar(xdata1,ydata1,fmt='.')#,yerr=yerr,xerr=xerr, fmt='.')
ax.plot(x1,x0,y1)
ax.plot(x0,x2,y2)
ax.set_title('Widok przestrzenny 13.5(7) mm')
ax.set_xlabel('Nr piksela')
ax.set_ylabel('Nr piksela')
ax.set_zlabel('Intensywnosć')

max_range = np.array([x1.max()-x1.min(), x2.max()-x2.min(), y1.max()-y2.min()]).max() / 2.0
mid_x = (x1.max()+x1.min()) * 0.5
mid_y = (x2.max()+x2.min()) * 0.5
#mid_z = (y1.max()+y1.min()) * 0.5
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
#ax.set_zlim(0, max_range-mid_z)

bx=fig.add_subplot(223)
bx.plot(x1,y1)
bx.errorbar(xdata1,ydata1,fmt='.')
bx.set_title('Płaszczyzna równoległa')
bx.set_xlabel('Nr piksela')
bx.set_ylabel('Intensywnosć')
bx.text(375,5,r'$\sigma$=18.05(27)')
bx.grid(True)

cx=fig.add_subplot(224)
cx.plot(x2,y2)
cx.errorbar(xdata2,ydata2,fmt='.')
cx.set_title('Płaszczyzna prostopadła')
cx.set_xlabel('Nr piksela')
cx.set_ylabel('Intensywnosć')
cx.text(290,30,r'$\sigma$=83.57(62)')
cx.grid(True)

plt.savefig('rozbieznosc4.eps')
#plt.show()
########################################
