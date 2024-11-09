def check_valid_brackets(s):
    stack = []
    parentheses = {')': '(', '}': '{', ']': '['}

    for c in s:
        if stack and parentheses[c] in stack:
            stack.remove(parentheses[c])
        else:
            stack.append(c)

    # return not stack
    # dict_brackets = {')': '(', '}': '{', ']': '['}
    # stack = []
    # for bracket in brackets:
    #     if bracket in dict_brackets:
    #         top_element = stack.pop() if stack else '#'
    #         if dict_brackets[bracket] != top_element:
    #             return False
    #     else:
    #         stack.append(bracket)

    # return not stack


print(check_valid_brackets('[{}]'))


# def test():
#     assert check_valid_brackets('({})') is True
#     assert check_valid_brackets('[(})') is False


# test()