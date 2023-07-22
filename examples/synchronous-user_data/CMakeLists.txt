cmake_minimum_required(VERSION 3.2)
project(synchronous-user_data)

add_executable(synchronous-user_data
    main.cpp
)

target_link_libraries(synchronous-user_data
    ${CONAN_LIBS}
    binapi_lib
)
