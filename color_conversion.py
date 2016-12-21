from colormath.color_objects import SpectralColor, xyYColor
from colormath.color_conversions import convert_color
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

files=[r'widmo1',
       r'widmo2',
       r'widmo3',
       r'widmo4']
data=[]
values=[]
for i in range(4):
    with open(files[i]) as f:
        data.append(f.read())
for i in data:
    values.append(i.split())
xmono=[]
ymono=[]
monoframe=np.zeros(50)
for i in range(50):
    monoframe[i]=1
    mono = SpectralColor(*monoframe, observer='2', illuminant='d65')
    mono = convert_color(mono, xyYColor)
    xmono.append(mono.get_value_tuple()[0])
    ymono.append(mono.get_value_tuple()[1])
    monoframe[i]=0

zarowka=SpectralColor(*values[0], observer='2', illuminant='d65')
halogen=SpectralColor(*values[1], observer='2', illuminant='d65')
led=SpectralColor(*values[2], observer='2', illuminant='d65')
swietlowka=SpectralColor(*values[3], observer='2', illuminant='d65')
zarowka_xyY=convert_color(zarowka, xyYColor)
halogen_xyY=convert_color(halogen, xyYColor)
led_xyY=convert_color(led, xyYColor)
swietlowka_xyY=convert_color(swietlowka, xyYColor)
x1=zarowka_xyY.get_value_tuple()[0]
y1=zarowka_xyY.get_value_tuple()[1]

x2=halogen_xyY.get_value_tuple()[0]
y2=halogen_xyY.get_value_tuple()[1]
x3=led_xyY.get_value_tuple()[0]
y3=led_xyY.get_value_tuple()[1]
x4=swietlowka_xyY.get_value_tuple()[0]
y4=swietlowka_xyY.get_value_tuple()[1]
print(zarowka_xyY)
print(halogen_xyY)
print(swietlowka_xyY)
print(led_xyY)
T=np.arange(1300,6500,100)
xplanck=[]
yplanck=[]

for v in T:
    try:
        if v<=2222:
            x=(-0.2661239e9/v/v/v-0.234358e6/v**2+0.8776956e3/v+0.17991)
            xplanck.append(x)
            yplanck.append(-1.1063814*x**3 - 1.3481102*x**2 + 2.18555832*x - 0.20219683)

        elif v>2222 and v<=4000:
            x=(-0.2661239*(1e9/v/v/v)-0.234358*(1e6/v**2)+0.8776956*(1e3/v)+0.17991)
            xplanck.append(x)
            yplanck.append(-0.9549476*x**3
               - 1.37418593*x**2
               + 2.09137015*x - 0.16748867)

        else:
            x=(-3.0258469e9/v/v/v+2.1070379e6/v/v+0.2226347e3/v+0.24039)
            xplanck.append(x)
            yplanck.append(3.081758*x**3
               - 5.8733867*x**2
               + 3.75112997*x - 0.37001483)
    except: pass

plt.grid(True)
plt.plot(xplanck,yplanck, color='cyan')
plt.plot(xmono,ymono, color='black')
plt.plot(x1,y1, 'ro', color='red')
plt.plot(x2,y2, 'bo', color='blue')
plt.plot(x3,y3, 'go', color='green')
plt.plot(x4,y4, 'yo', color='yellow')
plt.plot(0.31271,0.32902, color='purple', marker='*')
t1 = mpatches.Patch(color='red', label='Zarówka wolframowa')
t2 = mpatches.Patch(color='green', label='LED')
t3 = mpatches.Patch(color='blue', label='Zarówka halogenowa')
t4 = mpatches.Patch(color='yellow', label='Swietlówka Polux Platinum')
t5 = mpatches.Patch(color='purple', label='Punkt bieli (6500 K)')
plt.legend(handles=[t1,t2,t3,t4,t5], loc='upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.annotate(s='400 nm',xy=(xmono[6],ymono[6]),xytext=(0.2,0.05),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='500 nm',xy=(xmono[16],ymono[16]),xytext=(0.05,0.5),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='600 nm',xy=(xmono[26],ymono[26]),xytext=(0.6,0.3),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='550 nm',xy=(xmono[21],ymono[21]),xytext=(0.25,0.6),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='520 nm',xy=(xmono[18],ymono[18]),xytext=(0.1,0.7),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='2800 K',xy=(xplanck[14],yplanck[14]),xytext=(0.46,0.48),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='2700 K',xy=(xplanck[13],yplanck[13]),xytext=(0.48,0.48),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='2600 K',xy=(xplanck[12],yplanck[12]),xytext=(0.5,0.48),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='2500 K',xy=(xplanck[11],yplanck[11]),xytext=(0.52,0.48),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='2900 K',xy=(xplanck[15],yplanck[15]),xytext=(0.44,0.48),arrowprops={'arrowstyle':'-|>'})
plt.annotate(s='3000 K',xy=(xplanck[16],yplanck[16]),xytext=(0.42,0.48),arrowprops={'arrowstyle':'-|>'})
plt.show()
#plt.savefig('ścieżka-do-zapisu')