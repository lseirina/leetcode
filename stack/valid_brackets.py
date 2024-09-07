def check_valid_brackets(brackets):
    dict_brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for bracket in brackets:
        if stack and bracket in dict_brackets:

        else:
            stack.append(bracket)




def test():
    assert check_valid_brackets('({})') is True
    assert check_valid_brackets('[(})') is False
