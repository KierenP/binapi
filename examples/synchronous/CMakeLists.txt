cmake_minimum_required(VERSION 3.2)
project(synchronous)

add_executable(synchronous
    main.cpp
)

target_link_libraries(synchronous
    ${CONAN_LIBS}
    binapi_lib
)
