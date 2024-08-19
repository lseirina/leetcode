"""
Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef
"""
def decode_string(s):
    stack = []
    split_s = s.split('[')
    # for c in split_s:
    #     if stack and int(stack[-1]):
    #         n = int(stack[-1])
    #         while n > 0:
    #             stack.append(c)
    #             n -= 1

    #     else:
    #         stack.append(c)

    return split_s



print(decode_string("2[abc]3[cd]ef"))