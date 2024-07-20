# ('abcdefg')) # should return True
# ('hello')) # should return False
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{result} is a good result')
        return result
    return wrapper

@my_decorator
def find_unique_chars(s):
    if len(s) == len(set(s)):
        return True
    else:
        return False


print(find_unique_chars('abcddefg'))


def test():
    assert find_unique_chars('') is True

    print('Tests passed')



test()















































# def unique_chars(s):
#     result = set()
#     for char in s:
#         if char in result:
#             return False
#         else:
#             result.add(char)

#     return True

# print(unique_chars("abcdefg"))