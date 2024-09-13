"""
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


def find_last_word(s):
    split_s = s.split()
    return len(split_s[-1])


print(find_last_word("luffy is still joyboy"))