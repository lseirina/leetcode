
#  if the input string is "hello", the function should return "h"
# because "h" is the first non-repeating character in the string.



















from collections import Counter
def find_not_repeat_char(s: str):
    count = Counter(s)


    for k, v in count.items():
        if v == 1:
            return k

# print(find_not_repeat_char('hello'))






















# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         result = result.title()
#         return result
#     return wrapper

# @my_decorator
# def first_non_repeating_char(string):
#     char_count = {}

#     for char in string:
#         char_count[char] = char_count.get(char, 0) + 1

#     for char in string:
#         if char_count[char] == 1:
#             return char


# print(first_non_repeating_char("hello"))

# def test():
#     assert first_non_repeating_char('hhello') == 'E'

#     print('tests passed')

# test()