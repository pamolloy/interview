cmake_minimum_required(VERSION 3.6.2)

set(CMAKE_CXX_STANDARD 11)

project(left_unqiue)

find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})
enable_testing()

file(GLOB SOURCES "*.cc")
add_executable(testLeftUnique ${SOURCES})
target_link_libraries(testLeftUnique ${GTEST_BOTH_LIBRARIES} pthread)

add_test(testLeftUnique testLeftUnique)
