"""
Input: s = "paper", t = "title"
Output: true
"""
from collections import Counter

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    my_dict1 = {}
    my_dict2 = {}
    for c1, c2 in zip(s, t):
        if (c1 in my_dict1 and my_dict1[c1] != c2) or (c2 in my_dict2 and my_dict2[c2] != c1):
            return False
        my_dict1[c1] = c2
        my_dict2[c2] = c1
    return True



print(is_isomorphic("paper", "title"))
