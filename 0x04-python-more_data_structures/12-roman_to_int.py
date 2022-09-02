#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to integer

    Args:
        roman_string (str): roman numerals

    Returns:
        int: converted value
        Zero: if roman_string is not a string or None
    """
    roman_numerals = {"I": 1,
                      "V": 5,
                      "X": 10,
                      "L": 50,
                      "C": 100,
                      "D": 500,
                      "M": 1000}

    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0

    arabic_numeral = 0
    # loop through the roman_strings and roman_strings+1
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in roman_numerals.keys():
            return 0
        elif roman_numerals[i] >= roman_numerals[j]:
            arabic_numeral += roman_numerals[i]
        else:
            arabic_numeral -= roman_numerals[i]

    # Add the last letter in roman_string
    arabic_numeral += roman_numerals[roman_string[-1]]

    return (arabic_numeral)
