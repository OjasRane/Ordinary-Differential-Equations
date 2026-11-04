# Ordinary Differential Equations

This project is a collection of fixed-step numerical solvers for ordinary differential equations, with mathematical notebooks, animations, and Python and C++ implementations. It is intended for learning and experimentation. For production scientific computing, use a mature package such as `scipy.integrate`.

## What is included

- Scalar and state-vector initial value problem (IVP) solvers using Euler, midpoint, Heun, and classical fourth-order Runge–Kutta (RK4) methods.
- A finite-difference solver for linear, second-order boundary value problems (BVPs), using the Thomas algorithm to solve the resulting tridiagonal system.
- Jupyter notebooks that derive the methods and apply them to coupled systems, population models, and the error function.
- Matplotlib animations of pendulums, spring–mass systems, population growth, the error function, and chaotic systems.
- A C++ solver library, C++ animation example, and Python and C++ benchmark programs.

## Python setup

Python 3.12 or newer is required. From the repository root, create the environment with `uv`:

```bash
uv sync --locked
```

Or install the project into a virtual environment with pip:

```bash
python3.12 -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
```

## Dependencies

| Dependency | Used for |
| --- | --- |
| [NumPy](https://numpy.org/) | Array storage and numerical calculations in the Python solvers, notebooks, and examples. |
| [Matplotlib](https://matplotlib.org/) | Plotting numerical results and displaying the Python animations. |
| [JupyterLab](https://jupyter.org/) | Running the project's explanatory notebooks. |
| [Jacobi](https://github.com/OjasRane/Jacobi) | A from-scratch C++20 numerical computing library developed by Ojas Rane, project author. The C++ ODE solver uses Jacobi's vector and matrix types and numerical operations. |

NumPy, Matplotlib, and JupyterLab are installed with the Python setup above. The `uv.lock` file records their resolved versions for `uv`. Jacobi is a separate C++ dependency; see the [C++ setup guide](csolver/README.md#requirements-and-build) for instructions to build it and place its files in this project.

## Quick start

The Python solvers return NumPy arrays. Scalar IVP methods return `(x, y)`. State-vector methods return `(t, solution)`, with one state variable per row of `solution`. BVP methods return `(x, y)`.

```python
import numpy as np
from solver import bvp, ivp

# y' = y, y(0) = 1
x, y = ivp.rk4(0.0, 1.0, 0.01, func=lambda x, y: y, initial=1.0)

# x' = v, v' = -x, with x(0) = 0 and v(0) = 1
def oscillator(t, state):
    position, velocity = state
    return np.array([velocity, -position])

t, state = ivp.state_rk4(0.0, 10.0, 0.01, oscillator, np.array([0.0, 1.0]))

# y'' - 4y = 4x, y(0) = 0, y(1) = 2
x_bvp, y_bvp = bvp.fdm(
    0.0, 1.0, 0.01,
    p=lambda x: np.zeros_like(x),
    q=lambda x: -4 * np.ones_like(x),
    r=lambda x: 4 * x,
    initial=0.0,
    end=2.0,
)
```

For scalar second-order IVPs in the form $y''+P(x,y)y'=Q(x,y)$, pass `p`, `q`, `initial`, and `initial_slope` to a scalar IVP method and omit `func`.

## C++ setup

The C++ library requires CMake 3.20 or newer, Ninja, a C++20 compiler, and Jacobi. First follow the [Jacobi setup steps](csolver/README.md#requirements-and-build) to build Jacobi and place its headers and library under `csolver/dependencies/jacobi/`. Then configure and build from the repository root:

```bash
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

The project builds the `ODE` static library, the `Benchmark` executable, and the `HalvorsenAttractor` executable. These commands also work in Windows PowerShell. Ninja is the generator used for the project build. See [`csolver/README.md`](csolver/README.md) for platform-specific Jacobi setup and the C++ API.

## Project guides

- [`solver/`](solver/README.md): Python solver APIs and numerical methods.
- [`csolver/`](csolver/README.md): C++ solver API and build details.
- [`analysis/`](analysis/README.md): Notebook guide and learning path.
- [`animation_scripts/`](animation_scripts/README.md): Animation gallery and run instructions.
- [`benchmark/`](benchmark/README.md): Benchmark programs, outputs, and usage.

## Project tree

```text
.
├── analysis/                 # Mathematical notebooks
├── animation_scripts/        # Python and C++ animation examples and media
├── benchmark/                # Python and C++ benchmark programs and results
├── csolver/                  # C++ solver library and Jacobi integration
├── solver/                   # Python solver package
├── CMakeLists.txt            # Root CMake build
├── LICENSE
├── pyproject.toml             # Python package metadata and dependencies
├── requirements.txt
└── uv.lock                    # Resolved Python dependencies
```

## Scope

All solvers use fixed steps and do not provide adaptive error control, event detection, stiffness handling, or dense output. The BVP implementation handles scalar linear second-order equations. These implementations emphasize transparent numerical updates over input validation and production features.

## Usage of AI

- All modules have code written entirely by me.
- AI was used for better understanding of the concepts.
- Draft for READMEs were generated by AI and were modified by me, for better explanation.

## License

This project is distributed under the [MIT License](LICENSE).
