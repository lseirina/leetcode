"""
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
"""

def find_equal_pairs(grid):
    count = 0
    columns = list(zip(*grid))
    for row in grid:
        for col in columns:
            if tuple(row) == col:
                count += 1


    return count


print(find_equal_pairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))