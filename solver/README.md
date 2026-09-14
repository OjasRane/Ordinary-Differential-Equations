# Solver package

The `solver` package contains the numerical core of the [Ordinary Differential Equations project](../README.md). Its implementations are intentionally compact and written directly with NumPy so the update rules behind each method remain easy to study.

## Contents

| Module | Purpose |
| --- | --- |
| [`ivp.py`](ivp.py) | Fixed-step solvers for first- and second-order initial value problems |
| [`bvp.py`](bvp.py) | Finite-difference solver for linear second-order boundary value problems |
| [`__init__.py`](__init__.py) | Marks this directory as the importable `solver` package |

Install the project from its root directory before using the package. See the main [installation guide](../README.md#installation) for `uv` and `pip` instructions.

## Importing the modules

```python
from solver import bvp, ivp
```

There is no command-line interface. Each solver is a Python function that returns two one-dimensional NumPy arrays:

```python
x, y = solver(...)
```

## Initial value problems

The IVP module supports scalar first-order equations

$$
y' = f(x,y), \qquad y(a)=y_0,
$$

and scalar second-order equations

$$
y'' + P(x,y)y' = Q(x,y), \qquad y(a)=y_0, \quad y'(a)=v_0.
$$

All four functions have the same call signature:

```python
method(a, b, h, **kwargs)
```

| Function | Method | Expected global order |
| --- | --- | ---: |
| `ivp.euler_method` | Euler | $O(h)$ |
| `ivp.midpoint_method` | Explicit midpoint | $O(h^2)$ |
| `ivp.heun_method` | Heun / improved Euler | $O(h^2)$ |
| `ivp.rk4` | Classical fourth-order Runge–Kutta | $O(h^4)$ |

### Common parameters

| Argument | Meaning |
| --- | --- |
| `a` | Start of the integration interval |
| `b` | Requested end of the integration interval |
| `h` | Fixed step size |
| `initial` | Initial value $y(a)$ |

### First-order arguments

Pass `func` to select first-order mode:

| Keyword | Expected value |
| --- | --- |
| `func` | Callable with signature `func(x, y)` that evaluates $f(x,y)$ |

For example, solve $y'=y$ with $y(0)=1$:

```python
import numpy as np

from solver import ivp

x, y = ivp.rk4(
    a=0.0,
    b=1.0,
    h=0.01,
    func=lambda x, y: y,
    initial=1.0,
)

assert np.isclose(y[-1], np.e, atol=1e-8)
```

### Second-order arguments

Omit `func` and provide all three second-order keywords:

| Keyword | Expected value |
| --- | --- |
| `p` | Callable `p(x, y)` that evaluates $P(x,y)$ |
| `q` | Callable `q(x, y)` that evaluates $Q(x,y)$ |
| `initial_slope` | Initial derivative $y'(a)$ |

For example, solve the harmonic oscillator $y''=-y$, $y(0)=0$, $y'(0)=1$:

```python
from solver import ivp

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

The derivative is evolved internally but is not included in the return value. For second-order problems, the Euler implementation updates `y` using the newly computed slope; the higher-order methods evolve `y` and $y'$ together using their respective stage calculations.

## Boundary value problems

`bvp.fdm` solves scalar, linear second-order equations of the form

$$
y'' + P(x)y' + Q(x)y = R(x), \qquad y(a)=y_a, \quad y(b)=y_b.
$$

Its signature is:

```python
bvp.fdm(a, b, h, *, p, q, r, initial, end)
```

The implementation replaces the derivatives with centered finite differences. This produces a tridiagonal system for the $N-1$ interior values, which is solved in $O(N)$ time with the Thomas algorithm.

SciPy's sparse solvers were deliberately avoided here — exploiting the tridiagonal structure by hand, rather than eliminating full rows, was the actual point of this part of the project.

| Argument | Meaning |
| --- | --- |
| `a`, `b` | Boundary coordinates |
| `h` | Fixed grid spacing |
| `p` | Vectorized callable evaluating $P(x)$ |
| `q` | Vectorized callable evaluating $Q(x)$ |
| `r` | Vectorized callable evaluating $R(x)$ |
| `initial` | Left boundary value $y(a)$ |
| `end` | Right boundary value $y(b)$ |

The coefficient functions receive the complete NumPy array of interior grid points. They should return arrays of the same shape; use `np.zeros_like(x)` or `np.full_like(x, value)` for constant coefficients.

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

See [`solving_bvp_problems_using_fdm.ipynb`](../analysis/solving_bvp_problems_using_fdm.ipynb) for the full finite-difference derivation and a comparison with the analytical solution.

## Current limitations

- Scalar, real-valued state variables only; solution arrays use `float64`.
- Fixed-step integration only—there is no local-error estimate or adaptive step sizing.
- No validation is performed for missing callables, initial values, interval direction, or step size.
- No dedicated support for stiff equations, events, dense output, systems of ODEs, or complex-valued states.
- The BVP solver assumes a nonsingular tridiagonal system and does not pivot around zero or ill-conditioned diagonal entries.

These solvers are designed for learning and experimentation. For production numerical work, use a mature library with input validation, adaptive methods, and documented stability guarantees.

## Related notebooks

- [`solving_ivp_problems.ipynb`](../analysis/solving_ivp_problems.ipynb) derives all four IVP methods and compares their errors.
- [`solving_bvp_problems_using_fdm.ipynb`](../analysis/solving_bvp_problems_using_fdm.ipynb) derives the finite-difference system and Thomas-algorithm solution.
- [`population_models.ipynb`](../analysis/population_models.ipynb) applies RK4 to exponential, logistic, and Allee-effect models.
- [`erf_function_using_ode.ipynb`](../analysis/erf_function_using_ode.ipynb) computes the error function as an IVP.

## License

This package is part of the project distributed under the [MIT License](../LICENSE).
