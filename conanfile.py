from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
import os

class licensepp(ConanFile):
    name = "licensepp"
    version = "1.2.0"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }

    default_options = {
        "shared": False,
        "fPIC": True
    }
    
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "test/*", "lib/*"
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        
    def requirements(self):
        self.requires("nlohmann_json/[>=3.12.0]")
        self.requires("ripe/4.2.2")

    def build_requirements(self):
        self.test_requires("gtest/[>=1.17.0]")
        
    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["licensepp"]

