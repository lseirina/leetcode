"""
Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
"""
def remove_occurences(s, part):
    while part in s:
        s = s.replace(part, '', 1)  # Remove only the leftmost occurrence
    return s
    # res = []
    # l_part = len(part)
    # for char in s:
    #     res.append(char)
    #     if part in ''.join(res):
    #         res = res[:-l_part]

    # return ''.join(res)

print(remove_occurences("axxxxyyyyb", 'xy'))
