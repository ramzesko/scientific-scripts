import matplotlib.pyplot as plt


file = r'ścieżka-do-pliku'
k = 2.45
R = 100
xdata = []
ydata = []
with open(file, 'r') as f:
    for line in f.readlines():
        if line[0] != '#':
            xdata.append(float(line.split()[0]))
            ydata.append(float(line.split()[1]))

xerr = [0.1 for x in xdata]
yerr = [0.005 * y + 0.02 for y in ydata]

# rysowanie i wyświetlenie wykresu
fig = plt.figure()
ax = fig.add_subplot(111)
ax.errorbar(xdata, ydata, yerr=yerr, xerr=xerr, fmt='.')
# ax.plot(xdata, ydata, 'o')
ax.grid(True)

plt.show()
