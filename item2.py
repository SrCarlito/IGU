from math import sin, cos, exp, pi, e    # Importamos las funciones matematicas
import numpy as np                # Importamos numpy
import matplotlib.pyplot as plt   # Importamos matplotlib



def f1(t): return sin(t) * cos(1/(t))
def f2(t): return exp(-t) * cos(2*pi*t)
def f3(t): return sin(t) * cos(1/(t+0.1))
def f4(t): return -2 * pi * exp(-t) * sin(2*pi*t) - e**(-t) * cos(2*pi*t)


t1 = np.arange(-0.2, 0.2, 0.001)
t2 = np.arange(-5.0, 1.0, 0.10)
t3 = np.arange(-3.0, 2.0, 0.02)
t4 = np.arange(-5.0, 1.0, 0.10)

f = [f2, f4, f3, f1]
t = [t2, t4, t3, t1]


fig, ax = plt.subplots(2, 2)
ax = np.ravel(ax)


lines = [0,0,0,0]

for i in range(4):
    lines[i] = ax[i].plot(t[i], [f[i](x) for x in t[i]])
    ax[i].grid(True)
    ax[i].set_ylabel('f(t)')
    ax[i].set_xlabel('t')
    ax[i].set_title('función  f'+str(i+1))
    ax[i].grid(False)

ax[1].set_facecolor('lightgrey')

ax[3].set_facecolor('lightgrey')     
lines[3][0].set_color("green")

fig.tight_layout()
plt.show()
