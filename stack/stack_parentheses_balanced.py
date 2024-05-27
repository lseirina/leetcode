# print(balanced_parentheses("((()))"))















def balanced_parentheses(s):


    res = 0
    for c in s:
        if c == "(":
            res += 1

        if c == ")":
            res -= 1
    if res == 0:
        return True

    else:
        return False

print(balanced_parentheses("((()))"))