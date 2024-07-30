"""
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
"""

from collections import Counter


def part_string(s):
    res = ''
    ans = []
    for char in s:
        if char in res:
            ans.append(res)
            res = ''

        res += char
    ans.append(res)

    return len(ans)


print(part_string("abacaba"))
