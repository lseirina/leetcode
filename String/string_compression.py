"""
input: word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b
"""

def find_compress_str(word):
    res = []
    count = 0

    for i in range(len(word)-1):
        if word[i] == word[i+1] and count < 9:
            count += 1

        else:
            res.append(str(count))
            res.append(word[i])
            count = 1

    res.append(str(count))
    res.append(word[i])

    return ''.join(res)


print(find_compress_str("aaaaaaaaaaaaaabb"))



#     comp = ''
#     i = 0

#     while i < len(word):
#         char = word[i]
#         count = 0

#         while i < len(word) and word[i] == char and count < 9:
#             count += 1
#             i += 1

#         comp += str(count) + char

#     return comp

# print(find_compress_str("aaaaaaaaaaaaaabb"))










#     count = 1
#     compress_str = ''
#     new_char = word[0]
#     for i in range(1, len(word)):
#         if word[i] == new_char and count < 9:
#             count += 1
#         else:
#             compress_str += str(count) + new_char
#             new_char = word[i]
#             count = 1

#     compress_str += str(count) + new_char

#     return compress_str

# print(find_compress_str("aaaaaaaaaaaaaabb"))