"""
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
"""
def find_largest_altitude(gain):
    current_gain = 0
    max_gain = 0
    for i in range(len(gain)):
        current_gain += gain[i]
        max_gain = max(max_gain, current_gain)

    return max_gain


print(find_largest_altitude([52,-91,72]))