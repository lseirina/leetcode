"""
Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".
"""
def convert(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result.upper()
        return result
    return wrapper


@convert
def decode_message(key, message):
    mapping = {" ":" "}
    letters = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    count = 0
    for char in key:
        if char not in mapping:
            mapping[char] = letters[count]
            count += 1
    for i in message:
        res += mapping[i]

    return res



print(decode_message("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))