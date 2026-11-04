cmake_minimum_required(VERSION 3.20)
project(Ordinary-Differential-Equations VERSION 0.5.0 LANGUAGES CXX)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_library(ODE STATIC src/ivp.cpp src/bvp.cpp)

set(JACOBI_ROOT ${CMAKE_CURRENT_SOURCE_DIR}/dependencies/jacobi)
set(JACOBI_LIBRARY
        ${JACOBI_ROOT}/lib/${CMAKE_STATIC_LIBRARY_PREFIX}Jacobi${CMAKE_STATIC_LIBRARY_SUFFIX}
)
if(NOT EXISTS "${JACOBI_ROOT}/include/jacobi/jacobi.h" OR NOT EXISTS "${JACOBI_LIBRARY}")
    message(FATAL_ERROR
            "Jacobi was not found. Build Jacobi and place its include/ directory and static library at "
            "${JACOBI_ROOT}/include and ${JACOBI_ROOT}/lib/.")
endif()

target_include_directories(ODE PUBLIC ${JACOBI_ROOT}/include)
target_include_directories(ODE PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<INSTALL_INTERFACE:include>
)
target_link_libraries(ODE PUBLIC ${JACOBI_LIBRARY})
