import numpy as np
from solver import ivp, bvp
from time import perf_counter_ns

def lorenz_func(t, state):
    x, y, z = state
    sigma = 10
    rho = 28
    beta = 8/3
    return np.array([
        sigma*(y-x),
        x*(rho-z)-y,
        x*y-beta*z
    ])

def halvorsen_func(t, state):
    x, y, z = state
    a = 1.4
    return np.array([
        -a*x-4*y-4*z-y**2,
        -a*y-4*z-4*x-z**2,
        -a*z-4*x-4*y-x**2
    ])

benchmarkFile = open("PySolver_Benchmark.csv", "wb")
benchmarkFile.write(b"System/Method,Run1,Run2,Run3,Run4,Run5,Run6,Run6\n")

benchmarkFile.write(b"Lorenz Attractor/Euler's Method(IVP),")
for i in range(10):
    if i > 2:
        start = perf_counter_ns()
        solution = ivp.state_euler_method(0, 100, 0.01, lorenz_func, np.array([0, 1, 0]))
        end = perf_counter_ns()
        time_elapsed = str(round((end - start)*(10**(-6)), 6))
        benchmarkFile.write(time_elapsed.encode("utf-8"))
        benchmarkFile.write(b',')
    else:
        solution = ivp.state_euler_method(0, 100, 0.01, lorenz_func, np.array([0, 1, 0]))
benchmarkFile.seek(-1, 2)
benchmarkFile.write(b"\n")

benchmarkFile.write(b"Lorenz Attractor/Midpoint Method(IVP),")
for i in range(10):
    if i > 2:
        start = perf_counter_ns()
        solution = ivp.state_midpoint_method(0, 100, 0.01, lorenz_func, np.array([0, 1, 0]))
        end = perf_counter_ns()
        time_elapsed = str(round((end - start)*(10**(-6)), 6))
        benchmarkFile.write(time_elapsed.encode("utf-8"))
        benchmarkFile.write(b',')
    else:
        solution = ivp.state_midpoint_method(0, 100, 0.01, lorenz_func, np.array([0, 1, 0]))
benchmarkFile.seek(-1, 2)
benchmarkFile.write(b"\n")

benchmarkFile.write(b"Lorenz Attractor/Heun's Method(IVP),")
for i in range(10):
    if i > 2:
        start = perf_counter_ns()
        solution = ivp.state_heun_method(0, 100, 0.01, lorenz_func, np.array([0, 1, 0]))
        end = perf_counter_ns()
        time_elapsed = str(round((end - start)*(10**(-6)), 6))
        benchmarkFile.write(time_elapsed.encode("utf-8"))
        benchmarkFile.write(b',')
    else:
        solution = ivp.state_heun_method(0, 100, 0.01, lorenz_func, np.array([0, 1, 0]))
benchmarkFile.seek(-1, 2)
benchmarkFile.write(b"\n")

benchmarkFile.write(b"Lorenz Attractor/Runge Kutta Method of order 4(IVP),")
for i in range(10):
    if i > 2:
        start = perf_counter_ns()
        solution = ivp.state_rk4(0, 100, 0.01, lorenz_func, np.array([0, 1, 0]))
        end = perf_counter_ns()
        time_elapsed = str(round((end - start)*(10**(-6)), 6))
        benchmarkFile.write(time_elapsed.encode("utf-8"))
        benchmarkFile.write(b',')
    else:
        solution = ivp.state_rk4(0, 100, 0.01, lorenz_func, np.array([0, 1, 0]))
benchmarkFile.seek(-1, 2)
benchmarkFile.write(b"\n")

benchmarkFile.write(b"Halvorsen Attractor/Midpoint Method(IVP),")
for i in range(10):
    if i > 2:
        start = perf_counter_ns()
        t, solution = ivp.state_midpoint_method(0, 100, 0.01, halvorsen_func, np.array([1, 0, 0]))
        end = perf_counter_ns()
        time_elapsed = str(round((end - start)*(10**(-6)), 6))
        benchmarkFile.write(time_elapsed.encode("utf-8"))
        benchmarkFile.write(b',')
    else:
        t, solution = ivp.state_midpoint_method(0, 100, 0.01, halvorsen_func, np.array([1, 0, 0]))
benchmarkFile.seek(-1, 2)
benchmarkFile.write(b"\n")

benchmarkFile.write(b"Halvorsen Attractor/Heun's Method(IVP),")
for i in range(10):
    if i > 2:
        start = perf_counter_ns()
        solution = ivp.state_heun_method(0, 100, 0.01, halvorsen_func, np.array([1, 0, 0]))
        end = perf_counter_ns()
        time_elapsed = str(round((end - start)*(10**(-6)), 6))
        benchmarkFile.write(time_elapsed.encode("utf-8"))
        benchmarkFile.write(b',')
    else:
        solution = ivp.state_heun_method(0, 100, 0.01, halvorsen_func, np.array([1, 0, 0]))
benchmarkFile.seek(-1, 2)
benchmarkFile.write(b"\n")

benchmarkFile.write(b"Halvorsen Attractor/Runge Kutta Method of order 4(IVP),")
for i in range(10):
    if i > 2:
        start = perf_counter_ns()
        solution = ivp.state_rk4(0, 100, 0.01, halvorsen_func, np.array([1, 0, 0]))
        end = perf_counter_ns()
        time_elapsed = str(round((end - start)*(10**(-6)), 6))
        benchmarkFile.write(time_elapsed.encode("utf-8"))
        benchmarkFile.write(b',')
    else:
        solution = ivp.state_rk4(0, 100, 0.01, halvorsen_func, np.array([1, 0, 0]))
benchmarkFile.seek(-1, 2)
benchmarkFile.write(b"\n")

benchmarkFile.write(b"Poisson Equation/FDM(BVP),")
for i in range(10):
    if i > 2:
        start = perf_counter_ns()
        solution = bvp.fdm(0, 100, 0.01, initial=0, end=0, p=lambda x: 0*x, q=lambda x: 0*x, r=lambda x: 0*x-2)
        end = perf_counter_ns()
        time_elapsed = str(round((end - start)*(10**(-6)), 6))
        benchmarkFile.write(time_elapsed.encode("utf-8"))
        benchmarkFile.write(b",")
    else:
        solution = bvp.fdm(0, 100, 0.01, initial=0, end=0, p=lambda x: 0*x, q=lambda x: 0*x, r=lambda x: 0*x-2)
benchmarkFile.seek(-1, 2)
benchmarkFile.write(b"\n")

benchmarkFile.close()