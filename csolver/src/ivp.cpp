#include <cstdint>
#include <jacobi/jacobi.h>
#include "ode/ivp.h"

csolver::IVPSolution<double> csolver::euler_method(const double a, const double b, const double h, jacobi::Vector<double> (*func)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>& initial) {
    const auto N = static_cast<std::uint64_t>((b - a) / h);
    const jacobi::Vector<double> time = a + h * jacobi::arange<double>(0.0, static_cast<double>(N+1), 1.0);
    jacobi::Matrix<double> solution(N+1, initial.size());
    solution.row(0) = initial;
    for (std::uint64_t i = 0; i < N; ++i) {
        solution.row(i+1) = solution.row(i) + h * func(time[i], solution.row(i));
    }
    return {time, solution};
}

csolver::IVPSolution<double> csolver::midpoint_method(const double a, const double b, const double h, jacobi::Vector<double> (*func)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>& initial) {
    const auto N = static_cast<std::uint64_t>((b - a) / h);
    const jacobi::Vector<double> time = a + h * jacobi::arange<double>(0.0, static_cast<double>(N+1), 1.0);
    jacobi::Matrix<double> solution(N+1, initial.size());
    solution.row(0) = initial;
    for (std::uint64_t i = 0; i < N; ++i) {
        jacobi::Vector<double> midpoint = solution.row(i) + (h / 2.0) * func(time[i], solution.row(i));
        solution.row(i+1) = solution.row(i) + h * func(time[i] + (h / 2.0), midpoint);
    }
    return {time, solution};
}

csolver::IVPSolution<double> csolver::heun_method(const double a, const double b, const double h, jacobi::Vector<double> (*func)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>& initial) {
    const auto N = static_cast<std::uint64_t>((b - a) / h);
    const jacobi::Vector<double> time = a + h * jacobi::arange<double>(0.0, static_cast<double>(N+1), 1.0);
    jacobi::Matrix<double> solution(N+1, initial.size());
    solution.row(0) = initial;
    for (std::uint64_t i = 0; i < N; ++i) {
        jacobi::Vector<double> slope1 = func(time[i], solution.row(i));
        jacobi::Vector<double> slope2 = func(time[i+1], solution.row(i) + h * slope1);
        jacobi::Vector<double> slope = (slope1 + slope2) / 2.0;
        solution.row(i+1) = solution.row(i) + h * slope;
    }
    return {time, solution};
}

csolver::IVPSolution<double> csolver::rk4(const double a, const double b, const double h, jacobi::Vector<double> (*func)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>& initial) {
    const auto N = static_cast<std::uint64_t>((b - a) / h);
    const jacobi::Vector<double> time = a + h * jacobi::arange<double>(0.0, static_cast<double>(N+1), 1.0);
    jacobi::Matrix<double> solution(N+1, initial.size());
    solution.row(0) = initial;
    for (std::uint64_t i = 0; i < N; ++i) {
        jacobi::Vector<double> k1 = func(time[i], solution.row(i));
        jacobi::Vector<double> k2 = func(time[i] + (h / 2.0), solution.row(i) + (h / 2.0) * k1);
        jacobi::Vector<double> k3 = func(time[i] + (h / 2.0), solution.row(i) + (h / 2.0) * k2);
        jacobi::Vector<double> k4 = func(time[i+1], solution.row(i) + h * k3);
        jacobi::Vector<double> slope = (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0;
        solution.row(i+1) = solution.row(i) + h * slope;
    }
    return {time, solution};
}
