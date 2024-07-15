# print(found_first_unique_char('asdas'))

from collections import Counter

def find_first_unique_char(chars):
    my_dict = Counter(chars)

    for char in chars:
        if my_dict[char] == 1:
            return char

print(find_first_unique_char('asdas'))
































# def found_first_unique_char(s):
#     my_dict = {}
#     for c in s:
#         my_dict[c] = my_dict.get(c, 0) + 1

#     for i in range(len(s)):
#         if my_dict[s[i]] == 1:
#             return i

#     return -1

# print(found_first_unique_char('asdas'))
