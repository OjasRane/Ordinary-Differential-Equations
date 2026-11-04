#include "ode/ivp.h"
#include "ode/bvp.h"
#include "timer.h"
#include <fstream>
#include <string>

int main() {
    std::ofstream benchmarkFile("CSolver_Benchmark.csv", std::ios::binary | std::ios::out | std::ios::trunc);
    benchmarkFile << "System/Method,Run1,Run2,Run3,Run4,Run5,Run6,Run7\n";

    benchmark::Timer::run = 0;
    for (int i = 0; i < 10; ++i) {
        if (i > 2) {
            benchmark::Timer timer;
            auto solution = csolver::euler_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double sigma = 10.0; constexpr double rho = 28.0; constexpr double beta = 8.0/3.0; return jacobi::Vector<double>{ sigma*(y-x), x*(rho-z)-y, x*y-beta*z }; }, jacobi::Vector<double>{ 0.0, 1.0, 0.0 });
        }
        else {
            auto solution = csolver::euler_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double sigma = 10.0; constexpr double rho = 28.0; constexpr double beta = 8.0/3.0; return jacobi::Vector<double>{ sigma*(y-x), x*(rho-z)-y, x*y-beta*z }; }, jacobi::Vector<double>{ 0.0, 1.0, 0.0 });
        }
    }

    benchmarkFile << "Lorenz Attractor/Euler's Method(IVP),";
    for (double i : benchmark::Timer::time) {
        std::string s = std::to_string(i);
        benchmarkFile.write(s.c_str(), s.size());
        benchmarkFile.put(',');
    }
    benchmarkFile.seekp(-1, std::ios::end);
    benchmarkFile.put('\n');

    benchmark::Timer::run = 0;
    for (int i = 0; i < 10; ++i) {
        if (i > 2) {
            benchmark::Timer timer;
            auto solution = csolver::midpoint_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double sigma = 10.0; constexpr double rho = 28.0; constexpr double beta = 8.0/3.0; return jacobi::Vector<double>{ sigma*(y-x), x*(rho-z)-y, x*y-beta*z }; }, jacobi::Vector<double>{ 0.0, 1.0, 0.0 });
        }
        else {
            auto solution = csolver::midpoint_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double sigma = 10.0; constexpr double rho = 28.0; constexpr double beta = 8.0/3.0; return jacobi::Vector<double>{ sigma*(y-x), x*(rho-z)-y, x*y-beta*z }; }, jacobi::Vector<double>{ 0.0, 1.0, 0.0 });
        }
    }

    benchmarkFile << "Lorenz Attractor/Midpoint Method(IVP),";
    for (double i : benchmark::Timer::time) {
        std::string s = std::to_string(i);
        benchmarkFile.write(s.c_str(), s.size());
        benchmarkFile.put(',');
    }
    benchmarkFile.seekp(-1, std::ios::end);
    benchmarkFile.put('\n');

    benchmark::Timer::run = 0;
    for (int i = 0; i < 10; ++i) {
        if (i > 2) {
            benchmark::Timer timer;
            auto solution = csolver::heun_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double sigma = 10.0; constexpr double rho = 28.0; constexpr double beta = 8.0/3.0; return jacobi::Vector<double>{ sigma*(y-x), x*(rho-z)-y, x*y-beta*z }; }, jacobi::Vector<double>{ 0.0, 1.0, 0.0 });
        }
        else {
            auto solution = csolver::heun_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double sigma = 10.0; constexpr double rho = 28.0; constexpr double beta = 8.0/3.0; return jacobi::Vector<double>{ sigma*(y-x), x*(rho-z)-y, x*y-beta*z }; }, jacobi::Vector<double>{ 0.0, 1.0, 0.0 });
        }
    }

    benchmarkFile << "Lorenz Attractor/Heun's Method(IVP),";
    for (double i : benchmark::Timer::time) {
        std::string s = std::to_string(i);
        benchmarkFile.write(s.c_str(), s.size());
        benchmarkFile.put(',');
    }
    benchmarkFile.seekp(-1, std::ios::end);
    benchmarkFile.put('\n');

    benchmark::Timer::run = 0;
    for (int i = 0; i < 10; ++i) {
        if (i > 2) {
            benchmark::Timer timer;
            auto solution = csolver::rk4(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double sigma = 10.0; constexpr double rho = 28.0; constexpr double beta = 8.0/3.0; return jacobi::Vector<double>{ sigma*(y-x), x*(rho-z)-y, x*y-beta*z }; }, jacobi::Vector<double>{ 0.0, 1.0, 0.0 });
        }
        else {
            auto solution = csolver::rk4(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double sigma = 10.0; constexpr double rho = 28.0; constexpr double beta = 8.0/3.0; return jacobi::Vector<double>{ sigma*(y-x), x*(rho-z)-y, x*y-beta*z }; }, jacobi::Vector<double>{ 0.0, 1.0, 0.0 });
        }
    }

    benchmarkFile << "Lorenz Attractor/Runge Kutta Method of order 4(IVP),";
    for (double i : benchmark::Timer::time) {
        std::string s = std::to_string(i);
        benchmarkFile.write(s.c_str(), s.size());
        benchmarkFile.put(',');
    }
    benchmarkFile.seekp(-1, std::ios::end);
    benchmarkFile.put('\n');

    benchmark::Timer::run = 0;
    for (int i = 0; i < 10; ++i) {
        if (i > 2){
            benchmark::Timer timer;
            auto solution = csolver::midpoint_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double a = 1.4; return jacobi::Vector<double>{ -a*x-4*y-4*z-y*y, -a*y-4*z-4*x-z*z, -a*z-4*x-4*y-x*x }; }, jacobi::Vector<double>{1.0, 0.0, 0.0});
        }
        else {
            auto solution = csolver::midpoint_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double a = 1.4; return jacobi::Vector<double>{ -a*x-4*y-4*z-y*y, -a*y-4*z-4*x-z*z, -a*z-4*x-4*y-x*x }; }, jacobi::Vector<double>{1.0, 0.0, 0.0});
        }
    }

    benchmarkFile << "Halvorsen Attractor/Midpoint Method(IVP),";
    for (double i : benchmark::Timer::time) {
        std::string s = std::to_string(i);
        benchmarkFile.write(s.c_str(), s.size());
        benchmarkFile.put(',');
    }
    benchmarkFile.seekp(-1, std::ios::end);
    benchmarkFile.put('\n');

    benchmark::Timer::run = 0;
    for (int i = 0; i < 10; ++i) {
        if (i > 2){
            benchmark::Timer timer;
            auto solution = csolver::heun_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double a = 1.4; return jacobi::Vector<double>{ -a*x-4*y-4*z-y*y, -a*y-4*z-4*x-z*z, -a*z-4*x-4*y-x*x }; }, jacobi::Vector<double>{1.0, 0.0, 0.0});
        }
        else {
            auto solution = csolver::heun_method(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double a = 1.4; return jacobi::Vector<double>{ -a*x-4*y-4*z-y*y, -a*y-4*z-4*x-z*z, -a*z-4*x-4*y-x*x }; }, jacobi::Vector<double>{1.0, 0.0, 0.0});
        }
    }

    benchmarkFile << "Halvorsen Attractor/Heun's Method(IVP),";
    for (double i : benchmark::Timer::time) {
        std::string s = std::to_string(i);
        benchmarkFile.write(s.c_str(), s.size());
        benchmarkFile.put(',');
    }
    benchmarkFile.seekp(-1, std::ios::end);
    benchmarkFile.put('\n');

    benchmark::Timer::run = 0;
    for (int i = 0; i < 10; ++i) {
        if (i > 2){
            benchmark::Timer timer;
            auto solution = csolver::rk4(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double a = 1.4; return jacobi::Vector<double>{ -a*x-4*y-4*z-y*y, -a*y-4*z-4*x-z*z, -a*z-4*x-4*y-x*x }; }, jacobi::Vector<double>{1.0, 0.0, 0.0});
        }
        else {
            auto solution = csolver::rk4(0.0, 100.0, 0.01, [](double t, const jacobi::Vector<double>& vec) -> jacobi::Vector<double> { const double x = vec[0]; const double y = vec[1]; const double z = vec[2]; constexpr double a = 1.4; return jacobi::Vector<double>{ -a*x-4*y-4*z-y*y, -a*y-4*z-4*x-z*z, -a*z-4*x-4*y-x*x }; }, jacobi::Vector<double>{1.0, 0.0, 0.0});
        }
    }

    benchmarkFile << "Halvorsen Attractor/Runge Kutta Method of order 4(IVP),";
    for (double i : benchmark::Timer::time) {
        std::string s = std::to_string(i);
        benchmarkFile.write(s.c_str(), s.size());
        benchmarkFile.put(',');
    }
    benchmarkFile.seekp(-1, std::ios::end);
    benchmarkFile.put('\n');

    benchmark::Timer::run = 0;
    for (int i = 0; i < 10; ++i) {
        if (i > 2) {
            benchmark::Timer timer;
            auto solution = csolver::fdm(0.0, 100.0, 0.01, 0.0, 0.0, [](double x) -> double { return 0.0; }, [](double x) -> double { return 0.0; }, [](double x) -> double { return -2.0; });
        }
        else {
            auto solution = csolver::fdm(0.0, 100.0, 0.01, 0.0, 0.0, [](double x) -> double { return 0.0; }, [](double x) -> double { return 0.0; }, [](double x) -> double { return -2.0; });
        }
    }

    benchmarkFile << "Poisson Equation/FDM(BVP),";
    for (double i : benchmark::Timer::time) {
        std::string s = std::to_string(i);
        benchmarkFile.write(s.c_str(), s.size());
        benchmarkFile.put(',');
    }
    benchmarkFile.seekp(-1, std::ios::end);
    benchmarkFile.put('\n');

    benchmarkFile.close();
}