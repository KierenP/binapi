cmake_minimum_required(VERSION 3.2)
project(asynchronous-user_data)

add_executable(asynchronous-user_data
    main.cpp
)

target_link_libraries(asynchronous-user_data
    ${CONAN_LIBS}
    binapi_lib
)