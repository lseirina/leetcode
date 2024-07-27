def rotate(nums, k):
    # k %= n ensures that the number of rotations is minimized and within the effective range.
    # if len = 5 and k =12, 12 % 5 = 2 (5*2 = 10 12=10 = 2 (как решаем в столбик)),
    # т.е. два раза пройдет по списку с длинной 5 и останется еще 2 раза переместить
    k = k % len(nums)
    # The notation nums[:] = ... is used to modify the list nums in place,
    # whereas nums = ... would reassign the variable nums to a new list
    nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)
