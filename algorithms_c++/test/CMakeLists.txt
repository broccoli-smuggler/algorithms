include(ExternalProject)

find_package(Threads REQUIRED)

if(NOT TARGET libgtest)
  # Download and install GoogleTest
  ExternalProject_Add(
    gtest
    URL https://github.com/google/googletest/archive/master.zip
    PREFIX ${CMAKE_CURRENT_BINARY_DIR}/gtest
    # Disable install step
    INSTALL_COMMAND ""
  )

  # Get gtest source and binary directories from CMake project
  ExternalProject_Get_Property(gtest source_dir binary_dir)

  # Create a libgtest target to be used as a dependency by test programs
  add_library(libgtest IMPORTED STATIC GLOBAL)
  add_dependencies(libgtest gtest)

  # Set libgtest properties
  set_target_properties(libgtest PROPERTIES
    "IMPORTED_LOCATION" "${binary_dir}/lib/libgtest.a"
    "IMPORTED_LINK_INTERFACE_LIBRARIES" "${CMAKE_THREAD_LIBS_INIT}"
  )

  # Create a libgmock target to be used as a dependency by test programs
  add_library(libgmock IMPORTED STATIC GLOBAL)
  add_dependencies(libgmock gtest)

  # Set libgmock properties
  set_target_properties(libgmock PROPERTIES
    "IMPORTED_LOCATION" "${binary_dir}/lib/libgmock.a"
    "IMPORTED_LINK_INTERFACE_LIBRARIES" "${CMAKE_THREAD_LIBS_INIT}"
  )

  include_directories("${source_dir}/googletest/include"
                    "${source_dir}/googlemock/include")
else()
  message("Found gtest")

  # Get gtest source and binary directories from CMake project
  ExternalProject_Get_Property(gtest source_dir binary_dir)

  include_directories("${source_dir}/googletest/include"
                      "${source_dir}/googlemock/include")
endif()

file(GLOB SRCS *.cpp)

add_executable(think-cell_test ${SRCS})

target_link_libraries(think-cell_test
        libgtest
        libgmock
        )

target_include_directories(think-cell_test PUBLIC
        ../
        ./mocks
        )

add_test(NAME think-cell_test
        COMMAND think-cell_test
        )
#
#add_custom_target(imagr_data_capture_coverage)
#add_custom_command(TARGET imagr_data_capture_coverage
#        COMMAND echo "========== Coverage =========="
#        COMMAND ./imagr_data_capture_unit_tests
#        COMMAND lcov --capture --directory ${CMAKE_CURRENT_BINARY_DIR}/CMakeFiles/imagr_data_capture_unit_tests.dir --output-file full_coverage.info
#        COMMAND lcov --extract full_coverage.info "*/data_capture/*" --output-file data_capture_coverage.info
#        COMMAND genhtml data_capture_coverage.info --output-directory data_capture_coverage
#        )
#
#add_dependencies(imagr_data_capture_coverage imagr_data_capture_unit_tests)

