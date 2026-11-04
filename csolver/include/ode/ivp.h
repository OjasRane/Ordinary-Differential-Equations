#pragma once
#include <jacobi/jacobi.h>

namespace csolver {
    template <typename T>
    struct IVPSolution {
        jacobi::Vector<T> time;
        jacobi::Matrix<T> solution;
        friend IVPSolution<double> euler_method(double, double, double, jacobi::Vector<double> (*)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>&);
        friend IVPSolution<double> midpoint_method(double, double, double, jacobi::Vector<double> (*)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>&);
        friend IVPSolution<double> heun_method(double, double, double, jacobi::Vector<double> (*)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>&);
        friend IVPSolution<double> rk4(double, double, double, jacobi::Vector<double> (*)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>&);
    private:
        IVPSolution(const jacobi::Vector<T>& time, const jacobi::Matrix<T>& solution) : time(time), solution(solution) {}
    };

    IVPSolution<double> euler_method(double, double, double, jacobi::Vector<double> (*)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>&);
    IVPSolution<double> midpoint_method(double, double, double, jacobi::Vector<double> (*)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>&);
    IVPSolution<double> heun_method(double, double, double, jacobi::Vector<double> (*)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>&);
    IVPSolution<double> rk4(double, double, double, jacobi::Vector<double> (*)(double, const jacobi::Vector<double>&), const jacobi::Vector<double>&);
}
