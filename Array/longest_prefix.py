"""
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
from collections import defaultdict

def longestCommonPrefix(strs):

    min_len = min(strs, key=lambda x: len(x))

    res = []
    ans = []
    for i in range(len(strs)):
        if min_len[0] != strs[i][0]:
            return ''
        for j in range(len(min_len)):
            if min_len[j] == strs[i][j]:
                res.append(min_len[j])
            if res and j == len(min_len)-1:
                ans.append(res)
                res = []

    min_ans = min(ans)
    return ''.join(min_ans)


print(longestCommonPrefix(["flower","flow","flight"]))