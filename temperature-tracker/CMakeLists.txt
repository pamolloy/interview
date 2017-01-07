cmake_minimum_required(VERSION 3.6.2)

set(CMAKE_CXX_STANDARD 11)

project(temp_tracker)

find_package(GTest REQUIRED)
include_directories(${GTEST_INCLUDE_DIRS})
enable_testing()

file(GLOB SOURCES "*.cc")
add_executable(testTempTracker ${SOURCES})
target_link_libraries(testTempTracker ${GTEST_BOTH_LIBRARIES} pthread)

add_test(testTempTracker testTempTracker)
