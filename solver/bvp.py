import numpy as np

def fdm(a, b, h, **kwargs):
    """Finite Difference Method: Solves second order linear ODE using finite differences method.
    :param a: start point. The start of region of observation.
    :param b: end point. The end of region of observation.
    :param h: step size.
    :kwargs initial: initial value for the BVP problem.
    :kwargs end: end value for the BVP problem.
    :kwargs p, q, r: Functions from the linear second order ODE: y'' + Py' + Qy = R. All functions should accept single parameter.
    """
    N = int((b-a)/h)
    initial = kwargs.get("initial", None)
    end = kwargs.get("end", None)
    p, q, r= kwargs.get("p", None), kwargs.get("q", None), kwargs.get("r", None)
    x = a + h * np.arange(1, N, dtype=np.float64)
    I0 = 2 - h * p(x)
    I1 = 2 * (h**2) * q(x) - 4
    I2 = 2 + h * p(x)
    B = 2 * (h**2) * r(x)
    B[0] -= I0[0] * initial
    B[-1] -= I2[-1] * end
    sparse_matrix = np.empty((3, N-1))
    sparse_matrix[0, 0] = 0
    sparse_matrix[2, 0] = 0
    sparse_matrix[0, 1:] = I2[:-1]
    sparse_matrix[1, :] = I1
    sparse_matrix[2, 1:] = I0[1:]
    eliminated_matrix = np.empty((2, N-1))
    eliminated_matrix[0, :] = sparse_matrix[0, :]
    eliminated_matrix[1, 0] = sparse_matrix[1, 0]
    for i in range(1, N-1):
        a_i = sparse_matrix[2, i]
        d_i = eliminated_matrix[1, i-1]
        factor = a_i / d_i
        eliminated_matrix[1, i] = sparse_matrix[1, i] - factor * eliminated_matrix[0, i]
        B[i] -= factor * B[i-1]
    y = np.empty(N-1)
    y[-1] = B[-1] / eliminated_matrix[1, -1]
    for i in range(N-3, -1, -1):
        y[i] = (B[i] - eliminated_matrix[0, i+1] * y[i+1]) / eliminated_matrix[1, i]

    x, y = np.insert(x, 0, a), np.insert(y, 0, initial)
    x, y = np.append(x, b), np.append(y, end)
    return x, y