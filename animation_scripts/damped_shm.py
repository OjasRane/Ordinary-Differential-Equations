import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import ivp

m = 1
k = 4
c = 0.5

a = 0
b = 30
h = 0.01
p = lambda t, x: c/m
q = lambda t, x: -(k/m)*x

data = {
    "p": p,
    "q": q,
    "initial": 1,
    "initial_slope": 0
}

t, x = ivp.rk4(a, b, h, **data)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))
ax1.set_xlim(-2, 2)
ax1.set_xticklabels([])
ax1.set_yticklabels([])
fig.suptitle(r"Spring mass system following: "+r"$\frac{d^2x}{dt^2}+\frac{c}{m}\frac{dy}{dt}=-\frac{k}{m}x$", fontsize=20)
ax1.set_title(f"Damped spring mass system simulation with damping coefficient: {c} "+r"$N\cdot s/m$")
spring, = ax1.plot([], [], color="red", label=f"Spring with spring constant: {k} N/m")
mass, = ax1.plot([], [], "s", color="blue", markersize=18, label=f"Mass: {m} kg")
ax1.legend(
    borderpad=1.2,
    framealpha=0.8,
    fontsize=12
)
ax1.grid()

x_vs_t, = ax2.plot([], [])
ax2.set_xlabel("Time"+r"$\longrightarrow$")
ax2.set_ylabel(r"$Position$"+r"$\longrightarrow$")
ax2.set_xlim(a, b)
ax2.set_ylim(-1.2, 1.2)
ax2.grid()

def update(frame):
    spring.set_data([-2, x[frame]], [0, 0])
    spring.set_linewidth(abs(x[frame] - 4)*2)
    mass.set_data([x[frame]], [0])
    x_vs_t.set_data(t[:frame], x[:frame])
    return mass, spring, x_vs_t

anim = FuncAnimation(
    fig=fig,
    func=update,
    interval=20,
    frames=900
)

plt.show()