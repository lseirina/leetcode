"""
Input: nums = [5,4,2,3]
Output: [3,2,5,4]
Explanation: In round one, first Alice removes 2 and then Bob removes 3. Then in arr firstly Bob appends 3 and then Alice appends 2. So arr = [3,2].
At the begining of round two, nums = [5,4]. Now, first Alice removes 4 and then Bob removes 5. Then both append in arr which becomes [3,2,5,4].
"""
def number_game(nums):
    arr = []

    while nums:
        a_min = min(nums)
        nums.remove(a_min)

        b_min = min(nums)
        nums.remove(b_min)

        arr.append(b_min)
        arr.append(a_min)

    return arr


print(number_game([5,4,2,3]))
