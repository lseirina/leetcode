"""
Input: s = "anagram", t = "nagaram"

Output: true
"""
def check_anagram(s, t):
    if sorted(s) == sorted(t):
        return True
    return False


print(check_anagram("anagram", "nagaram"))