# Ordinary Differential Equations

A small, from-scratch collection of fixed-step numerical solvers for ordinary differential equations, accompanied by mathematical walkthroughs and animated applications. The project covers scalar and state-vector initial value problems (IVPs), coupled systems, higher-order equations, linear boundary value problems (BVPs), population models, and chaotic dynamics.

> This is an educational implementation built with NumPy. It is useful for studying numerical methods and experimenting with ODE models; for production scientific computing, prefer a mature solver such as `scipy.integrate.solve_ivp` or `scipy.integrate.solve_bvp`.

https://github.com/user-attachments/assets/77b3ca64-fb23-4500-be51-931f0a997506
<p align="center">
    Numerical simulation of two double pendulums with nearly identical initial conditions.
</p>

## Features

- First-order IVPs of the form $y' = f(x, y)$
- Second-order IVPs of the form $y'' + P(x,y)y' = Q(x,y)$
- State-vector IVPs of the form $\vec{r}'(t)=f(t,\vec{r})$, including coupled systems and higher-order ODEs rewritten as first-order systems
- Euler, midpoint, Heun, and classical fourth-order Runge–Kutta (RK4) methods
- Linear second-order BVPs solved with finite differences and the Thomas tridiagonal algorithm
- Explanatory Jupyter notebooks that derive the methods, introduce state vectors, and compare numerical results with analytical solutions
- Matplotlib animations for pendulums, spring–mass systems, population growth, the error function, and the Lorenz attractor

## Numerical methods

| Method | Scalar first-/second-order IVP | State-vector IVP | Expected global order |
| --- | --- | --- | ---: |
| Euler | `solver.ivp.euler_method` | `solver.ivp.state_euler_method` | $O(h)$ |
| Explicit midpoint | `solver.ivp.midpoint_method` | `solver.ivp.state_midpoint_method` | $O(h^2)$ |
| Heun / improved Euler | `solver.ivp.heun_method` | `solver.ivp.state_heun_method` | $O(h^2)$ |
| Classical RK4 | `solver.ivp.rk4` | `solver.ivp.state_rk4` | $O(h^4)$ |

The state-vector methods solve systems in the form

$$
\frac{d\vec{r}}{dt}=f(t,\vec{r}), \qquad \vec{r}(a)=\vec{r}_0.
$$

Representing the dependent variables and their derivatives in one NumPy vector makes the same four methods applicable to coupled systems and ODEs of arbitrary order after reduction to a first-order system.

The BVP function `solver.bvp.fdm` uses second-order central finite differences for linear equations, giving an expected global order of $O(h^2)$.

The BVP solver handles equations in the form

$$
y'' + P(x)y' + Q(x)y = R(x), \qquad y(a)=y_a, \quad y(b)=y_b.
$$

It stores only the three diagonals of the resulting linear system and solves them directly instead of constructing a dense $(N-1)\times(N-1)$ matrix.

## Installation

### Prerequisites

- Python 3.12 or newer
- Git

### Using `uv` (recommended)

