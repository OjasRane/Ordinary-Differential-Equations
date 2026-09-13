import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import ivp

g = 9.81
L = 2

p = lambda t, theta: 0
q = lambda t, theta: -(g/L)*np.sin(theta)

a = 0
b = 30
h = 0.01

data = {
    "p": p,
    "q": q,
    "initial": np.deg2rad(60),
    "initial_slope": 0
}

t, theta = ivp.rk4(a, b, h, **data)

fig, ax = plt.subplots()
fig.suptitle(f"Simple Pendulum following the equation: "+r"$\frac{d^2\theta}{dt^2}=-\frac{g}{L}\sin{(\theta)}$", fontsize=16)
ax.set_xlim(-L, L)
ax.set_ylim(-L-0.5, 0.5)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_aspect('equal')
ax.grid()
string, = ax.plot([], [], color="red", lw=2, label=f"String of length={L} m")
ax.plot([0], [0], "o", markersize=8, color="black", label="Pivot")
bob, = ax.plot([], [], "o", color="blue", label="Bob", markersize=18)
ax.legend(loc="upper left")

def update(frame):
    string.set_data([0, L*np.sin(theta[frame])], [0, -L*np.cos(theta[frame])])
    bob.set_data([L*np.sin(theta[frame])], [-L*np.cos(theta[frame])])
    return string, bob

anim = FuncAnimation(
    fig=fig,
    func=update,
    frames=900,
    interval=20
)

plt.show()
