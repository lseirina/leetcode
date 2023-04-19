"""
Input: s = "(()())(())"
Output: "()()()"
"""

def remove_out_parentheses(str):

    stack = []
    opened = 0

    for char in str:
        if char == "(" and opened > 0:
            stack.append(char)

        if char ==")" and opened > 1:
            stack.append(char)

        if char =="(":
            opened += 1
        if char == ")":
            opened -= 1

    return "".join(stack)

print(remove_out_parentheses("(()())(())"))































def removeOuterParentheses(S):
        res = []
        opened = 0
        for c in S:
            if c == '(' and opened > 0:
                res.append(c)
            if c == ')' and opened > 1:
                res.append(c)

            if c == '(':
                opened += 1
            else:
                opened -= 1
        return "".join(res)


print(removeOuterParentheses("(()())(())"))