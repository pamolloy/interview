#include "gtest/gtest.h"

#include "solution.h"

TEST(LeftUnique, base)
{
    LeftUnique lu("dpgkdispdflgs");

    EXPECT_EQ('k', lu.left_unique());
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
