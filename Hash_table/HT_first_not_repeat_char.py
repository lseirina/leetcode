
#  if the input string is "hello", the function should return "h" 
# because "h" is the first non-repeating character in the string.


def first_non_repeating_char(string):
    char_count = {}
    
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in string:
        if char_count[char] == 1:
            return char    
   

print(first_non_repeating_char("hello"))