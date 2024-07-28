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
        return c in ['a', 'e', 'i', 'o', 'u']

    vowels = [c for c in s if is_vowels]
    vowel_index = 0
    res = []
    vowels.sort()

    for c in s:
        if c in vowels:
            res.append(vowels[vowel_index])
            vowel_index += 1
        else:
            res.append(c)

    return ''.join(res)


print(permute_string("lEetcOde"))
