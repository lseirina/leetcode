# my_str = 'aabcccccaaa' -> 'a2b1c5a3'

def compress_string(s):
    count = 1
    compress_string = ''
    new_char = s[0]
    for i in range(1, len(s)):
        if s[i] == new_char:
            count += 1
        else:
            compress_string += new_char + str(count)
            count = 1
            new_char = s[i]

    compress_string += new_char + str(count)

    if len(compress_string) < len(s):
        return compress_string
    return s


print(compress_string('aabcccccaaa'))