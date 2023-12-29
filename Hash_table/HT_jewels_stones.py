"""
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""
#import collections
def convert(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result += 1
        return result
    return wrapper

@convert
def num_jewels_in_stone(jewels, stones):
    set_jewels = set(jewels)
    count = 0

    for stone in stones:
        if stone in set_jewels:
            count += 1

    return count



def test():
    assert num_jewels_in_stone("aA", "aAAbbbb") == 4
    assert num_jewels_in_stone("B", "aAAbbbb") == 1
    print('Tests passed')

test()
"""
The list comprehension
    return sum(stone in set_jewels for stone in stones)

"""

print(num_jewels_in_stone("aA","aAAbbbb"))

