"""
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.

"""
from collections import Counter


def create_2d_array(nums):
    count = Counter(nums)

    ans = []
    while count:
        temp = []
        res = []
        for k, v in count.items():
            temp.append(k)
            v -= 1
            if v == 0:
                res.append(k)
            count[k] = v
        ans.append(temp)
        for num in res:
            del count[num]

    return ans


print (create_2d_array([1, 3, 4, 1, 2, 3, 1]))


# from collections import Counter
# def find_matrix(nums):
#     count = Counter(nums)
#     result = {}

#     k = max(count.values())
#     A = list(count.elements()) #The elements() method is a part of the Counter class in Python. It returns an iterator over
#                                #elements repeating each element as many times as its count.
#     #return [A[i::k] for i in range(k)] #The slicing syntax A[i::k] means to start from index i and to take every kth
#     # element from that point onwards.
#     return A
