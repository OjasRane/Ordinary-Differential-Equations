import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from csolver import decoder

time = decoder.load("double_halvorsen_attractor_time.jcbi")
solution = decoder.load("double_halvorsen_attractor_solution.jcbi", dtype=np.float64)
x, y, z = solution[:, 0], solution[:, 1], solution[:, 2]

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(projection="3d")

ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(y), np.max(y))
ax.set_zlim(np.min(z), np.max(z))
ax.axis("off")
ax.view_init(20, 55)

ax.set_title("Halvorsen Attractor\n"+r"$\frac{dx}{dt}=-ax-4y-4z-y^2\qquad\frac{dy}{dt}=-ay-4z-4x-z^2\qquad\frac{dz}{dt}=-az-4x-4y-x^2$"+"\n"+r"$x_0=1\qquad y_0=0\qquad z_0=0$")

attractor, = ax.plot([], [], [], lw=0.05)

SKIP = 200

def update(frame):
    if frame*SKIP < len(time):
        attractor.set_data(x[:frame*SKIP], y[:frame*SKIP])
        attractor.set_3d_properties(z[:frame*SKIP])
    return attractor,

anim = FuncAnimation(
    fig=fig,
    frames=len(time) // SKIP,
    interval=20,
    func=update,
    cache_frame_data=False,
    repeat=False
)
plt.show()
