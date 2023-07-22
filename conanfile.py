from conans import ConanFile, CMake

class binapiConan(ConanFile):
    url = "https://github.com/niXman/binapi"
    license = "Apache-2.0"
    description = "Binance C++ library"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*", "include/*", "examples/*", "CMakeLists.txt"

    requires = [
        "boost/1.82.0",
        "openssl/3.1.1",
    ]

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_EXPORT_COMPILE_COMMANDS"] = "ON"
        cmake.configure()
        return cmake
   
    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="include")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["binapi_lib"]
