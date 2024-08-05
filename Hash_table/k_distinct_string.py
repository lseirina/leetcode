"""
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned.
"""
from collections import Counter


def find_k_distinct_string(arr, k):
    count = Counter(arr)
    res = []

    for key, v in count.items():
        if v == 1:
            res.append(key)
    if len(res) < k:
        return ''
    return res[k-1]



print(find_k_distinct_string(["aaa","aa","a"], 1))
