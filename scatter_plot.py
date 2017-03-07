import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as opt


def linear_fun(x, a, b):
    return a * x + b


def quadratic_fun(x, a, b, c):
    return a * x**2 + b * x + c

file = r'sciezka\soczewka1.txt'

xdata = []
ydata = []
xfitdata = []
yfitdata = []

with open(file, 'r') as f:
    for line in f.readlines():
        try:
            xdata.append(float(line.split()[0]))
            ydata.append(float(line.split()[1]))
        except:
            pass

xerr = [0.5 for x in xdata]
yerr = [0.1 for y in ydata]

popt1, pcov1 = opt(linear_fun, xdata, ydata)
perr1 = np.sqrt(np.diag(pcov1))
print('A=', popt1[0], '+/-', perr1[0], 'B=', popt1[1], '+/-', perr1[1])
x = np.linspace(15, max(xdata), 50000)
y1 = linear_fun(x, *popt1)

# rysowanie i wyświetlenie wykresu
fig = plt.figure()
ax = fig.add_subplot(111)
# ax.errorbar(xdata,ydata,yerr=yerr,xerr=xerr, fmt='ro')
ax.plot(xdata, ydata, '.')
ax.grid(True)
ax.set_title('Zaleznosc mocy sygnału od ustawienia polaryzatora')
ax.set_xlabel('Kat polaryzacji [deg]')
ax.set_ylabel('Napiecie na detektorze [mV]')

plt.show()
# plt.savefig('polaryzacja.eps')
