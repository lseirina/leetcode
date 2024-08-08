"""
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""
def merge_alternately(word1, word2):
    i = 0
    res = []
    min_len = min(len(word1), len(word2))
    while i <= min_len - 1:
        res.append(word1[i])
        res.append(word2[i])
        i += 1

    res.append(word1[i:])
    res.append(word2[i:])

    return ''.join(res)


print(merge_alternately("abc", "pqr"))
