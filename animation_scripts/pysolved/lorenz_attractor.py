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
initial_state = np.array([0, 1, 0])

t, solution = ivp.state_rk4(a, b, h, func, initial_state)
x, y, z = solution[0], solution[1], solution[2]

fig = plt.figure()
fig.suptitle("Lorenz Attractor\n"+r"$\frac{dx}{dt}=\sigma(y-x)\qquad\frac{dy}{dt}=x(\rho - z)-y\qquad\frac{dz}{dt}=xy-\beta z$"+"\n"+r"$x_0=0\quad y_0=1\quad z_0=0$", fontsize=15)
ax = fig.add_subplot(111, projection="3d")
lorenz, = ax.plot([], [], [], lw=0.6)
point, = ax.plot([], [], [], "o", markersize=5, color="#FF4500")
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z))
ax.view_init(elev=10, azim=-45, roll=0)
ax.axis("off")

POINTS_PER_FRAME = 30
def update(frame):
    if frame*POINTS_PER_FRAME < len(t):
        lorenz.set_data(x[:frame*POINTS_PER_FRAME], y[:frame*POINTS_PER_FRAME])
        lorenz.set_3d_properties(z[:frame*POINTS_PER_FRAME])
        point.set_data([x[frame*POINTS_PER_FRAME]], [y[frame*POINTS_PER_FRAME]])
        point.set_3d_properties([z[frame*POINTS_PER_FRAME]])
    else:
        point.set_data([], [])
        point.set_3d_properties([])
    ax.view_init(elev=10, azim=-45+frame*0.3, roll=0)
    return lorenz

ani = FuncAnimation(
    fig=fig,
    func=update,
    interval=20,
    frames=len(t) // POINTS_PER_FRAME + 150,
    cache_frame_data=False,
    repeat=False
)
plt.show()
