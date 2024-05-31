# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def find_longest_prefix(words: list[str]) -> str:
    res = []
    short_word = min(words, key=len)
    for i in range(len(short_word)):
        for word in words.remove(short_word):
            if word[i] == short_word[i]:
                res.append(short_word[:i+1])
    return res

print(find_longest_prefix(["flower", "flow", "flight"]))
