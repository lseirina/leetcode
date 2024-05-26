# ('abcdefg')) # should return True
# ('hello')) # should return False

def find_unique_chars(chars):
    if len(chars) == len(set(chars)):
        return True
    return False


print(find_unique_chars('abcddefg'))
























def unique_chars(s):
    result = set()
    for char in s:
        if char in result:
            return False
        else:
            result.add(char)

    return True

print(unique_chars("abcdefg"))