"""
Input: accounts = [[1,2,3],[3,6,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
"""

def find_max_wealth(accounts):
   return max([sum(account) for account in accounts])

print(find_max_wealth([[1,2,3],[3,7,1]]))
















# def find_max_wealth(accounts):
#     """Find the maximim wealth."""
#     return max([sum(account) for account in accounts])

# print(find_max_wealth([[1,2,3],[3,2,1]]))
