"""
Input: pattern = "abba", s = "dog cat cat dog"

Output: true
"""

def find_word_pattern(pattern, s):
    new_s = s.split()
    my_dict1 = {}
    my_dict2 = {}
    for c1, c2 in zip(pattern, new_s):
        if (c1 in my_dict1 and my_dict1[c1] != c2) or (c2 in my_dict2 and my_dict2[c2] != c1):
            return False
        my_dict1[c1] = c2
        my_dict2[c2] = c1
    return True




print(find_word_pattern("abba", "dog dog dog dog"))
