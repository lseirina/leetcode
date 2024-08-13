"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.
"""
def find_max_area(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area between the two lines
        current_area = min(height[left], height[right]) * (right - left)
        # Update the maximum area found
        max_area = max(max_area, current_area)

        # Move the pointer that is at the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


print(find_max_area([1,8,6,2,5,4,8,3,7]))
