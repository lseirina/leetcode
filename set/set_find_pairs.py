
# arr1 = [1, 2, 3, 4, 5]
# arr2 = [2, 4, 6, 8, 10]
# target = 7
# Output: [(5, 2), (3, 4), (1, 6)]
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} return {result}')
        return result
    return wrapper

@my_decorator
def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []

    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))

    return pairs

print(find_pairs([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], 7))

