# Analysis notebooks

The notebooks in this directory explain the project's numerical methods and apply them to example problems. They combine mathematical derivations, executable Python, analytical comparisons, and plots using the [Python solver package](../solver/README.md).

## Notebook guide

| Notebook | Topics |
| --- | --- |
| [`solving_ivp_problems.ipynb`](solving_ivp_problems.ipynb) | Vector fields; scalar and state-vector IVPs; Euler, midpoint, Heun, and RK4; coupled systems; Lorenz trajectories |
| [`solving_bvp_problems_using_fdm.ipynb`](solving_bvp_problems_using_fdm.ipynb) | Central finite differences, the tridiagonal system, and the Thomas algorithm |
| [`population_models.ipynb`](population_models.ipynb) | Exponential and logistic growth, carrying capacity, and the Allee effect |
| [`erf_function_using_ode.ipynb`](erf_function_using_ode.ipynb) | Computing the error function as an initial value problem |

## Suggested order

Start with `solving_ivp_problems.ipynb` for the numerical methods and state-vector formulation. Continue with `solving_bvp_problems_using_fdm.ipynb` for the finite-difference method, then explore the population and error-function examples. The last two notebooks can also be read independently after the basic IVP methods.

## Run the notebooks

Install the project from its root by following the [Python setup guide](../README.md#python-setup), then start JupyterLab:

```bash
uv run jupyter lab analysis
```

With an activated pip environment, use:

```bash
python -m jupyter lab analysis
```

Open a notebook and run its cells from top to bottom. Later cells may reuse values created earlier. Python 3.12 or newer is required; NumPy, Matplotlib, and JupyterLab are project dependencies.

## Learning notes

The IVP notebook compares numerical solutions with known solutions for selected equations and discusses global error orders. Its state-vector examples show how coupled and higher-order equations can use the same integration methods. The BVP notebook derives the centered-difference equations and compares the computed result with an analytical solution. The application notebooks use RK4 to evaluate population models and the integral defining the error function.

These notebooks are educational examples, not performance benchmarks or production modelling workflows. See the [solver guide](../solver/README.md#grid-and-limitations) for implementation limits.

## Related guides

- [Python solver](../solver/README.md)
- [Animations](../animation_scripts/README.md)
- [Benchmarks](../benchmark/README.md)

## Project tree

```text
analysis/
├── README.md                           # Notebook guide
├── erf_function_using_ode.ipynb         # Error function as an IVP
├── population_models.ipynb              # Exponential, logistic, and Allee models
├── solving_bvp_problems_using_fdm.ipynb # Finite-difference BVP method
└── solving_ivp_problems.ipynb           # IVP methods and state-vector systems
```

## License

The notebooks are part of the project distributed under the [MIT License](../LICENSE).
