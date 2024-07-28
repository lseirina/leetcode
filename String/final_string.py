"""
Your laptop keyboard is faulty,
and whenever you type a character 'i' on it,
it reverses the string that you have written.
Typing other characters works as expected.
Input: s = "string"
Output: "rtsng"
# """


def final_string(s):
    result = []

    for char in s:
        if char == 'i':
            result.reverse()
        else:
            result.append(char)

    return ''.join(result)

print(final_string("string"))
