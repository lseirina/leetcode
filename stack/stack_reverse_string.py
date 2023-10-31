# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# def reverse_string(chars):
#     return chars[::-1]

# print(reverse_string(["h","e","l","l","o"]))






















# def reverse_string(chars):
#     stack = []
#     while chars:
#         stack.append(chars.pop())
#     return stack

# print(reverse_string(["h","e","l","l","o"]))
























# def reverse_string(s):
#     stack = []

#     while s:
#         stack.append(s.pop())

#     return stack

# print(reverse_string(["h","e","l","l","o"]))



# def reverse_string(s):
#     stack = []
#     for c in s:
#         stack.append(c)

#     for i in range(len(s)):
#         s[i] = stack.pop()

#     return s
# print(reverse_string(["h","e","l","l","o"]))