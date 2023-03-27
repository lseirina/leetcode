# ('abcdefg')) # should return True
# ('hello')) # should return False

def unique_chars(s):
    result = set()
    for char in s:
        if char in result:
            return False
        else:
            result.add(char)
            
    return True

print(unique_chars("abcdefg"))