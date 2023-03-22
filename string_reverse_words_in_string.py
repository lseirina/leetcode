# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

def reverse_words(words):
    word = words.split(" ")
    
    for i in range(len(word)):
        word[i] = word[i][::-1]
    
    return " ".join(word)
        

    
        

print(reverse_words("Let's take LeetCode contest"))