#include <jacobi/jacobi.h>
#include "ode/ivp.h"

static jacobi::Vector<double> func(double t, const jacobi::Vector<double>& vec) {
    const double x = vec[0];
    const double y = vec[1];
    const double z = vec[2];
    constexpr double a = 1.4;
    return jacobi::Vector<double>{ -a*x-4*y-4*z-y*y, -a*y-4*z-4*x-z*z, -a*z-4*x-4*y-x*x };
}

int main() {
    constexpr double a = 0.0, b = 1000.0, h = 0.01;
    const jacobi::Vector<double> initial{ 1.0, 0.0, 0.0 };

    const auto [time, solution] = csolver::rk4(a, b, h, func, initial);
    time.save("double_halvorsen_attractor_time.jcbi");
    solution.save("double_halvorsen_attractor_solution.jcbi");
}
