import numpy as np

def euler_method(a, b, h, **kwargs):
    """Euler's method: Solves first or second order ODE using Euler's method.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :kwargs func: Function to find first derivative at any point x,y. func should accept 2 values. Required for first order ODE.
    :kwargs initial: given initial condition of solution variable to solve IVP problems. Required.
    :kwargs initial_slope: given initial condition of first derivative to solve IVP problems.
    :kwargs p, q: Functions from the general second order ODE: y'' + Py' = Q. Both functions should accept 2 values. Required for second order ODE.
    """
    N = int((b-a)/h)
    second_order = False
    func = kwargs.get("func", None)
    x = a + h * np.arange(N+1, dtype=np.float64)
    y = np.zeros_like(x, dtype=np.float64)
    y[0] = kwargs.get("initial", None)
    if func is None:
        second_order = True
        p, q = kwargs.get("p", None), kwargs.get("q", None)
        initial_slope = kwargs.get("initial_slope", None)
        dy = np.zeros_like(x, dtype=np.float64)
        dy[0] = initial_slope
    for i in range(N):
        if second_order:
            dy[i+1] = dy[i] + h * (q(x[i], y[i]) - p(x[i], y[i]) * dy[i])
            y[i+1] = y[i] + h * dy[i+1]
        else:
            y[i+1] = y[i] + h * func(x[i], y[i])
    return x, y

def midpoint_method(a, b, h, **kwargs):
    """Midpoint method: Solves first or second order ODE using Midpoint method.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :kwargs func: Function to find first derivative at any point x,y. func should accept 2 values. Required for first order ODE.
    :kwargs initial: given initial condition of solution variable to solve IVP problems. Required.
    :kwargs initial_slope: given initial condition of first derivative to solve IVP problems.
    :kwargs p, q: Functions from the general second order ODE: y'' + Py' = Q. Both functions should accept 2 values. Required for second order ODE.
    """
    N = int((b-a)/h)
    x = a + h * np.arange(N+1, dtype=np.float64)
    y = np.zeros_like(x, dtype=np.float64)
    y[0] = kwargs.get("initial", None)
    second_order = False
    func = kwargs.get("func", None)
    if func is None:
        second_order = True
        p, q = kwargs.get("p", None), kwargs.get("q", None)
        initial_slope = kwargs.get("initial_slope", None)
        dy = np.zeros_like(x, dtype=np.float64)
        dy[0] = initial_slope
    for i in range(N):
        if second_order:
            slope1 = q(x[i], y[i]) - p(x[i], y[i]) * dy[i]
            x_mid = x[i] + h / 2
            dy_mid = dy[i] + (h/2) * slope1
            y_mid = y[i] + (h/2) * dy[i]
            slope = q(x_mid, y_mid) - p(x_mid, y_mid) * dy_mid
            dy[i+1] = dy[i] + h * slope
            y[i+1] = y[i] + h * dy_mid
        else:
            slope1 = func(x[i], y[i])
            slope = func(x[i]+h/2, y[i] + (h/2)*slope1)
            y[i+1] = y[i] + h * slope
    return x, y

def heun_method(a, b, h, **kwargs):
    """Heun method: Solves first or second order ODE using Heun's method.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :kwargs func: Function to find first derivative at any point x,y. func should accept 2 values. Required for first order ODE.
    :kwargs initial: given initial condition of solution variable to solve IVP problems. Required.
    :kwargs initial_slope: given initial condition of first derivative to solve IVP problems.
    :kwargs p, q: Functions from the general second order ODE: y'' + Py' = Q. Both functions should accept 2 values. Required for second order ODE.
    """
    N = int((b-a)/h)
    x = a + h * np.arange(N+1, dtype=np.float64)
    y = np.zeros_like(x, dtype=np.float64)
    y[0] = kwargs.get("initial", None)
    second_order = False
    func = kwargs.get("func", None)
    if func is None:
        second_order = True
        p, q = kwargs.get("p", None), kwargs.get("q", None)
        initial_slope = kwargs.get("initial_slope", None)
        dy = np.zeros_like(x, dtype=np.float64)
        dy[0] = initial_slope
    for i in range(N):
        if second_order:
            slope1 = q(x[i], y[i]) - p(x[i], y[i]) * dy[i]
            dy_ = dy[i] + h * slope1
            y_ = y[i] + h * dy[i]
            slope2 = q(x[i+1], y_) - p(x[i+1], y_) * dy_
            slope = (slope1 + slope2) / 2
            dy[i+1] = dy[i] + h * slope
            y[i+1] = y[i] + h * (dy[i] + dy_) / 2
        else:
            slope1 = func(x[i], y[i])
            slope2 = func(x[i+1], y[i] + h * slope1)
            slope = (slope1 + slope2) / 2
            y[i+1] = y[i] + h * slope
    return x, y

def rk4(a, b, h, **kwargs):
    """RK4 method: Solves first or second order ODE using Runge-Kutta method of order 4.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :kwargs func: Function to find first derivative at any point x,y. func should accept 2 values. Required for first order ODE.
    :kwargs initial: given initial condition of solution variable to solve IVP problems. Required.
    :kwargs initial_slope: given initial condition of first derivative to solve IVP problems.
    :kwargs p, q: Functions from the general second order ODE: y'' + Py' = Q. Both functions should accept 2 values. Required for second order ODE.
    """
    N = int((b-a)/h)
    x = a + h * np.arange(N+1, dtype=np.float64)
    y = np.zeros_like(x, dtype=np.float64)
    y[0] = kwargs.get("initial", None)
    second_order = False
    func = kwargs.get("func", None)
    if func is None:
        second_order = True
        p, q = kwargs.get("p", None), kwargs.get("q", None)
        initial_slope = kwargs.get("initial_slope", None)
        dy = np.zeros_like(x, dtype=np.float64)
        dy[0] = initial_slope
    for i in range(N):
        if second_order:
            k1 = q(x[i], y[i]) - p(x[i], y[i]) * dy[i]
            x_ = x[i] + h / 2
            dy2 = dy[i] + (h/2)*k1
            y_ = y[i] + (h/2)*dy[i]
            k2 = q(x_, y_) - p(x_, y_) * dy2
            dy3 = dy[i] + (h/2)*k2
            y_ = y[i] + (h/2)*dy2
            k3 = q(x_, y_) - p(x_, y_) * dy3
            x_ = x[i+1]
            dy4 = dy[i] + h*k3
            y_ = y[i] + h*dy3
            k4 = q(x_, y_) - p(x_, y_) * dy4
            dy[i+1] = dy[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
            y[i+1] = y[i] + h*(dy[i] + 2*dy2 + 2*dy3 + dy4)/6
        else:
            k1 = func(x[i], y[i])
            k2 = func(x[i]+h/2, y[i] + (h/2)*k1)
            k3 = func(x[i]+h/2, y[i] + (h/2)*k2)
            k4 = func(x[i+1], y[i]+h*k3)
            y[i+1] = y[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    return x, y