import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as opt


'''
Zmieniając dane pomiarowe należy zaktualizować następujące dane wejściowe:
-ścieżkę do pliku zawierającego w pierszej kolumnie współrzędne przestrzenne a w drugiej napięcie/amplitudę sygnału
-odległość źródła od detektora wzdłuż osi równoległej do biegu wiązki
-niepewność pomiaru napięcia wg specyfikacji urządzenia pomiarowego przy wykorzystywanym zakresie
'''

# tutaj ścieżka do pliku z danymi
file = r'pełna-ścieżka-do-pliku'

# dodatkowe parametry do wyznaczenia apertury numerycznej (L-odległość w mm)
L = 60


# definicja funkcji Gaussa
def gauss(x, A, x0, sigma):
    return A * np.exp(-(x-x0)**2 / (2*sigma**2)) / (sigma * np.sqrt(2 * np.pi))


# wczytywanie punktów pomiarowych z pliku
xdata = []
ydata = []
with open(file, 'r') as f:
    for line in f.readlines():
        if line[0] != '#':
            xdata.append(float(line.split()[0]))
            ydata.append(float(line.split()[1]))

# definicja niepewności pomiarowych
xerr = [0.1 for x in xdata]
yerr = [0.005 * y + 0.02 for y in ydata]

# dopasowanie funkcji Gaussa i wypisanie parametrów dopasowania
popt, pcov = opt(gauss, xdata, ydata)
perr = np.sqrt(np.diag(pcov))
print('A=', popt[0], '+/-', perr[0], 'x0=', popt[1], '+/-', perr[1], 'sigma=', popt[2], '+/-', perr[2])

# próbkowanie rozkładu przed wykreśleniem
x = np.linspace(min(xdata), max(xdata), 500000)
y = gauss(x, *popt)

# liczenie apertury numerycznej
ymax = gauss(popt[1], *popt)
y5 = 0.05 * ymax
diff_list = []
arg_list = []
for arg in x:
    diff = np.fabs(gauss(arg, *popt) - y5)
    if diff < 0.002:
        diff_list.append(diff)
        arg_list.append(arg)
arg_left = [element for element in arg_list if element < popt[1]]
diff_left = diff_list[:len(arg_left)]
arg_right = [element for element in arg_list if element > popt[1]]
diff_right = diff_list[len(arg_right):]
left_border = arg_left[np.argmin(diff_left)]
right_border = arg_right[np.argmin(diff_right)]
W = (np.abs(popt[1] - left_border) + np.abs(popt[1] - right_border)) / 2
NA = W / np.sqrt(W**2 + L**2)

# oszacowanie niepewności - dL narzucona z góry znacznie przewyższa dW w przybliżeniu równe 2*dx0
dW = 0.071
dL = 5

dNA = np.sqrt((L**2 / (W**2 + L**2)**1.5)**2 * dW**2 + (W * L / (W**2 + L**2)**1.5)**2 * dL**2)
print(NA, '+/-', dNA)
print(left_border, right_border)

# rysowanie i wyświetlenie wykresu
fig = plt.figure()
ax = fig.add_subplot(111)
ax.errorbar(xdata, ydata, yerr=yerr, xerr=xerr, fmt='.')
ax.plot(x, y)
ax.grid(True)
ax.set_title('Tytuł')
ax.set_xlabel('Pozycja [mm]')
ax.set_ylabel('Napiecie [V]')

plt.annotate(s='11.842(47) mm', xy=(popt[1], ymax), xytext=(6, 1.3), arrowprops={'arrowstyle': '-|>'})
plt.annotate('5.423(49) mm', xy=(left_border, y5), xytext=(4.5, 0.4), arrowprops={'arrowstyle': '-|>'})
plt.annotate('18.261(49) mm', xy=(right_border, y5), xytext=(16.5, 0.4), arrowprops={'arrowstyle': '-|>'})

plt.show()
# plt.savefig('1554aperture.eps')

