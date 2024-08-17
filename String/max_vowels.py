"""
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
"abciiidef", 3
"""

def find_max_vowels(s, k):
    vowels = set('aeuio')
    current_vowel_count = 0
    for c in s[:k]:
        if c in vowels:
            current_vowel_count += 1

    max_vowel_count = current_vowel_count

    for i in range(k, len(s)):
        if s[i-k] in vowels:
            current_vowel_count -= 1
        if s[i] in vowels:
            current_vowel_count += 1
        max_vowel_count = max(max_vowel_count, current_vowel_count)

    return max_vowel_count


print(find_max_vowels("abciiidef", 3))
