#include "gtest/gtest.h"

#include "solution.h"

TEST(TempTracker, mode)
{
    TempTracker tracker;

    tracker.insert(1);
    tracker.insert(2);
    tracker.insert(3);
    tracker.insert(2);

    EXPECT_EQ(2, tracker.get_mode());
}

TEST(TempTracker, max)
{
    TempTracker tracker;

    tracker.insert(1);
    tracker.insert(2);
    tracker.insert(3);
    tracker.insert(2);

    EXPECT_EQ(3, tracker.get_max());
}

TEST(TempTracker, min)
{
    TempTracker tracker;

    tracker.insert(1);
    tracker.insert(2);
    tracker.insert(3);
    tracker.insert(2);

    EXPECT_EQ(1, tracker.get_min());
}

int main(int argc, char **argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
