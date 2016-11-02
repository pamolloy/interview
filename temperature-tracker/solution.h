#include <cstdint>      // uint32_t
#include <map>          // map<>

using Temp = float;

class TempTracker
{
    public:
        // Members
        TempTracker();
        void insert(Temp);
        Temp get_max();
        Temp get_min();
        Temp get_mean();
        uint32_t get_mode();

    private:
        Temp max;
        Temp min;
        Temp mean;
        uint32_t mode;
        uint32_t count;
        std::map<Temp,uint32_t> temp_count;
        // TODO(PM): Understand this a bit better
        using pair_type = decltype(temp_count)::value_type;
};
