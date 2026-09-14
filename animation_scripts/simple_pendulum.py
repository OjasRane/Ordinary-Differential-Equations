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

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))
fig.suptitle(f"Simple Pendulum following the equation: "+r"$\frac{d^2\theta}{dt^2}=-\frac{g}{L}\sin{(\theta)}$", fontsize=16)
ax1.set_xlim(-L, L)
ax1.set_ylim(-L-0.5, 0.5)
ax1.set_xticklabels([])
ax1.set_yticklabels([])
ax1.set_aspect('equal')
ax1.grid()
string, = ax1.plot([], [], color="red", lw=2, label=f"String of length={L} m")
ax1.plot([0], [0], "o", markersize=8, color="black", label="Pivot")
bob, = ax1.plot([], [], "o", color="blue", label="Bob", markersize=18)
ax1.legend(loc="upper left")

ax2.set_xlim(a, b)
ax2.set_ylim(-data["initial"]-0.5, data["initial"]+0.5)
ax2.set_xlabel("Time"+r"$\longrightarrow$")
ax2.set_ylabel("Angle from vertical "+r"$(\theta)\longrightarrow$")
ax2.grid()
exact_solution, = ax2.plot([], [], color="red", label="Exact Solution: "+r"$\frac{d^2\theta}{dt^2}=-\frac{g}{L}\sin{(\theta)}$")
small_angle_approximation_solution, = ax2.plot([], [], color="green", label="Small Angle Approximation Solution: "+r"$\frac{d^2\theta}{dt^2}=-\frac{g}{L}\theta$")
ax2.legend(loc="upper right")
small_angle_approximation = lambda t: data["initial"] * np.cos(np.sqrt(g / L) * t)
small_angle_theta = small_angle_approximation(t)

def update(frame):
    string.set_data([0, L*np.sin(theta[frame])], [0, -L*np.cos(theta[frame])])
    bob.set_data([L*np.sin(theta[frame])], [-L*np.cos(theta[frame])])
    exact_solution.set_data(t[:frame], theta[:frame])
    small_angle_approximation_solution.set_data(t[:frame], small_angle_theta[:frame])
    return string, bob, exact_solution, small_angle_approximation_solution

anim = FuncAnimation(
    fig=fig,
    func=update,
    frames=900,
    interval=20
)

plt.show()
