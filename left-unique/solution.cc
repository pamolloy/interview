#include "solution.h"

#include <string>
#include <unordered_map>
#include <list>

LeftUnique::LeftUnique(std::string s) : _characters{s} {}

char LeftUnique::left_unique()
{
    struct UniqueIndex {
        uint64_t index;
        bool repeated;
    };

    std::unordered_map<char, UniqueIndex> character_map;

    for (std::string::size_type index = 0; index < _characters.size(); ++index) {
        auto character = _characters[index];
        auto search = character_map.find(character);
        if (search == character_map.end()) {
            character_map[character] = (UniqueIndex){index, false};
        } else {
            character_map[character].repeated = true;
        }
    }

    char character;
    uint64_t index;
    for (auto element : character_map) {
        if (element.second.repeated == false &&
            element.second.index < index)
        {
            character = element.first;
            index = element.second.index;
        }
    }

    return character;
}
