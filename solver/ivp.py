import numpy as np

def euler_method(func, a, b, h, initial):
    """Euler's method: Solves first order ODE using Euler's method.
    :param func: function to find first derivative at any point x,y. func should accept 2 values.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :param initial: given initial condition to solve IVP problems.
    """
    N = int((b-a)/h)
    x = np.arange(a, b+h, step=h, dtype=np.float64)
    y = np.zeros_like(x, dtype=np.float64)
    y[0] = initial
    for i in range(N):
        y[i+1] = y[i] + h * func(x[i], y[i])
    return x, y

def midpoint_method(func, a, b, h, initial):
    """Midpoint method: Solves first order ODE using Midpoint method.
    :param func: function to find first derivative at any point x,y. func should accept 2 values.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :param initial: given initial condition to solve IVP problems.
    """
    N = int((b-a)/h)
    x = np.arange(a, b+h, step=h, dtype=np.float64)
    y = np.zeros_like(x, dtype=np.float64)
    y[0] = initial
    for i in range(N):
        slope1 = func(x[i], y[i])
        slope = func(x[i]+h/2, y[i] + (h/2)*slope1)
        y[i+1] = y[i] + h * slope
    return x, y

def heun_method(func, a, b, h, initial):
    """Heun method: Solves first order ODE using Heun's method.
    :param func: function to find first derivative at any point x,y. func should accept 2 values.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :param initial: given initial condition to solve IVP problems."""
    N = int((b-a)/h)
    x = np.arange(a, b+h, step=h, dtype=np.float64)
    y = np.zeros_like(x, dtype=np.float64)
    y[0] = initial
    for i in range(N):
        slope1 = func(x[i], y[i])
        y_ = y[i] + h * slope1
        slope2 = func(x[i+1], y_)
        slope = (slope1 + slope2) / 2
        y[i+1] = y[i] + h * slope
    return x, y

def rk4(func, a, b, h, initial):
    """RK4 method: Solves first order ODE using Runge-Kutta method of order 4.
    :param func: function to find first derivative at any point x,y. func should accept 2 values.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :param initial: given initial condition to solve IVP problems.
    """
    N = int((b-a)/h)
    x = np.arange(a, b+h, step=h, dtype=np.float64)
    y = np.zeros_like(x, dtype=np.float64)
    y[0] = initial
    for i in range(N):
        k1 = func(x[i], y[i])
        k2 = func(x[i]+h/2, y[i] + (h/2)*k1)
        k3 = func(x[i]+h/2, y[i] + (h/2)*k2)
        k4 = func(x[i+1], y[i]+h*k3)
        y[i+1] = y[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
    return x, y