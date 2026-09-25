# Solver package

The `solver` package is the numerical core of the [Ordinary Differential Equations project](../README.md). It implements fixed-step methods directly with NumPy so that the update rules remain visible and easy to study.

## Contents

| Module | Purpose |
| --- | --- |
| [`ivp.py`](ivp.py) | Scalar and state-vector solvers for initial value problems |
| [`bvp.py`](bvp.py) | Finite-difference solver for scalar, linear second-order boundary value problems |
| [`__init__.py`](__init__.py) | Marks this directory as the importable `solver` package |

Install the project from its root directory before using the package. See the main [installation guide](../README.md#installation) for `uv` and `pip` instructions.

```python
from solver import bvp, ivp
```

There is no command-line interface. The modules expose regular Python functions that return NumPy arrays.

## Numerical methods

The IVP module provides a scalar implementation and a state-vector implementation of each integration method:

| Method | Scalar first-/second-order function | State-vector function | Expected global order |
| --- | --- | --- | ---: |
| Euler | `ivp.euler_method` | `ivp.state_euler_method` | $O(h)$ |
| Explicit midpoint | `ivp.midpoint_method` | `ivp.state_midpoint_method` | $O(h^2)$ |
| Heun / improved Euler | `ivp.heun_method` | `ivp.state_heun_method` | $O(h^2)$ |
| Classical RK4 | `ivp.rk4` | `ivp.state_rk4` | $O(h^4)$ |

The BVP module provides `bvp.fdm`, a second-order central finite-difference method whose resulting tridiagonal system is solved with the Thomas algorithm in $O(N)$ time.

## Scalar initial value problems

The original IVP interface supports scalar first-order equations

$$
y'=f(x,y), \qquad y(a)=y_0,
$$

and scalar second-order equations

$$
y''+P(x,y)y'=Q(x,y), \qquad y(a)=y_0, \quad y'(a)=v_0.
$$

All four scalar functions share the signature

```python
method(a, b, h, **kwargs)
```

and return `(x, y)`, where both arrays have shape `(N + 1,)`.

### Common parameters

| Argument | Meaning |
| --- | --- |
| `a` | Start of the integration interval |
| `b` | Requested end of the integration interval |
| `h` | Fixed step size |
| `initial` | Initial value $y(a)$ |

### First-order equations

Pass `func` to select first-order mode. It must accept `(x, y)` and return $f(x,y)$.

```python
import numpy as np

from solver import ivp

# y' = y, y(0) = 1
x, y = ivp.rk4(
    a=0.0,
    b=1.0,
    h=0.01,
    func=lambda x, y: y,
    initial=1.0,
)

assert np.isclose(y[-1], np.e, atol=1e-8)
```

### Second-order equations

Omit `func` to select second-order mode and provide:

| Keyword | Expected value |
| --- | --- |
| `p` | Callable `p(x, y)` evaluating $P(x,y)$ |
| `q` | Callable `q(x, y)` evaluating $Q(x,y)$ |
| `initial_slope` | Initial derivative $y'(a)$ |

```python
from solver import ivp

# y'' = -y, y(0) = 0, y'(0) = 1
x, y = ivp.rk4(
    a=0.0,
    b=10.0,
    h=0.01,
    p=lambda x, y: 0.0,
    q=lambda x, y: -y,
    initial=0.0,
    initial_slope=1.0,
)
```

The derivative is evolved internally but is not returned. For second-order equations, `euler_method` updates `y` using the newly computed slope; the higher-order methods evolve $y$ and $y'$ together through their respective stage calculations.

## State-vector initial value problems

The state-vector interface solves systems in the general form

$$
\frac{d\vec{r}}{dt}=\langle f_1(t,\vec{r}), f_2(t,\vec{r}), \ldots, f_n(t,\vec{r})\rangle, \qquad \vec{r}(a)=\vec{r}_0.
$$

It supports coupled systems directly and supports higher-order ODEs after they are rewritten as first-order systems. For example, a second-order equation

$$
y''=f(t,y,y')
$$

can be represented using $\vec{r}=\langle y,v\rangle$, where $v=y'$, so that

$$
\frac{d\vec{r}}{dt}=\langle v,f(t,y,v)\rangle.
$$

All four state-vector functions share the signature

```python
method(a, b, h, func, initial_state)
```

| Argument | Expected value |
| --- | --- |
| `a`, `b` | Start and requested end of the integration interval |
| `h` | Fixed step size |
| `func` | Callable `func(t, state)` returning a one-dimensional derivative array |
| `initial_state` | One-dimensional NumPy array containing $\vec{r}_0$ |

They return `(t, solution)`:

- `t` has shape `(N + 1,)`.
- `solution` has shape `(number_of_states, N + 1)`.
- `solution[i]` contains the complete trajectory of state component `i`.

### Coupled-system example

Solve

$$
x'=\frac{y}{8}, \qquad y'=\frac{x}{2}, \qquad x(0)=1, \quad y(0)=0.
$$

```python
import numpy as np

from solver import ivp

def coupled_system(t, state):
    x, y = state
    return np.array([y / 8, x / 2])

t, solution = ivp.state_rk4(
    0.0,
    4.0,
    0.01,
    coupled_system,
    np.array([1.0, 0.0]),
)

x = solution[0]
y = solution[1]
```

The same interface powers the project's nonlinear [`double_pendulum.py`](../animation_scripts/double_pendulum.py) and [`lorenz_attractor.py`](../animation_scripts/lorenz_attractor.py) demonstrations.

The state-vector derivation, coupled examples, higher-order reduction, and Lorenz system are in [`solving_ivp_problems.ipynb`](../analysis/solving_ivp_problems.ipynb).

## Boundary value problems

`bvp.fdm` solves scalar, linear second-order equations of the form

$$
y''+P(x)y'+Q(x)y=R(x), \qquad y(a)=y_a, \quad y(b)=y_b.
$$

Its usage is:

```python
bvp.fdm(a, b, h, p=p, q=q, r=r, initial=initial, end=end)
```

Centered finite differences produce a tridiagonal system for the $N-1$ interior values. The implementation stores only its three diagonals and solves them with the Thomas algorithm rather than allocating and eliminating a full dense matrix.

| Argument | Meaning |
| --- | --- |
| `a`, `b` | Boundary coordinates |
| `h` | Fixed grid spacing |
| `p` | Vectorized callable evaluating $P(x)$ |
| `q` | Vectorized callable evaluating $Q(x)$ |
| `r` | Vectorized callable evaluating $R(x)$ |
| `initial` | Left boundary value $y(a)$ |
| `end` | Right boundary value $y(b)$ |

The coefficient functions receive the complete NumPy array of interior points and should return arrays of the same shape. Use `np.zeros_like(x)` or `np.full_like(x, value)` for constant coefficients.

```python
import numpy as np

from solver import bvp

# y'' - 4y = 4x, y(0) = 0, y(1) = 2
x, y = bvp.fdm(
    a=0.0,
    b=1.0,
    h=0.01,
    p=lambda x: np.zeros_like(x),
    q=lambda x: np.full_like(x, -4.0),
    r=lambda x: 4.0 * x,
    initial=0.0,
    end=2.0,
)
```

See [`solving_bvp_problems_using_fdm.ipynb`](../analysis/solving_bvp_problems_using_fdm.ipynb) for the complete finite-difference derivation and a comparison with the analytical solution.

## Choosing an interface

| Problem | Recommended interface |
| --- | --- |
| Scalar first-order IVP | `euler_method`, `midpoint_method`, `heun_method`, or `rk4` with `func` |
| Scalar second-order IVP in the supported $P$/$Q$ form | The same scalar methods with `p`, `q`, and `initial_slope` |
| Coupled system or higher-order IVP | `state_euler_method`, `state_midpoint_method`, `state_heun_method`, or `state_rk4` |
| Scalar linear second-order BVP | `bvp.fdm` |

## Current limitations

- All methods use fixed steps and real-valued `float64` arrays.
- There is no adaptive error control, stiffness handling, event detection, or dense output.
- Inputs are not validated for missing callables, incompatible state shapes, interval direction, or invalid step sizes.
- State-vector IVP functions require a one-dimensional NumPy `initial_state`; they do not currently support complex-valued states.
- The BVP solver is limited to scalar, linear second-order equations and assumes a nonsingular tridiagonal system. It does not pivot around zero or ill-conditioned diagonal entries.

These implementations are intended for learning and experimentation. For production numerical work, use a mature library with input validation, adaptive methods, and documented stability guarantees.

## Related material

- [`solving_ivp_problems.ipynb`](../analysis/solving_ivp_problems.ipynb) derives the scalar and state-vector IVP methods and compares their errors.
- [`solving_bvp_problems_using_fdm.ipynb`](../analysis/solving_bvp_problems_using_fdm.ipynb) derives the finite-difference system and Thomas-algorithm solution.
- [`population_models.ipynb`](../analysis/population_models.ipynb) applies RK4 to exponential, logistic, and Allee-effect models.
- [`erf_function_using_ode.ipynb`](../analysis/erf_function_using_ode.ipynb) computes the error function as an IVP.
- [`animation_scripts/`](../animation_scripts/) contains physical and chaotic-system demonstrations built on the solvers.

## License

This package is part of the project distributed under the [MIT License](../LICENSE).
