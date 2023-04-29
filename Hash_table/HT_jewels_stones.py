"""
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""
import collections

def num_jewels_in_stone(jewels, stones):
    set_jewels = set(jewels)
    count = 0

    for stone in stones:
        if stone in set_jewels:
            count += 1

    return count

"""
The list comprehension
    return sum(stone in set_jewels for stone in stones)

"""

print(num_jewels_in_stone("aA","aAAbbbb"))

