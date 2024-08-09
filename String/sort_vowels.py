"""
Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c',
and 'd' are all consonants. The vowels are sorted according
to their ASCII values, and the consonants remain in the same places.
The vowels are 'a', 'e', 'i', 'o', and 'u'
"""

def permute_string(s):
    def is_vowels(c):
        return c.lower() in 'aeiou'

    vowels = [c for c in s if is_vowels(c)]
    vowels.sort()
    vowel_index = 0
    res = []

    for char in s:
        if is_vowels(char):
            res.append(vowels[vowel_index])
            vowel_index += 1

        else:
            res.append(char)

    return res


print(permute_string("lEetcOde"))
