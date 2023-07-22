cmake_minimum_required(VERSION 3.2)
project(asynchronous)

add_executable(asynchronous
    main.cpp
)

target_link_libraries(asynchronous
    ${CONAN_LIBS}
    binapi_lib
)
