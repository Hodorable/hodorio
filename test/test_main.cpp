#include <gtest/gtest.h>
#include <gmock/gmock.h>

// powered by gtest : https://github.com/google/googletest/blob/master/googletest/docs/Primer.md

int main(int argc, char * argv[]) {

  testing::InitGoogleMock(&argc, argv);

  return RUN_ALL_TESTS();
}
