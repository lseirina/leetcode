"""
Input: ransomNote = "aab", magazine = "baa"
Output: true
"""
from collections import Counter


def canConstruct(ransomNote, magazine):
    count = Counter(magazine)
    for c in ransomNote:
        if c in count and count[c] > 0:
            count[c] -= 1
        else:
            return False
    return True


print(canConstruct('aab', 'baafdb'))
