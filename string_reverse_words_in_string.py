# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
def my_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result.upper()
        return result
    return wrapper


@my_decorator
def reverse_words(s):
    res = s.split()
    for i in range(len(res)):
        res[i] = res[i][::-1]
    return ' '.join(res)


print(reverse_words("Let's take LeetCode contest"))


def test_reverse_words():
    assert reverse_words("Let's take LeetCode contest") == "S'TEL EKAT EDOCTEEL TSETNOC"
    assert reverse_words('') == ''

    print('Tests passed')



test_reverse_words()


















# def reverse_words(words):
#     word = words.split(" ")

#     for i in range(len(word)):
#         word[i] = word[i][::-1]

#     return " ".join(word)





# print(reverse_words("Let's take LeetCode contest"))