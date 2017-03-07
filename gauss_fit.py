import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as opt


'''
Dopasowuje funkcję Gaussa do punktów pomiarowych wczytywanych z pliku tekstowego
'''

# tutaj ścieżka do pliku z danymi
file = r'sciezka/plik.txt'


# definicja funkcji Gaussa
def gauss(x, A, x0, sigma):
    return A * np.exp(-(x-x0)**2 / (2*sigma**2)) / (sigma * np.sqrt(2*np.pi))

# wczytywanie punktów pomiarowych z pliku
xdata = []
ydata = []
with open(file, 'r') as f:
    for line in f.readlines():
        if line[0] != '#':
            xdata.append(float(line.split()[0]))
            ydata.append(float(line.split()[1]))

# definicja niepewności pomiarowych - opcjonalne
xerr = [0.1 for x in xdata]
yerr = [0.005*y + 4 for y in ydata]

# dopasowanie funkcji Gaussa i wypisanie parametrów dopasowania
popt, pcov = opt(gauss, xdata, ydata)
perr = np.sqrt(np.diag(pcov))
print('A=', popt[0], '+/-', perr[0], 'x0=', popt[1], '+/-', perr[1], 'sigma=', popt[2], '+/-', perr[2])

# próbkowanie rozkładu przed wykreśleniem
x = np.linspace(min(xdata), max(xdata), 50000)
y = gauss(x, *popt)

# rysowanie i wyświetlenie wykresu
plt.errorbar(xdata, ydata, yerr=yerr, xerr=xerr, fmt='.')
plt.plot(x, y)
plt.grid(True)
plt.xlabel('Pozycja detektora [mm]')
plt.ylabel('Napiecie [mV]')
plt.show()
# plt.savefig('gauss.eps')