[`uv`](https://docs.astral.sh/uv/) uses the checked-in lockfile to create a reproducible environment.

#### Linux and macOS

```bash
git clone https://github.com/OjasRane/Ordinary-Differential-Equations.git
cd Ordinary-Differential-Equations
uv sync --locked
uv run jupyter lab
```

#### Windows (PowerShell)

```powershell
git clone https://github.com/OjasRane/Ordinary-Differential-Equations.git
Set-Location Ordinary-Differential-Equations
uv sync --locked
uv run jupyter lab
```

### Using `pip`

#### Linux and macOS

```bash
git clone https://github.com/OjasRane/Ordinary-Differential-Equations.git
cd Ordinary-Differential-Equations
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m jupyter lab
```

#### Windows (PowerShell)

```powershell
git clone https://github.com/OjasRane/Ordinary-Differential-Equations.git
Set-Location Ordinary-Differential-Equations
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
python -m jupyter lab
```

## Quick start

Run commands from the project root so that Python can import the local `solver` package.

### First-order IVP

Solve $y'=y$, $y(0)=1$, over $[0,1]$:

```python
import matplotlib.pyplot as plt

from solver import ivp

x, y = ivp.rk4(
    0.0,
    1.0,
    0.01,
    func=lambda x, y: y,
    initial=1.0,
)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
```

### Second-order IVP

For $y'' + P(x,y)y'=Q(x,y)$, omit `func` and provide `p`, `q`, and the initial slope. This example solves $y''=-y$, $y(0)=0$, $y'(0)=1$:

```python
from solver import ivp

x, y = ivp.rk4(
    0.0,
    10.0,
    0.01,
    p=lambda x, y: 0.0,
    q=lambda x, y: -y,
    initial=0.0,
    initial_slope=1.0,
)
```

### Coupled system with a state vector

State-vector methods accept a derivative function that returns one derivative for every state variable. This example solves $x'=v$, $v'=-x$ with $x(0)=0$ and $v(0)=1$:

```python
import numpy as np

from solver import ivp

def harmonic_oscillator(t, state):
    x, velocity = state
    return np.array([velocity, -x])

t, solution = ivp.state_rk4(
    0.0,
    10.0,
    0.01,
    harmonic_oscillator,
    np.array([0.0, 1.0]),
)

x = solution[0]
velocity = solution[1]
```

### Boundary value problem

Solve $y''-4y=4x$, with $y(0)=0$ and $y(1)=2$:

```python
import numpy as np

from solver import bvp

x, y = bvp.fdm(
    0.0,
    1.0,
    0.01,
    p=lambda x: np.zeros_like(x),
    q=lambda x: -4 * np.ones_like(x),
    r=lambda x: 4 * x,
    initial=0.0,
    end=2.0,
)
```

Scalar IVP and BVP solvers return `(x, y)`. State-vector IVP solvers return `(t, solution)`, where `solution` has shape `(number_of_states, number_of_time_points)`. The grids include both endpoints when the step size divides the interval exactly.

## API conventions and current scope

- `a` and `b` are the interval boundaries and `h` is a fixed step size.
- For first-order IVPs, `func` must accept `(x, y)` and `initial` supplies $y(a)$.
- For second-order IVPs, `p` and `q` must accept `(x, y)`; `initial` and `initial_slope` supply $y(a)$ and $y'(a)$.
- For state-vector IVPs, `func(t, state)` must return a one-dimensional derivative array matching the one-dimensional `initial_state` array.
- For BVPs, `p`, `q`, and `r` must accept NumPy arrays and return broadcast-compatible arrays. `initial` and `end` are the two boundary values.
- The grid uses `N = int((b - a) / h)`. Choose a positive `h` that divides the interval exactly if the final grid point must equal `b`.
- All methods use real-valued `float64` arrays and fixed steps. They do not provide adaptive error control, event detection, stiffness handling, dense output, or argument validation.
- The finite-difference BVP implementation remains limited to scalar, linear second-order equations.

## Notebooks

| Notebook | Contents |
| --- | --- |
| [`solving_ivp_problems.ipynb`](analysis/solving_ivp_problems.ipynb) | Euler, midpoint, Heun, and RK4 derivations; scalar and state-vector IVPs; coupled systems; Lorenz attractor |
| [`solving_bvp_problems_using_fdm.ipynb`](analysis/solving_bvp_problems_using_fdm.ipynb) | Finite-difference derivation, tridiagonal system construction, and comparison with an analytical solution |
| [`population_models.ipynb`](analysis/population_models.ipynb) | Exponential growth, logistic growth, carrying capacity, and the Allee effect |
| [`erf_function_using_ode.ipynb`](analysis/erf_function_using_ode.ipynb) | Computing and plotting the error function as an IVP |

## Animations

The repository includes interactive scripts and pre-rendered media:

| Demo | Source | Rendered output |
| --- | --- | --- |
| Simple pendulum | [`simple_pendulum.py`](animation_scripts/simple_pendulum.py) | [`simple_pendulum.gif`](animation_scripts/animations/simple_pendulum.gif) |
| Undamped spring–mass system | [`spring_mass.py`](animation_scripts/spring_mass.py) | [`spring_mass.gif`](animation_scripts/animations/spring_mass.gif) |
| Damped spring–mass system | [`damped_shm.py`](animation_scripts/damped_shm.py) | [`damped_shm.mp4`](animation_scripts/animations/damped_shm.mp4) |
| Population model with the Allee effect | [`population_modelling.py`](animation_scripts/population_modelling.py) | [`population_modelling.gif`](animation_scripts/animations/population_modelling.gif) |
| Error function | [`erf.py`](animation_scripts/erf.py) | [`erf.gif`](animation_scripts/animations/erf.gif) |
| Double pendulum | [`double_pendulum.py`](animation_scripts/double_pendulum.py) | [`double_pendulum.mp4`](animation_scripts/animations/double_pendulum.mp4) |
| Lorenz attractor | [`lorenz_attractor.py`](animation_scripts/lorenz_attractor.py) | [`lorenz_attractor.mp4`](animation_scripts/animations/lorenz_attractor.mp4) |

Open an interactive Matplotlib window for any demo from the repository root, for example:

```bash
uv run python animation_scripts/simple_pendulum.py
```

The current scripts display animations with `plt.show()`; the rendered GIF and MP4 files are already included separately under `animation_scripts/animations/`.

## Project structure

```text
.
├── solver/
│   ├── __init__.py
│   ├── README.md                      # Solver API and numerical-method guide
│   ├── ivp.py                         # Fixed-step IVP methods
│   └── bvp.py                         # Finite-difference BVP solver
├── analysis/
│   ├── README.md                      # Notebook guide and learning path
│   ├── solving_ivp_problems.ipynb
│   ├── solving_bvp_problems_using_fdm.ipynb
│   ├── population_models.ipynb
│   └── erf_function_using_ode.ipynb
├── animation_scripts/
│   ├── animations/                    # Pre-rendered GIF and MP4 files
│   ├── README.md                      # Animation gallery and usage guide
│   ├── damped_shm.py
│   ├── double_pendulum.py
│   ├── erf.py
│   ├── lorenz_attractor.py
│   ├── population_modelling.py
│   ├── simple_pendulum.py
│   └── spring_mass.py
├── pyproject.toml                     # Package metadata and direct dependencies
├── requirements.txt                   # pip-compatible dependency list
├── uv.lock                            # Fully resolved dependency lockfile
└── README.md
```

## Dependencies

| Package | Minimum version | Purpose |
| --- | ---: | --- |
| NumPy | 2.5.3 | Numerical arrays and solver calculations |
| Matplotlib | 3.11.1 | Plots and animations |
| JupyterLab | 4.6.3 | Interactive notebooks |

Exact transitive versions are recorded in `uv.lock`.

## Usage of AI

- All modules have code written entirely by me.
- AI was used for better understanding of the concepts.
- Draft for READMEs were generated by AI and were modified by me, for better explanation.

## Future Scope

The numerical solvers are currently implemented in Python using NumPy. A future version of the project will move the computational core to C++, with Python bindings provided through pybind11.

Python will continue to be used for experimentation, notebooks, and visualization with Matplotlib, while the underlying numerical methods will be implemented in C++.

Planned directions include:

- Porting the IVP and BVP solvers to C++
- Exposing the C++ implementation to Python using pybind11
- Exploring adaptive step-size methods

## License

This project is available under the [MIT License](LICENSE).
