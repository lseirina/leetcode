

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# -  2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = [num + 1 for num in result]
        return result
    return wrapper

#@my_decorator
def next_greater_element(nums1, nums2):
    if not nums2:
        return None

    next_greater = {}
    result = []
    stack = []

    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack[-1]] = num
            stack.pop()
        stack.append(num)

    for element in stack:
        next_greater[element] = -1

    for num in nums1:
        result.append(next_greater[num])

    return result

print(next_greater_element([2,4,7], [1,7,2,8,5,4,2,3,4,8,5]))

def test():
    assert next_greater_element([2,4,7], [1,7,2,8,5,4,2,3,4,8,5]) == [3,8,8]
    assert next_greater_element([0], [0]) == [-1]
    print('Tests passed')

test()