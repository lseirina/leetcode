"""
Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".
"""
import random


def valid_string(n):
    res = set()
    queue = ['']
    # Use a queue to generate the strings systematically
    while queue:
        s = queue.pop(0)
        if len(s) == n:
            res.add(s)
        else:
            queue.append(s + '0')
            queue.append(s + '1')

    filtered_res = {char for char in res if '00' not in char}
    return filtered_res


print(valid_string(3))
