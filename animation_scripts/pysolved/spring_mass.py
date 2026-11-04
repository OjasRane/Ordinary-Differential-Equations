import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import ivp

k = 100
m = 25

a = 0
b = 30
h = 0.01
p = lambda t, x: 0
q = lambda t, x: -(k/m)*x

data = {
    "p": p,
    "q": q,
    "initial": 2,
    "initial_slope": 0
}

t, x = ivp.rk4(a, b, h, **data)
fig, ax = plt.subplots()

ax.set_xlim(-3, 3)
ax.set_xticklabels([])
ax.set_yticklabels([])
fig.suptitle(r"Spring mass system following: "+r"$\frac{d^2x}{dt^2}=-\frac{k}{m}x$", fontsize=20)
spring, = ax.plot([], [], color="red", label=f"Spring with spring constant: {k} N/m")
mass, = ax.plot([], [], "s", color="blue", markersize=18, label=f"Mass: {m} kg")
ax.legend(
    borderpad=1.2,
    framealpha=0.8,
    fontsize=12
)
ax.grid()

def update(frame):
    spring.set_data([-3, x[frame]], [0, 0])
    spring.set_linewidth(abs(x[frame] - 4)*2)
    mass.set_data([x[frame]], [0])
    return mass, spring

anim = FuncAnimation(
    fig=fig,
    func=update,
    interval=20,
    frames=900,
    repeat=False
)

plt.show()