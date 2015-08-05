#!/usr/bin/env python
#
#   license-plate/solution.py
#

examples = [
    ("ANA 1452", True),
    ("CKE 1743", True),
    ("SKG 9538", True),
    ("ZAA 1543", False)
]

words = ["Banana", "Chicken", "Wolf", "Canteen", "Skiing", "Pantheon"]

def match(license_plate, words):
    #TODO: Word must be longer than plate_characters
    for word in words:
        plate_characters = {character: False for character in license_plate[:3]}
        for plate_character in plate_characters:
            # TODO: Start iterating at the last matching character
            # TODO: Don't iterate through the whole word if the plate_character
            #       is before the last character
            for word_character in word:
                if word_character == plate_character:
                    plate_characters[plate_character] = True

            # If the plate_character was not found in the word don't checking
            # the word for other plate_charaters
            if not plate_characters[plate_character]:
                break

        #TODO: Check to make sure that all the plate_characters were found

    return True

if __name__ == "__main__":
    for example, result in examples:
        assert result == match(words)
