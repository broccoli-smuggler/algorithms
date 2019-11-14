cmake_minimum_required(VERSION 3.15)
project(think_cell)

set(CMAKE_CXX_STANDARD 17)

enable_testing()

add_executable(think_cell main.cpp interfaces/ITree.h BST.tcc BST.h)

add_subdirectory(test)

