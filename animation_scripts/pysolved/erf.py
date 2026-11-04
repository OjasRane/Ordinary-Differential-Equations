import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import ivp

func = lambda x, y: 2*np.exp(-x**2)/np.sqrt(np.pi)
a = 0
b = 32
h = 0.01
initial = 0

x, y = ivp.rk4(a, b, h, initial=initial, func=func)
step = 30
x = x[::step]
y = y[::step]

fig, ax = plt.subplots()
ax.set_xlim(-b, b)
ax.set_ylim(-1.2, 1.2)
fig.suptitle("Solution to: "+r"$\frac{dy}{dx}=\frac{2}{\sqrt{\pi}}{e^{-x^2}}$", fontsize=20)
ax1, = ax.plot([], [], color="red")
ax2, = ax.plot([], [], color="red")
ax.grid()

def update(frame):
    ax1.set_data(x[:frame], y[:frame])
    ax2.set_data(-x[:frame], -y[:frame])
    return ax1, ax2

anim = FuncAnimation(
    fig=fig,
    func=update,
    interval=20,
    frames=len(x),
    repeat=False
)

plt.show()