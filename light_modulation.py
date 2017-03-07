import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as opt


def linear_fun(x, a, b):
    return a * x + b


def gauss(x, A0, A, x0, sigma):
    return A0 + A * np.exp(-(x-x0)**2 / (2*sigma**2)) / (sigma * np.sqrt(2*np.pi))

file = r'sciezka\plik.txt'

freq = []
imin = []
imax = []
dc = []

with open(file, 'r') as f:
    for line in f.readlines():
        try:
            freq.append(float(line.split()[0]))
            imin.append(float(line.split()[1]))
            imax.append(float(line.split()[2]))
        except:
            pass
        try:
            constant = float(line.split()[3])
            dc.append(constant)
        except:
            dc.append(constant)

freq = np.array(freq)
imin = np.array(imin)
imax = np.array(imax)
dc = np.array(dc)

imax = dc + imax
imin = dc - imin
c = np.array((imax-imin) / (imin+imax))
k = np.array((imax-imin) / 153)

popt1, pcov1 = opt(gauss, freq, c)
perr1 = np.sqrt(np.diag(pcov1))
print('A=', popt1[0], '+/-', perr1[0], 'B=', popt1[1], '+/-', perr1[1])
x = np.linspace(0, max(freq), 50000)
y1 = gauss(x, *popt1)

plt.plot(freq, c, 'ro')
# plt.plot(x, y1)
plt.grid(True)
plt.title('Modulator akustooptyczny')
plt.xlabel('Czestotliwosć modulacji [Hz]')
plt.ylabel('Wspólczynnik przenoszenia amplitudy')
plt.show()
# plt.savefig('elektrooptycznyamp.eps')
