# Python solver

The `solver` package implements the Python numerical methods in this project using NumPy. Its update steps are written directly so they can be followed alongside the derivations in the [analysis notebooks](../analysis/README.md).

## Modules

| Module | Purpose |
| --- | --- |
| [`ivp.py`](ivp.py) | Scalar and state-vector initial value problem methods |
| [`bvp.py`](bvp.py) | Finite-difference solver for scalar linear second-order boundary value problems |

Install the project from its root as described in the [setup guide](../README.md#python-setup). Import the modules with:

```python
from solver import bvp, ivp
```

## IVP methods

The scalar methods solve first-order equations

$$
y'=f(x,y), \qquad y(a)=y_0,
$$

or second-order equations in the supported form

$$
y''+P(x,y)y'=Q(x,y), \qquad y(a)=y_0, \quad y'(a)=v_0.
$$

All scalar methods share the signature `method(a, b, h, **kwargs)` and return `(x, y)`, where both arrays have `N + 1` values. Pass `func` for a first-order equation. For a second-order equation, omit `func` and pass `p`, `q`, `initial`, and `initial_slope`.

| Method | Function | Expected global order |
| --- | --- | ---: |
| Euler | `ivp.euler_method` | $O(h)$ |
| Explicit midpoint | `ivp.midpoint_method` | $O(h^2)$ |
| Heun | `ivp.heun_method` | $O(h^2)$ |
| Classical RK4 | `ivp.rk4` | $O(h^4)$ |

For example, RK4 can solve $y'=y$, $y(0)=1$ as follows:

```python
from solver import ivp

x, y = ivp.rk4(
    a=0.0,
    b=1.0,
    h=0.01,
    func=lambda x, y: y,
    initial=1.0,
)
```

## State-vector IVP methods

State-vector methods solve systems of the form

$$
\vec{r}'(t)=\vec{f}(t,\vec{r}), \qquad \vec{r}(a)=\vec{r}_0.
$$

They handle coupled systems and higher-order equations after those equations are rewritten as first-order systems. Each method accepts `(a, b, h, func, initial_state)`. The callback receives `(t, state)` and must return one derivative per state value. The initial state must be a one-dimensional NumPy array.

```python
import numpy as np
from solver import ivp

def oscillator(t, state):
    position, velocity = state
    return np.array([velocity, -position])

t, solution = ivp.state_rk4(
    0.0, 10.0, 0.01, oscillator, np.array([0.0, 1.0])
)
position = solution[0]
velocity = solution[1]
```

The returned time array has shape `(N + 1,)`; `solution` has shape `(number_of_states, N + 1)`, with each state variable in a row. The available functions are `state_euler_method`, `state_midpoint_method`, `state_heun_method`, and `state_rk4`.

## BVP method

`bvp.fdm` solves linear second-order equations

$$
y''+P(x)y'+Q(x)y=R(x), \qquad y(a)=y_a, \quad y(b)=y_b.
$$

It uses centered finite differences to form a tridiagonal system and the Thomas algorithm to solve for the interior values in $O(N)$ time. The function returns `(x, y)`, including both boundary points. The coefficient callbacks accept the array of interior grid points and should return broadcast-compatible NumPy arrays.

```python
import numpy as np
from solver import bvp

x, y = bvp.fdm(
    0.0, 1.0, 0.01,
    p=lambda x: np.zeros_like(x),
    q=lambda x: -4 * np.ones_like(x),
    r=lambda x: 4 * x,
    initial=0.0,
    end=2.0,
)
```

## Grid and limitations

The methods use `N = int((b - a) / h)` steps and form the grid as `a + h * arange(N + 1)`. Use a positive step size that divides the interval if the final grid point must equal `b`. The methods use real-valued `float64` arrays and fixed steps. They do not provide adaptive error control, event detection, stiffness handling, or dense output. Inputs are not comprehensively validated. The BVP solver assumes a nonsingular tridiagonal system.

## Related guides

- [C++ solver](../csolver/README.md)
- [Analysis notebooks](../analysis/README.md)
- [Animation examples](../animation_scripts/README.md)

## Project tree

```text
solver/
├── README.md       # Python solver guide
├── __init__.py     # Package initializer
├── bvp.py          # Finite-difference BVP solver
└── ivp.py          # Scalar and state-vector IVP methods
```

## License

This package is part of the project distributed under the [MIT License](../LICENSE).
