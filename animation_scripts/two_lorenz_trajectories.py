import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import ivp

sigma = 10
rho = 28
beta = 8/3

def func(t, state):
    x, y, z = state[0], state[1], state[2]
    return np.array([
            sigma*(y-x),
            x*(rho-z)-y,
            x*y-beta*z
        ])

a = 0
b = 100
h = 0.001

t, solution1 = ivp.state_rk4(a, b, h, func, np.array([0, 1, 0]))
x1, y1, z1 = solution1[0], solution1[1], solution1[2]

t, solution2 = ivp.state_rk4(a, b, h, func, np.array([0.1, 1, 0]))
x2, y2, z2 = solution2[0], solution2[1], solution2[2]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set_xlim(np.min([np.min(x1), np.min(x2)]), np.max([np.max(x1), np.max(x2)]))
ax.set_ylim(np.min([np.min(y1), np.min(y2)]), np.max([np.max(y1), np.max(y2)]))
ax.set_zlim(np.min([np.min(z1), np.min(z2)]), np.max([np.max(z1), np.max(z2)]))
ax.axis("off")

one, = ax.plot([], [], [], label=r"$\vec{r}_0=\langle 0, 1, 0 \rangle$", lw=0.5)
two, = ax.plot([], [], [], label=r"$\vec{r}_0=\langle 0.1, 1, 0 \rangle$", lw=0.5)
ax.legend(loc="upper right")

SKIP = 30

def update(frame):
    if frame*SKIP < 500:
        one.set_data(x1[:frame*SKIP], y1[:frame*SKIP])
        one.set_3d_properties(z1[:frame*SKIP])
        two.set_data(x2[:frame*SKIP], y2[:frame*SKIP])
        two.set_3d_properties(z2[:frame*SKIP])
    else:
        one.set_data(x1[frame*SKIP-500:frame*SKIP], y1[frame*SKIP-500:frame*SKIP])
        one.set_3d_properties(z1[frame*SKIP-500:frame*SKIP])
        two.set_data(x2[frame*SKIP-500:frame*SKIP], y2[frame*SKIP-500:frame*SKIP])
        two.set_3d_properties(z2[frame*SKIP-500:frame*SKIP])
    ax.view_init(elev=10, azim=frame*0.3)
    return one, two

anim = FuncAnimation(
            fig=fig,
            frames=len(t) // SKIP,
            interval=20,
            func=update
        )
plt.show()
