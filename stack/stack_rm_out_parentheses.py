"""
Input: s = "(()())(())"
Output: "()()()"
"""
def remove_out_parentheses(s):
    res = []
    count = 0
    for c in s:
        if c == '(' and count > 0:
            res.append(c)
        if c == ')' and count > 1:
            res.append(c)

        if c == '(':
            count += 1
        else:
            count -= 1

    return ''.join(res)

print(remove_out_parentheses("(()())(())"))




print(remove_out_parentheses("(()())(())(()(()))"))























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


print(removeOuterParentheses("((())())(())"))