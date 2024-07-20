
# Input: prices = [8,4,6,2,3]
# Output: [4,2,4,2,3]
# Explanation:
# For item 0 with price[0]=8 you will receive a discount equivalent to prices[1]=4, therefore, the final price you will pay is 8 - 4 = 4.
# For item 1 with price[1]=4 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 4 - 2 = 2.
# For item 2 with price[2]=6 you will receive a discount equivalent to prices[3]=2, therefore, the final price you will pay is 6 - 2 = 4.
# For items 3 and 4 you will not receive any discount at all.


def count_discount(nums):
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] >= num:
            nums[stack.pop()] -= num
        stack.append(i)

    return nums


print(count_discount([8,4,6,2,3]))





































# def final_price(A):
#     stack = []
#     for i, a in enumerate(A):
#         while stack and A[stack[-1]] >= a:
#             A[stack.pop()] -= a
#         stack.append(i)
#     return A

# print(final_price([8,4,6,2,3]))
