"""
Input: A = [1,3,2,4], B = [3,1,2,4]
Output: [0,2,3,4]
Explanation: At i = 0: no number is common, so C[0] = 0.
At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
"""
def find_common_prefix(A, B):
    n = len(A)
    set_A = set()
    set_B = set()
    common = set()
    res = []

    for i in range(n):
        set_A.add(A[i])
        set_B.add(B[i])
        if A[i] in set_B:
            common.add(A[i])
        if B[i] in set_A:
            common.add(B[i])

        res.append(len(common))

    return res


print(find_common_prefix([1,3,2,4], [3,1,2,4]))

















# def find_common_prefix(A, B):
#     set_A = set()
#     set_B = set()
#     n = len(A)
#     C = [0]*n

#     for i in range(n):
#         set_A.add(A[i])
#         set_B.add(B[i])

#         C[i] = len(set_A.intersection(set_B))

#     return C


# print(find_common_prefix([1,3,2,4], [3,1,2,4]))
