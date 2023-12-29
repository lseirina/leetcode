nums = [1, 2, 3, 4, 5]

num_iter = iter(nums)

while True:
    try:
        item = next(num_iter)
        print(item)
    except StopIteration:
        break
























# nums = [1, 2, 3]
# #print(dir(nums))

# i_nums = iter(nums)
# #print(dir(i_nums))


