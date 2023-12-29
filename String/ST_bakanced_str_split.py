"""
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL",
each substring contains same number of 'L' and 'R'.
"""

def split_balanced_string(s):
    count = 0
    res = 0
    for i in s:
        if i == "R":
            count += 1
        else:
            count -= 1
        if count == 0:
            res += 1

    return res


print(split_balanced_string("RLRRRLLRLL"))

def test():
    assert split_balanced_string("RLRRRLLRLL") == 2
    assert split_balanced_string("RLRRR") == 2
    print('tests passed')

test()