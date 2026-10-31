cmake_minimum_required(VERSION 3.20)
project(Ordinary-Differential-Equations VERSION 0.5.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_library(ODE STATIC src/ivp.cpp src/bvp.cpp)

target_include_directories(ODE PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/dependencies/jacobi/include)
target_include_directories(ODE PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(ODE PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/dependencies/jacobi/lib/libJacobi.a)