"""
Input: s = "abc", t = "bac"

Output: 2

Explanation:

For s = "abc" and t = "bac", the permutation difference of s and t is equal to the sum of:

The absolute difference between the index of the occurrence of "a" in s and the index of the occurrence of "a" in t.
The absolute difference between the index of the occurrence of "b" in s and the index of the occurrence of "b" in t.
The absolute difference between the index of the occurrence of "c" in s and the index of the occurrence of "c" in t.
That is, the permutation difference between s and t is equal to |0 - 1| + |2 - 2| + |1 - 0| = 2.

"""


def find_permutation(s, t):
    t_dict = {char: i for i, char in enumerate(t)}

    res = []

    for i in range(len(s)):
        if s[i] in t:
            res.append(abs(i - t_dict[s[i]]))

    return sum(res)



print(find_permutation("abc", "bac"))
