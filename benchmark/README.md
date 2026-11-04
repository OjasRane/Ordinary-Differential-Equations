# Benchmarks

This directory contains small programs that measure the Python and C++ solver implementations on the same kinds of IVP and BVP problems. They are intended for comparison and experimentation; the recorded times depend on the machine, compiler, build type, and software versions.

## Contents

| Path | Purpose |
| --- | --- |
| [`pysolver/benchmark.py`](pysolver/benchmark.py) | Times Python state-vector IVP methods and the Python BVP solver |
| [`pysolver/PySolver_Benchmark.csv`](pysolver/PySolver_Benchmark.csv) | Checked-in Python benchmark results |
| [`csolver/benchmark.cpp`](csolver/benchmark.cpp) | Times the C++ IVP methods and C++ BVP solver |
| [`csolver/timer.h`](csolver/timer.h) | Small scope-based timer used by the C++ benchmark |
| [`csolver/CSolver_Benchmark.csv`](csolver/CSolver_Benchmark.csv) | Checked-in C++ benchmark results |

Both programs run warm-up iterations, then record measured runs for Lorenz and Halvorsen attractor IVPs and a Poisson-equation BVP. The programs write CSV output to their current working directory. The Python benchmark uses milliseconds from `perf_counter_ns`; the C++ timer records milliseconds.

## Run the Python benchmark

Install the Python project as described in the [root guide](../README.md#python-setup), then run from the repository root:

```bash
uv run python benchmark/pysolver/benchmark.py
```

This writes `PySolver_Benchmark.csv` to the current directory and replaces a file with that name if present. Run from `benchmark/pysolver/` to write the output beside the checked-in CSV:

```bash
cd benchmark/pysolver
uv run python benchmark.py
```

## Run the C++ benchmark

First set up Jacobi and the C++ build environment as described in the [C++ solver guide](../csolver/README.md#requirements-and-build). Configure and build from the repository root:

```bash
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

Run the generated `Benchmark` executable with `benchmark/csolver` as its working directory to write the CSV beside the checked-in result. For the documented Ninja build on Linux or macOS:

```bash
cd benchmark/csolver
../../build/benchmark/csolver/Benchmark
```

On Windows, run `..\..\build\benchmark\csolver\Benchmark.exe` from `benchmark/csolver/`.

## Reading the results

The CSV files contain one row per problem and method and one column per measured run. Compare runs on the same machine and with the same compiler settings. These programs do not report error or enforce equal accuracy between methods, so elapsed time alone is not a measure of solver quality.

## Project tree

```text
benchmark/
├── csolver/
│   ├── CMakeLists.txt            # C++ benchmark target
│   ├── CSolver_Benchmark.csv     # C++ results
│   ├── benchmark.cpp             # C++ benchmark program
│   └── timer.h                   # C++ timing helper
├── pysolver/
│   ├── PySolver_Benchmark.csv    # Python results
│   └── benchmark.py              # Python benchmark program
└── README.md                     # Benchmark guide
```

## License

The benchmark programs are part of the project distributed under the [MIT License](../LICENSE).
