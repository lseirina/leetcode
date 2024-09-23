"""
Input: s = "paper", t = "title"
Output: true
"""
from collections import Counter

def is_isomorphic(s, t):
    my_dict = {}
    i = 0
    j = 0
    res = []
    for c in s:
        if t[i] in my_dict.values():
            return False
        my_dict[c] = t[i]
        i += 1

    for c in s:
        if my_dict[c] == t[j]:
            j += 1
            res.append(c)

    if len(res) == len(t):
        return True
    return False


print(is_isomorphic("paper", "title"))
