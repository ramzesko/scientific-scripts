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

file_planck=r'ścieżka-do-pliku-z-widmem-referencyjnego-źródła-planckowskiego'
file=r'ścieżka-do-pliku-z-widmem-eksperymentalnym'
filesav=r'ścieżka-do-zapisu-pliku-pomocnicznego-z-danymi-do-ciexyy.txt'

xdata_planck=[]
ydata_planck=[]
xcal=[]
ycal=[]
xdata=[]
ydata=[]
with open(file, 'r') as f:
    for line in f.readlines():
        try:
            xdata.append(float(line.split()[0]))
            ydata.append(float(line.split()[1]))
        except: pass

with open(file_planck, 'r') as f:
    for line in f.readlines():
        try:
            xdata_planck.append(float(line.split()[0]))
            ydata_planck.append(float(line.split()[1]))
        except: pass

x=np.arange(200e-9, 1100e-9, 1e-9)
y=Planck_distribution(x,2700)

for p in range(len(xdata_planck)):
    try:
        xcal.append(xdata_planck[p])
        if ydata_planck[p]!=0:
            ycal.append(Planck_distribution(xdata_planck[p]*1e-9,2600)/ydata_planck[p])
        else:
            ycal.append(0)
    except: pass
for p in range(len(xdata)):
    try:
        if xcal[p]==xdata[p]:
            ydata[p]=ydata[p]*ycal[p]
    except: pass

probx=[340]
proby=[]
for i in range(49):
    probx.append(probx[i]+10)

for i in probx:
    for row,val in enumerate(xdata):
        if np.abs(val-i)<0.5:
            proby.append(ydata[row])
            break

with open(filesav, 'w') as f:
    for i in proby:
        f.write(str(i))
        f.write(' ')

plt.hold(True)
plt.grid(True)
plt.plot(x*1e9,y, color='red')
plt.plot(xdata,ydata, color='green')
#plt.plot(xcal,ycal, color='purple')
plt.xlabel('Długosć fali [nm]')
plt.ylabel('Gestosc energii [J*s^-1*m^-3]')
t1 = mpatches.Patch(color='red', label='Widmo teoretyczne 2700 K')
t2 = mpatches.Patch(color='green', label=' - widmo eksperymentalne')
plt.legend(handles=[t1,t2], loc='upper right')
plt.show()
#plt.savefig('name.eps')
