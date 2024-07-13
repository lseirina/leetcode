"""
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
"""

def string_interpreter(s):
    return s.replace('()', 'o').replace('(al)', 'al')

print(string_interpreter("G()(al)"))














# def interpret(command):
#     """Intrtpret the command."""
#     command = command.replace('()', 'o')
#     command = command.replace('(al)', 'al')

#     return command

# print(interpret("G()(al)"))

# def test():
#     assert interpret("G()(al)") == 'Goal'
#     assert interpret('') == ''
#     assert interpret('oal') == 'oal'
#     print('Tests passed')

# test()