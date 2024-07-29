"""
Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
"""

def part_string(s):
    last_occurrence = {c: i for i, c in enumerate(s)}
    start, end = 0, 0
    res = []

    for i, c in enumerate(s):
        end = max(end, last_occurrence[c])

        if i == end:
            res.append(end - start + 1)
            start = i + 1

    return res


print(part_string("ababcbacadefegdehijhklij"))