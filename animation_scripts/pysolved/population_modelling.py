import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import ivp

r = 0.02
K = 1000
T = 50
initial = 100

func = lambda t, P: -r*P*(1-P/K)*(1-P/T)
a = 0
b = 80
h = 0.01

t, P = ivp.rk4(a, b, h, func=func, initial=initial)
step = int(1 / h)
P = P[::step]
t = t[::step]

fig, ax = plt.subplots(figsize=(10, 8))
fig.suptitle("Population Modelling using Allee's modification", fontsize=12)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
rng = np.random.default_rng(42)
scatter = ax.scatter([], [], label="10 individuals", marker="o")
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect("equal")
ax.legend(loc="upper right")

def update(frame):
    scatter.set_offsets(rng.uniform(low=0.5, high=9.5, size=(int(P[frame]/10), 2)))
    ax.set_title(f"Initial Population: {initial}, Carrying Capacity: {K}, Threshold Population: {T}\nYear: {t[frame]}"+r"$\qquad$"+f"Population: {int(P[frame])}")
    return scatter,

anim = FuncAnimation(fig=fig,
                    func=update,
                    interval=150,
                    frames=len(t),
)

plt.show()