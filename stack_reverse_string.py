# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

def reverse_string(s):
    stack = []
    for c in s:
        stack.append(c)
        
    for i in range(len(s)):
        s[i] = stack.pop()
        
    return s
print(reverse_string(["h","e","l","l","o"]))