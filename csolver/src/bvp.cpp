#include <cstdint>
#include <stdexcept>
#include <jacobi/jacobi.h>
#include "ode/bvp.h"

csolver::BVPSolution<double> csolver::fdm(const double a, const double b, const double h, const double initial, const double end, double (*p)(double), double (*q)(double), double (*r)(double)) {
    const auto N = static_cast<std::uint64_t>((b - a) / h);
    if (N < 3) {
        throw std::invalid_argument("N must be greater than 3");
    }
    jacobi::Vector<double> x = a + h * jacobi::arange<double>(1.0, static_cast<double>(N), 1.0);
    const jacobi::Vector<double> I0 = 2.0 - h * jacobi::map(p, x);
    jacobi::Vector<double> I1 = 2.0 * h * h * jacobi::map(q, x) - 4.0;
    const jacobi::Vector<double> I2 = 2.0 + h * jacobi::map(p, x);
    jacobi::Vector<double> B = 2.0 * h * h * jacobi::map(r, x);
    B[0] -= I0[0] * initial;
    B[N-1- 1] -= I2[N-1 - 1] * end;

    for (std::uint64_t i = 0; i < N-1 - 1; ++i) {
        const double a_i = I0[i+1];
        const double d_i = I1[i];
        const double factor = a_i / d_i;
        I1[i+1] -= factor * I2[i];
        B[i+1] -= factor * B[i];
    }
    jacobi::Vector<double> y(N-1);
    y[N-1 - 1] = B[N-1 - 1] / I1[N-1 - 1];
    for (std::uint64_t i = N-1 - 1; i > 0; --i) {
        y[i-1] = (B[i-1] - I2[i-1] * y[i]) / I1[i-1];
    }
    return {x, y};
}