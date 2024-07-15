"""
Input: word = "abcde"
Output: "1a1b1c1d1e"

"""
def compress_str(word):
    count = 1
    compress_str = ''
    new_char = word[0]
    for i in range(1, len(word)):
        if word[i] == new_char and count < 9:
            count += 1
        else:
            compress_str += str(count) + new_char
            new_char = word[i]
            count = 1

    compress_str += str(count) + new_char

    return compress_str

print(compress_str("aaaaaaaaaaaaaabb"))