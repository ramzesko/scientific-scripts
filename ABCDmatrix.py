import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as opt

def linear_fun(x,A,B):
    return A*x+B
def quadratic_fun(x,A,B,C):
    return A*x**2+B*x+C

file=r'sciezka/do/pliku/'

xdata=[]
ydata=[]
pdata=[]
xfitdata=[]
yfitdata=[]
alpha=[]
y_pom=[]

with open(file, 'r') as f:
    for line in f.readlines():
        try:
            xdata.append(float(line.split()[0]))
            ydata.append(float(line.split()[1]))
            pdata.append(float(line.split()[2]))
        except: pass

xerr=[0.25 for x in xdata]
yerr=[0.25 for y in ydata]
perr=[0.1 for p in pdata]

p_pom=[2 for p in pdata]
for pd, pp in zip(pdata,p_pom):
    alpha.append(pp/pd)
for ap, yp in zip(alpha,ydata):
    y_pom.append(-ap*yp)

y_pomerr=[0.25/y*ap+0.06*ypom for y,ypom,ap in zip(ydata,y_pom,alpha)]
alphaerr=[0.06*ap for ap in alpha]

popt1, pcov1 = opt(linear_fun,xdata,alpha)
perr1 = np.sqrt(np.diag(pcov1))
print('C=',popt1[0],'+/-',perr1[0],'D=',popt1[1],'+/-',perr1[1])
x=np.linspace(min(xdata)-1,max(xdata)+1,50000)
y1=linear_fun(x,*popt1)

popt2, pcov2 = opt(linear_fun,xdata,y_pom)
perr2 = np.sqrt(np.diag(pcov2))
print('A=',popt2[0],'+/-',perr2[0],'B=',popt2[1],'+/-',perr2[1])
x=np.linspace(min(xdata)-1,max(xdata)+1,50000)
y2=linear_fun(x,*popt2)

fig=plt.figure()

ax=fig.add_subplot(211)
ax.errorbar(xdata,alpha,yerr=alphaerr,xerr=xerr, fmt='.')
ax.plot(x,y1)
ax.grid(True)
ax.set_title('CX+D')
ax.set_ylabel('Powiekszenie obrazu')

bx=fig.add_subplot(212)
bx.errorbar(xdata,y_pom,yerr=y_pomerr,xerr=xerr, fmt='.')
bx.plot(x,y2)
bx.grid(True)
bx.set_title('AX+B')
bx.set_xlabel('Odległosć miedzy przedmiotem i soczewka X [cm]')
bx.set_ylabel('-Y * powiekszenie obrazu [cm]')

plt.show()
#plt.savefig('soczewka3.eps')