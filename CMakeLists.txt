cmake_minimum_required(VERSION 3.2)
project(binapi)

#----------------------------------------------------------------
# conan related stuff

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

#----------------------------------------------------------------

set(BINAPI_SOURCES
    src/api.cpp
    src/enums.cpp
    src/errors.cpp
    src/pairslist.cpp
    src/reports.cpp
    src/tools.cpp
    src/types.cpp
    src/websocket.cpp
)

add_library(binapi_lib STATIC 
    ${BINAPI_SOURCES}
)

target_link_libraries(binapi_lib
    ${CONAN_LIBS}
)

target_include_directories(binapi_lib
    PUBLIC ${CMAKE_SOURCE_DIR}/include
)

target_compile_definitions(binapi_lib
    PUBLIC DTF_HEADER_ONLY
)

target_compile_options(binapi_lib
    PUBLIC -Wall 
    PUBLIC -Wextra
)

target_link_options(binapi_lib
    PUBLIC -fuse-ld=lld
)

add_executable(binapi
    src/main.cpp
)

target_link_libraries(binapi
    ${CONAN_LIBS}
    binapi_lib
)

add_subdirectory(examples/asynchronous)
add_subdirectory(examples/asynchronous-user_data)
add_subdirectory(examples/synchronous)
add_subdirectory(examples/synchronous-user_data)
add_subdirectory(examples/websockets)
