"""
Input: s = "ab", t = "baab"
Output: true
"""


def find_subsequence(s, t):
    subsequence_index = 0
    for i in range(len(t)):
        if subsequence_index >= len(s):  # Check if we've matched the entire subsequence
            break
        if t[i] == s[subsequence_index]:
            subsequence_index += 1

    return len(s) == subsequence_index



print(find_subsequence('ab', 'baab'))
