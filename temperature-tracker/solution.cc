#include "solution.h"

#include <algorithm>    // max_element()
#include <limits>       // numeric_limits<>::infinity()

#include <cstdint>      // uint32_t

TempTracker::TempTracker()
{
    auto infinity = std::numeric_limits<float>::infinity();
    max = -infinity;
    min = infinity;
    mean = 0;
    count = 0;
}

void TempTracker::insert(Temp temp)
{
    if (temp > max) {
        max = temp;
    }
    if (temp < min) {
        min = temp;
    }

    mean = ((mean * count) + temp) / ++count;

    temp_count[temp]++;
}

Temp TempTracker::get_max()
{
    return max;
}

Temp TempTracker::get_min()
{
    return min;
}

Temp TempTracker::get_mean()
{
    return mean;
}

uint32_t TempTracker::get_mode()
{
    // TODO(PM): Understand this a bit better
    auto result = max_element(
        begin(temp_count),
        end(temp_count),
        [] (const pair_type & p1, const pair_type & p2) {
            return p1.second < p2.second;
        }
    );
    return result->first;
}
