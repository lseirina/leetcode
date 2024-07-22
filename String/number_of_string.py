"""
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
"""


def count_number_str(patterns, word):
    count = 0
    for pattern in patterns:
        if pattern in word:
            count += 1
    return count


print(count_number_str(["a","abc","bc","d"], "abc"))





















# def count_number_of_strings(patterns, word)
#     count = 0
#     for pattern in patterns:
#         if pattern in word:
#             count += 1
#     return count
