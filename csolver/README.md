# C++ solver

`csolver` is the C++ implementation of the project's fixed-step ODE methods. It provides state-vector IVP methods and a finite-difference BVP method. The API uses the [Jacobi](https://github.com/OjasRane/Jacobi) vector and matrix types.

## Contents

| Path | Purpose |
| --- | --- |
| [`include/ode/ivp.h`](include/ode/ivp.h) | State-vector Euler, midpoint, Heun, and RK4 declarations |
| [`include/ode/bvp.h`](include/ode/bvp.h) | Finite-difference BVP declaration |
| [`src/ivp.cpp`](src/ivp.cpp) | State-vector IVP implementations |
| [`src/bvp.cpp`](src/bvp.cpp) | Tridiagonal finite-difference BVP implementation |
| [`decoder.py`](decoder.py) | Reader for the `.jcbi` binary format written by Jacobi |

## Requirements and build

The build requires CMake 3.20 or newer, Ninja, a C++20 compiler, and Jacobi. Jacobi is a separate library that must be built and placed under `csolver/dependencies/jacobi/` before configuring this project. CMake selects the platform's usual static-library suffix (`.a` on Linux and macOS, `.lib` on Windows).

### Build Jacobi

Run these commands from the project root. They create a temporary `temp/` directory, clone and build Jacobi there with Ninja, then copy its headers and static library into `csolver/dependencies/jacobi/`. The library filename must be `libJacobi.a` on Linux/macOS or `Jacobi.lib` on Windows.

#### Linux and macOS

```bash
mkdir -p temp
git clone https://github.com/OjasRane/Jacobi.git temp/Jacobi
cmake -S temp/Jacobi -B temp/Jacobi/build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build temp/Jacobi/build
mkdir -p csolver/dependencies/jacobi/include csolver/dependencies/jacobi/lib
cp -r temp/Jacobi/include/. csolver/dependencies/jacobi/include/
cp temp/Jacobi/build/libJacobi.a csolver/dependencies/jacobi/lib/
rm -rf temp
```

If Jacobi's build produces the library under a configuration-specific directory, copy the resulting `libJacobi.a` from that directory into `csolver/dependencies/jacobi/lib/`.

#### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force -Path temp
git clone https://github.com/OjasRane/Jacobi.git temp/Jacobi
cmake -S temp/Jacobi -B temp/Jacobi/build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build temp/Jacobi/build
New-Item -ItemType Directory -Force -Path csolver/dependencies/jacobi/include, csolver/dependencies/jacobi/lib
Copy-Item temp/Jacobi/include/* csolver/dependencies/jacobi/include/ -Recurse
Copy-Item temp/Jacobi/build/libJacobi.lib csolver/dependencies/jacobi/lib/Jacobi.lib
Remove-Item -Recurse -Force temp
```

If the generated library has a different filename or is in a configuration-specific directory, copy it to `csolver/dependencies/jacobi/lib/Jacobi.lib`.

### Build this project

From the project root, configure and build with Ninja:

```bash
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

These commands also work in PowerShell. The build creates the `ODE` static library, the `Benchmark` executable, and the `HalvorsenAttractor` executable. Ninja is the required generator in the documented build steps. Jacobi is not fetched or built automatically by this project's CMake configuration.

## IVP API

The four methods accept the start and end times, fixed step size, a derivative callback, and an initial state:

```cpp
auto solution = csolver::rk4(a, b, h, derivative, initial_state);
```

The callback has type `jacobi::Vector<double>(double, const jacobi::Vector<double>&)`. For example, a harmonic oscillator can be represented as:

```cpp
static jacobi::Vector<double> oscillator(
    double /* t */, const jacobi::Vector<double>& state
) {
    return {state[1], -state[0]};
}

jacobi::Vector<double> initial{0.0, 1.0};
auto result = csolver::rk4(0.0, 10.0, 0.01, oscillator, initial);
```

The return value is an `IVPSolution<double>` with public `time` and `solution` members. The C++ solution matrix stores one time sample per row and one state variable per column. This layout differs from Python's `solver.ivp.state_*` layout, which stores state variables by row.

## BVP API

`csolver::fdm` solves $y''+P(x)y'+Q(x)y=R(x)$ with specified endpoint values. The callbacks each accept one `double` and return one `double`:

```cpp
auto result = csolver::fdm(
    0.0, 1.0, 0.01,  // a, b, h
    0.0, 2.0,        // y(a), y(b)
    p, q, r
);
```

It returns a `BVPSolution<double>` with public `x` and `y` members. The current implementation returns interior grid coordinates and values; endpoints are used in the solve but are not included in these returned vectors.

## Limitations

These methods use fixed steps and real-valued `double` data. They do not implement adaptive step control, event detection, or stiffness handling. Inputs are not generally validated; the BVP solver requires at least three intervals and a nonsingular tridiagonal system.

## Related guides

- [Python solver API](../solver/README.md)
- [Benchmark programs](../benchmark/README.md)
- [C++ Halvorsen-attractor example](../animation_scripts/csolved/halvorsen_attractor/halvorsen_attractor.cpp)

## Project tree

```text
csolver/
├── dependencies/jacobi/       # Jacobi headers and built library (set up separately)
├── include/ode/
│   ├── bvp.h                  # BVP API
│   └── ivp.h                  # IVP API
├── src/
│   ├── bvp.cpp                # BVP implementation
│   └── ivp.cpp                # IVP implementations
├── CMakeLists.txt             # C++ library build definition
├── README.md                  # C++ solver and build guide
├── __init__.py                # Python package initializer
└── decoder.py                 # Jacobi .jcbi file reader
```

## License

This library is part of the project distributed under the [MIT License](../LICENSE).
