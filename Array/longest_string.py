"""string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  # expected output: 'banana'"""


def get_longest_string(words):
    return max(words, key=lambda x: len(x))


print(get_longest_string(['apple', 'banana', 'kiwi', 'pear']))
























# def find_longest_string(words):
#     return max(words, key=len)

# string_list = ['apple', 'banana', 'kiwi', 'pear']
# longest = find_longest_string(string_list)
# print(longest)