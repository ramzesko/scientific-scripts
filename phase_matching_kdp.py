import numpy as np
import matplotlib.pyplot as plt


# współczynniki z sellmeiera dla 694.3 nm
# n0_2w = 1.531143447
# ne_2w = 1.485795648
# n0_1w = 1.50502213
# ne_1w = 1.465318989
# współczynniki z sellmeiera dla 800 nm
n0_2w = 1.524034577
ne_2w = 1.479813761
n0_1w = 1.501507292
ne_1w = 1.463302793
# współczynniki z sellmeiera dla 685.4 nm
# n0_2w=1.533625296
# ne_2w=1.487902849
# n0_1w=1.505347113
# ne_1w=1.465521264

theta = np.linspace(-np.pi, np.pi, 5000)

ne_theta_2w = 0.5 * (n0_1w + n0_1w*ne_1w / (np.sqrt(np.cos(theta)**2 * ne_1w**2 + np.sin(theta)**2 * n0_1w**2)))

P = 1 / ne_theta_2w**2
L = np.cos(theta)**2 / n0_2w**2 + np.sin(theta)**2 / ne_2w**2

plt.plot(np.rad2deg(theta), L)
plt.plot(np.rad2deg(theta), P)
plt.xlabel('Kat theta [deg]')
plt.ylabel('Prawa/lewa strona równania (8).')
plt.show()
# plt.savefig('rownanie.eps')
