

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
"""

def roman_to_integer(s):
    translation = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    s.replace('IV', 'IIII').replace('IX', 'VIIII')
    s.replace('XL', 'XXXX'.replace('XC', 'VXXXX'))
    s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
    count = 0

    for c in s:
        count += translation[c]

    return count

print(roman_to_integer("MCMXCIV"))





















def roman_to_interger(s):
    translation = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

    for c in s:
        number += translation[c]
    return number

print(roman_to_interger("MCMXCIV"))
