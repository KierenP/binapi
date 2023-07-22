cmake_minimum_required(VERSION 3.2)
project(websockets)

add_executable(websockets
    main.cpp
)

target_link_libraries(websockets
    ${CONAN_LIBS}
    binapi_lib
)