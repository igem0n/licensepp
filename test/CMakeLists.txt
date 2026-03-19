find_package (GTest REQUIRED)

include(GoogleTest)

add_executable (licensepp-unit-tests
    license-manager-for-test.h
    license-manager-test.h
    main.cc
    test.h
)

target_link_libraries (licensepp-unit-tests PRIVATE gtest::gtest licensepp)
gtest_discover_tests(licensepp-unit-tests)