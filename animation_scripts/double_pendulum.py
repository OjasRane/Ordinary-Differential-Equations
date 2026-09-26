import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from solver import ivp

g = 9.81
L1 = 5
L2 = 2
m1 = 10
m2 = 2

def func(t, state):
    theta1, w1, theta2, w2 = state[0], state[1], state[2], state[3]
    denominator = 2*m1 + m2 - m2*np.cos(2*theta1 - 2*theta2)
    return np.array([
        w1,
        (-g*(2*m1+m2)*np.sin(theta1) - m2*g*np.sin(theta1-2*theta2) - 2*np.sin(theta1-theta2)*m2*((w2**2)*L2+(w1**2)*L1*np.cos(theta1-theta2)))/(L1*denominator),
        w2,
        (2*np.sin(theta1-theta2) * ( (w1**2)*L1*(m1+m2) + g*(m1+m2)*np.cos(theta1) + (w2**2)*L2*m2*np.cos(theta1-theta2) ))/(L2*denominator)
    ])

a = 0
b = 30
h = 0.001
initial_state1 = np.array([np.pi/2, 0, np.pi, 0])
initial_state2 = np.array([(np.pi/2)-0.01, 0, np.pi, 0])

t, solution1 = ivp.state_rk4(a, b, h, func, initial_state1)
t, solution2 = ivp.state_rk4(a, b, h, func, initial_state2)

fig, ax = plt.subplots(figsize=(12, 10))
ax.set_title("Double Pendulum\nTwo systems with nearly identical initial state"+r"$(\Delta\theta_1=0.01).$", fontsize=16)
ax.set_xlim(-(L1+L2+1), L1+L2+1)
ax.set_ylim(-(L1+L2+1), L1+L2+1)
ax.set_aspect('equal')
ax.grid()

string1_1, = ax.plot([], [], color="red", lw=2, label=r"$\text{Initial Condition: }\langle \theta_1, \omega_1, \theta_2, \omega_2\rangle=\langle\frac{\pi}{2}, 0, \pi, 0\rangle$")
string2_1, = ax.plot([], [], color="red", lw=2, label=r"$\text{Initial Condition: }\langle \theta_1, \omega_1, \theta_2, \omega_2\rangle=\langle\frac{\pi}{2}, 0, \pi, 0\rangle$")
bob1_1, = ax.plot([], [], "o", color="red", markersize=11, label=r"$\text{Initial Condition: }\langle \theta_1, \omega_1, \theta_2, \omega_2\rangle=\langle\frac{\pi}{2}, 0, \pi, 0\rangle$")
bob2_1, = ax.plot([], [], "o", color="red", markersize=11, label=r"$\text{Initial Condition: }\langle \theta_1, \omega_1, \theta_2, \omega_2\rangle=\langle\frac{\pi}{2}, 0, \pi, 0\rangle$")

string1_2, = ax.plot([], [], color="green", lw=2, label=r"$\text{Initial Condition: }\langle \theta_1, \omega_1, \theta_2, \omega_2\rangle=\langle\frac{\pi}{2}-0.01, 0, \pi, 0\rangle$")
string2_2, = ax.plot([], [], color="green", lw=2, label=r"$\text{Initial Condition: }\langle \theta_1, \omega_1, \theta_2, \omega_2\rangle=\langle\frac{\pi}{2}-0.01, 0, \pi, 0\rangle$")
bob1_2, = ax.plot([], [], "o", color="green", markersize=11, label=r"$\text{Initial Condition: }\langle \theta_1, \omega_1, \theta_2, \omega_2\rangle=\langle\frac{\pi}{2}-0.01, 0, \pi, 0\rangle$")
bob2_2, = ax.plot([], [], "o", color="green", markersize=11, label=r"$\text{Initial Condition: }\langle \theta_1, \omega_1, \theta_2, \omega_2\rangle=\langle\frac{\pi}{2}-0.01, 0, \pi, 0\rangle$")

pivot, = ax.plot([0], [0], "o", label="Pivot", color="black", markersize=6)
ax.legend(handles=[pivot, string1_1, string1_2], loc="upper right", fontsize=12)
ax.set_xticklabels([])
ax.set_yticklabels([])

POINTS_PER_FRAME = 30
def update(frame):
    frame = frame * POINTS_PER_FRAME
    theta1_1, theta2_1 = solution1[0], solution1[2]
    string1_1.set_data([0, L1*np.sin(theta1_1[frame])], [0, -L1*np.cos(theta1_1[frame])])
    string2_1.set_data([L1*np.sin(theta1_1[frame]), L1*np.sin(theta1_1[frame]) + L2*np.sin(theta2_1[frame])], [-L1*np.cos(theta1_1[frame]), -L1*np.cos(theta1_1[frame]) - L2*np.cos(theta2_1[frame])])
    bob1_1.set_data([L1*np.sin(theta1_1[frame])], [-L1*np.cos(theta1_1[frame])])
    bob2_1.set_data([L1*np.sin(theta1_1[frame]) + L2*np.sin(theta2_1[frame])], [-L1*np.cos(theta1_1[frame]) - L2*np.cos(theta2_1[frame])])

    theta1_2, theta2_2 = solution2[0], solution2[2]
    string1_2.set_data([0, L1*np.sin(theta1_2[frame])], [0, -L1*np.cos(theta1_2[frame])])
    string2_2.set_data([L1*np.sin(theta1_2[frame]), L1*np.sin(theta1_2[frame]) + L2*np.sin(theta2_2[frame])], [-L1*np.cos(theta1_2[frame]), -L1*np.cos(theta1_2[frame]) - L2*np.cos(theta2_2[frame])])
    bob1_2.set_data([L1*np.sin(theta1_2[frame])], [-L1*np.cos(theta1_2[frame])])
    bob2_2.set_data([L1*np.sin(theta1_2[frame]) + L2*np.sin(theta2_2[frame])], [-L1*np.cos(theta1_2[frame]) - L2*np.cos(theta2_2[frame])])
    return bob1_1, bob2_1, string1_1, string2_1, bob1_2, bob2_2, string1_2, string2_2

ani = FuncAnimation(
    fig=fig,
    frames=len(t) // POINTS_PER_FRAME,
    func=update,
    interval=30,
    repeat=False
)
plt.show()
