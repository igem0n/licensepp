cmake_minimum_required (VERSION 3.30)

project (licensepp CXX)

set (LICENSEPP_MAJOR "1")
set (LICENSEPP_MINOR "2")
set (LICENSEPP_PATCH "0")

set (LICENSEPP_SOVERSION "${LICENSEPP_MAJOR}.${LICENSEPP_MINOR}.${LICENSEPP_PATCH}")

find_package(nlohmann_json REQUIRED)
find_package(ripe REQUIRED)

file(GLOB HEADER_FILES "include/license++/*.h")

set(LICENSEPP_SOURCE_FILES
    src/utils.cc
    src/json-object.cc
    src/crypto/aes.cc
    src/crypto/base64.cc
    src/crypto/base16.cc
    src/crypto/rsa.cc
    src/issuing-authority.cc
    src/license.cc
    src/c-bindings.cc
)

add_library (licensepp ${LICENSEPP_SOURCE_FILES})

target_sources(licensepp PUBLIC FILE_SET HEADERS BASE_DIRS include FILES ${HEADER_FILES})

if(BUILD_SHARED_LIBS)
    set_target_properties (licensepp PROPERTIES VERSION ${LICENSEPP_SOVERSION})
endif()

target_link_libraries (licensepp
    nlohmann_json::nlohmann_json
    ripe::ripe
)

install (TARGETS licensepp FILE_SET HEADERS)

########################################## Unit Testing ###################################
include(CTest)
if (BUILD_TESTING)
    add_subdirectory(test)
endif()
