#pragma once
#include <chrono>

namespace benchmark {
    class Timer {
    private:
        std::chrono::time_point<std::chrono::high_resolution_clock> m_StartPoint;
    public:
        static double time[7];
        static int run;
        Timer() : m_StartPoint(std::chrono::high_resolution_clock::now()) {}
        ~Timer() {
            const auto endPoint = std::chrono::high_resolution_clock::now();

            const auto start = std::chrono::time_point_cast<std::chrono::microseconds>(m_StartPoint).time_since_epoch().count();
            const auto end = std::chrono::time_point_cast<std::chrono::microseconds>(endPoint).time_since_epoch().count();
            const auto duration = end - start;

            time[run++] = duration * 0.001;
        }
    };

    int Timer::run = 0;
    double Timer::time[7];
}
