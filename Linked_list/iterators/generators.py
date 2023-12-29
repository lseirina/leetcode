def square_numbers(nums):
    return [x**2 for x in nums]

#print(square_numbers([1, 3, 5, 7]))

nums = [1, 2, 3]
my_nums = (x**2 for x in nums)
for num in my_nums:
    print(num)
# def square_numbers1(nums):
#     for num in nums:
#          yield num**2

# for num in square_numbers1([1, 3, 5]):
#     print(num)























# def sentence(sentence):
#     for word in sentence.split():
#         yield word


# my_sentence = sentence('This is a test')

# # for word in my_sentence:
# #     print(word)
# print(next(my_sentence))


# def my_range(start, end):
#     while start < end:
#         current = start
#         start += 1
#         yield current


# for num in my_range(1, 6):
#     print(num)






























#
#
#
#
#
