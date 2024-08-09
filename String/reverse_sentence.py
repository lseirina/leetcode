"""
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""
def reverse_sentence(s):
    split_s = s.split()
    split_s.reverse()

    return ' '.join(split_s)



print(reverse_sentence("a good   example"))