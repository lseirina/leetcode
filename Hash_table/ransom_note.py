"""
Input: ransomNote = "aab", magazine = "baa"
Output: true
"""
from collections import Counter


def canConstruct(ransomNote, magazine):
    count_r = Counter(ransomNote)
    count_m = Counter(magazine)
    i = 0
    n = len(set(ransomNote))
    for k, v in count_r.items():
        if count_m[k] >= v:
            i += 1

    if i == n:
        return True
    return False


print(canConstruct('aab', 'baafdb'))