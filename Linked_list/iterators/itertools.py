import itertools

def lt_2(n):
    if n >=2:
        return True
    return False

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3, 2, 1, 0]
names = ['Corey', 'Nicole']

result = itertools.combinations(letters, 2)

result1 = itertools.permutations(letters, 2)

result2 = itertools.product(numbers, repeat=4)

combined = itertools.chain(letters, numbers, names)

result3 = itertools.islice(range(10), 1, 5, 2)

selectors = [True, False, True, True]


result4 = itertools.compress(letters, selectors)

result5 = itertools.filterfalse(lt_2, numbers)

for item in result5:
    print(item)

# with open('project1/names.txt') as f:
#     header = itertools.islice(f,3)

#     for line in header:
#         print(line, end='')











# counter = itertools.count(start=5, step=5)

# counter = itertools.cycle([1,2,3])

# counter = itertools.repeat(2, times=5)

# squares = map(pow, range(10), itertools.repeat(2))
# squares = itertools.starmap(pow, [(0, 3), (1, 2), (2, 3)])

# data = [100, 200, 300, 400]

# daily_data = list(itertools.zip_longest(range(10), data))

# print(list(squares))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))