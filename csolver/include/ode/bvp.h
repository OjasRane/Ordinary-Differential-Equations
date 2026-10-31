#pragma once
#include <jacobi/jacobi.h>

namespace csolver {
    template <typename T>
    struct BVPSolution {
        jacobi::Vector<T> x;
        jacobi::Vector<T> y;
        friend BVPSolution<double> fdm(double, double, double, double, double, double (*)(double), double (*)(double), double (*)(double));
    private:
        BVPSolution(const jacobi::Vector<T>& x, const jacobi::Vector<T>& y) : x(x), y(y) {}
    };

    BVPSolution<double> fdm(double, double, double, double, double, double (*)(double), double (*)(double), double (*)(double));
}