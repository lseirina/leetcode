"""
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
from collections import defaultdict

def longestCommonPrefix(strs):
    if not strs:
        return ''
    min_str = min(strs, key=len)

    for i in range(len(min_str)):
        for s in strs:
            if s[i] != min_str[i]:
                return min_str[:i]

    return min_str


print(longestCommonPrefix(["flower","flow","flight"]))