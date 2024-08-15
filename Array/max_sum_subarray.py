"""
Given an array of integers and a number k, find the maximum sum of a subarray of size k.

Example:
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray [5, 1, 3] has the maximum sum of 9.
"""

def max_sum_subarray(arr, k):
    # Initialize variables
    #max_sum = 0
    window_sum = 0
    start = 0

    # Calculate the sum of the first window of size k
    for i in range(k):
        window_sum += arr[i]

    max_sum = window_sum

    for end in range(k, len(arr)):
        window_sum += arr[end] - arr[start]
        max_sum = max(max_sum, window_sum)
        start += 1

    return max_sum


print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))