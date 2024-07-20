
# Input: s = "(1+(2*3)+((8)/4))+1"
# # Output: 3

def count_max_depth(s):
    max_count = 0
    count = 0
    for c in s:
        if c == '(':
            count += 1
        if c == ')':
            count -= 1
        max_count = max(max_count, count)

    return max_count


print(count_max_depth("(1+(2*3)+((8)/4))+1"))

























# def find_max_depth(s):
#     count = 0
#     max_depth = 0
#     for c in s:
#         if c == '(':
#             count += 1
#         if c == ')':
#             count -= 1
#         max_depth = max(max_depth, count)

#     return max_depth


# print(find_max_depth("(1+(2*3)+(((8))/4))+1"))



























# def max_depth(s):
#     res = 0
#     temp = 0
#     for c in s:
#         if c == "(":
#             temp += 1
#             res = max(res, temp)
#         if c == ")":
#             temp -= 1

#     return res

# print(max_depth("(1+(2*3)+((8)/4))+1)"))