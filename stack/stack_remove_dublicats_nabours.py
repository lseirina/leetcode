# Input: s = "abbaca"
# Output: "ca"
# Explanation:
# For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal,
# and this is the only possible move.  The result of this move is that the string is "aaca",
# of which only "aa" is possible, so the final string is "ca".

def remove_duplicates_nabours(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return ''.join(stack)


print(remove_duplicates_nabours("abbaca"))


































# def remove_dublicates(chars: str):
#     stack = []
#     for c in chars:
#         if stack and stack[-1] == c:
#             stack.pop()
#         else:
#             stack.append(c)

#     return ''.join(stack)


# print(remove_dublicates("abbaca"))























def removeDublicates(s):
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)

print(removeDublicates("abbaca"))
