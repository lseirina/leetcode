"""
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
"""


def find_greatest_number_of_candies(nums, extra):
    """Find the kids who has the greatest number of candies."""
    result = []

    for num in nums:
        if (num + extra) >= max(nums):
            result.append(True)
        else:
            result.append(False)

    return result

print(find_greatest_number_of_candies([2,3,5,1,3], 3))
