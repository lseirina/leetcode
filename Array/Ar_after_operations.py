"""
Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
"""


def find_final_value(str):
    count = 0
    for i in str:
        if "+" in i:
            count += 1
        else:
            count -= 1

    return count

print(find_final_value(["--X","X++","X++"]))