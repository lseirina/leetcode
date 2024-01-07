def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result += 1
        return result
    return wrapper

@my_decorator
def remove_element(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1

    return len(nums)

print(remove_element([1, 1, 1, 4, 1], 1))

def test():
    assert remove_element([], 2) == 1

    print('Tests passed')





test()

















# def remove_element(nums, val):
#     i = 0
#     while i < len(nums):
#         if nums[i] == val:
#             nums.pop(i)
#         else:
#             i += 1


#     return len(nums)
# print(remove_element([1,1,1,1], 1))