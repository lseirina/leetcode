"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
def find_valid_palindrom(s):
    words = [c for c in s.lower() if c.isalpha() or c.isdigit()]
    palindrom = ''.join(words)
    if palindrom == palindrom[::-1]:
        return True
    return False


print(find_valid_palindrom("A man, a plan, a canal: Panama"))
