"""
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
"""

import math

def find_greatest_devisor(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''

    gcd_len = math.gcd(len(str1), len(str2))

    return str1[:gcd_len]




    # min_len = min(len(str1), len(str2))

    # for i in range(min_len, 0, -1):
    #     if len(str1) % i == 0 and len(str2) % i == 0:
    #         candidate = str1[:i]
    #         if candidate * (len(str1) // i) == str1 and candidate * (len(str2) // i) == str2:
    #             return candidate

    # return ''


print(find_greatest_devisor("ABABAB", "ABAB"))
