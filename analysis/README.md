# Analysis notebooks

This directory contains the mathematical explanations and worked examples for the numerical methods implemented in the project's [`solver`](../solver/) package. The notebooks combine derivations, executable Python, analytical reference solutions, and Matplotlib visualizations.

## Notebook guide

| Notebook | Main topics | Solver used |
| --- | --- | --- |
| [`solving_ivp_problems.ipynb`](solving_ivp_problems.ipynb) | Euler, midpoint, Heun, RK4, and first- and second-order IVPs | `solver.ivp` |
| [`solving_bvp_problems_using_fdm.ipynb`](solving_bvp_problems_using_fdm.ipynb) | Central finite differences and the Thomas tridiagonal algorithm | `solver.bvp` |
| [`population_models.ipynb`](population_models.ipynb) | Exponential growth, logistic growth, carrying capacity, and the Allee effect | `solver.ivp.rk4` |
| [`erf_function_using_ode.ipynb`](erf_function_using_ode.ipynb) | Computing the error function as an initial value problem | `solver.ivp.rk4` |

## Recommended learning path

1. Start with [`solving_ivp_problems.ipynb`](solving_ivp_problems.ipynb) to understand the fixed-step integration methods.
2. Continue with [`solving_bvp_problems_using_fdm.ipynb`](solving_bvp_problems_using_fdm.ipynb) to see how a differential equation becomes a tridiagonal linear system.
3. Explore [`population_models.ipynb`](population_models.ipynb) for a real-world nonlinear modelling application.
4. Finish with [`erf_function_using_ode.ipynb`](erf_function_using_ode.ipynb) for an example involving a special function without an elementary antiderivative.

The application notebooks can also be read independently after becoming familiar with basic first-order IVPs.

## Running the notebooks

Install the project and its dependencies by following the root [installation guide](../README.md#installation). To open JupyterLab directly in this directory, use one of the following workflows.

### Using `uv` (recommended)

#### Linux and macOS

```bash
git clone https://github.com/OjasRane/Ordinary-Differential-Equations.git
cd Ordinary-Differential-Equations
uv sync --locked
uv run jupyter lab analysis
```

#### Windows (PowerShell)

```powershell
git clone https://github.com/OjasRane/Ordinary-Differential-Equations.git
Set-Location Ordinary-Differential-Equations
uv sync --locked
uv run jupyter lab analysis
```

Open a notebook in JupyterLab and run its cells from top to bottom. The project is installed into the environment by `uv sync`, allowing notebook cells to import the local solver modules:

```python
from solver import bvp, ivp
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
python -m jupyter lab analysis
```

#### Windows (PowerShell)

```powershell
git clone https://github.com/OjasRane/Ordinary-Differential-Equations.git
Set-Location Ordinary-Differential-Equations
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
python -m jupyter lab analysis
```

Python 3.12 or newer is required.

## Notebook details

### Solving IVPs

[`solving_ivp_problems.ipynb`](solving_ivp_problems.ipynb) introduces ordinary differential equations and explains why numerical solutions are needed when a convenient analytical solution is unavailable. It derives four fixed-step methods for equations of the form

$$
y'=f(x,y), \qquad y(a)=y_0.
$$

The methods are presented in increasing order of accuracy:

| Method | Expected global error |
| --- | ---: |
| Euler | $O(h)$ |
| Midpoint | $O(h^2)$ |
| Heun | $O(h^2)$ |
| RK4 | $O(h^4)$ |

The first worked example solves

$$
y'=\cos(x), \qquad y(0)=0,
$$

and compares every numerical result with the analytical solution $y=\sin(x)$. A second example applies all four methods to

$$
y''-3y'=x-2y, \qquad y(0)=0, \quad y'(0)=0.
$$

Each plot reports the mean absolute difference between the numerical and analytical values.

### Solving BVPs with finite differences

[`solving_bvp_problems_using_fdm.ipynb`](solving_bvp_problems_using_fdm.ipynb) considers linear boundary value problems in the form

$$
y''+P(x)y'+Q(x)y=R(x), \qquad y(a)=y_0, \quad y(b)=y_N.
$$

It derives centered finite-difference approximations for $y'$ and $y''$, substitutes them into the differential equation, and shows why the resulting $N-1$ equations form a tridiagonal system. The implementation solves that system with the Thomas algorithm without allocating a full dense matrix.

The worked example solves

$$
y''-4y=4x, \qquad y(0)=0, \quad y(1)=2,
$$

then plots the finite-difference and analytical solutions together and reports their mean absolute difference.

### Population models

[`population_models.ipynb`](population_models.ipynb) develops increasingly realistic first-order models for the population $P(t)$ of a species:

1. Exponential growth assumes unlimited resources:

   $$
   \frac{dP}{dt}=rP.
   $$

2. Logistic growth introduces the carrying capacity $K$:

   $$
   \frac{dP}{dt}=rP\left(1-\frac{P}{K}\right).
   $$

3. The Allee-effect model adds a threshold population $T$:

   $$
   \frac{dP}{dt}=-rP\left(1-\frac{P}{K}\right)\left(1-\frac{P}{T}\right).
   $$

The notebook compares the exponential and logistic models, examines initial populations below, at, and above the carrying capacity, and demonstrates how populations above and below the Allee threshold behave differently.

A rendered animation based on the same model is available as [`population_modelling.gif`](../animation_scripts/animations/population_modelling.gif).

### Error function as an ODE

[`erf_function_using_ode.ipynb`](erf_function_using_ode.ipynb) starts from

$$
\operatorname{erf}(x)=\int_0^x \frac{2}{\sqrt{\pi}}e^{-t^2}\,dt
$$

and rewrites it as the IVP

$$
y'=\frac{2}{\sqrt{\pi}}e^{-x^2}, \qquad y(0)=0.
$$

RK4 computes the solution for nonnegative $x$. The notebook then uses the odd symmetry $\operatorname{erf}(-x)=-\operatorname{erf}(x)$ to plot the function over $[-32,32]$.

A rendered version of this visualization is available as [`erf.gif`](../animation_scripts/animations/erf.gif).

## Dependencies

| Package | Role in the notebooks |
| --- | --- |
| NumPy | Array operations, mathematical functions, and error calculations |
| Matplotlib | Static plots and visual comparisons |
| JupyterLab | Interactive notebook environment |
| IPython | Rich mathematical display used by the population notebook |

IPython is installed transitively with JupyterLab. Exact dependency constraints are declared in [`pyproject.toml`](../pyproject.toml), and resolved versions are recorded in [`uv.lock`](../uv.lock).

## Reproducibility notes

- Model constants, initial conditions, time intervals, and step sizes are defined directly in each notebook.
- The notebooks use the project's own fixed-step solvers rather than SciPy integration routines.
- Execute cells in order because later cells may reuse variables and results created by earlier cells.
- Decreasing the step size generally improves numerical accuracy but increases the number of solver iterations.

These notebooks are educational demonstrations rather than benchmarks or production modelling tools. See the [`solver` documentation](../solver/README.md#current-limitations) for the numerical implementation's current scope.

## License

The notebooks are part of the project distributed under the [MIT License](../LICENSE).
