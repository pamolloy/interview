#!/usr/bin/env python3.4
#
#   google-prep/solution.py
#

examples = [
    ([0], True),
    ([1, 2, 3, 0], True),
    ([1, 0, 0, 0], False)
]

def circular(array):
    """Follow the pointers in the array n number of times, where n is the
       length of the array"""

    current_index = 0

    for _ in range(len(array)):
        try:
            new_index = array[current_index]
        except TypeError:
            return False
        array[current_index] = "Visited"
        current_index = new_index

    if current_index == 0:
        return True

if __name__ == "__main__":
    for example, result in examples:
        print(str(example))
        print(result)
        assert result == circular(example)
