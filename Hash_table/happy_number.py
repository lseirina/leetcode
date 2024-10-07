"""
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


def find_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total_sum = 0
        while n > 0:
            digit = n % 10
            total_sum += digit ** 2
            n //= 10

        n = total_sum

    return n == 1


print(find_happy_number(2))
