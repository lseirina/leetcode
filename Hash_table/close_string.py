"""
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc
"""
from collections import Counter

def find_close_strings(word1, word2):
    if len(word1) != len(word2):
        return False

    if set(word1) != set(word2):
        return False

    count1 = Counter(word1)
    count2 = Counter(word2)

    if sorted(count1.values()) != sorted(count2.values()):
        return False

    return True


print(find_close_strings("cabbba", "abbccc"))