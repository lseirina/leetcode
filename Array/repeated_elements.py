# xample 1:

# Input: nums = [1,2,3,3]
# Output: 3


from collections import Counter
def repeatedNTimes(nums):
    count = Counter(nums)
    for k, v in count.items():
        if v > 1:
            return k
        
        
print(repeatedNTimes([1,2,3,3]))