# print(reverseWords("Let's take LeetCode contest"))
# output: s'teL ekat edoCteeL tsetnoc


def reverse_words(sentence):
    res = []
    s_sentence = sentence.split(' ')
    for word in s_sentence:
        res.append(word[::-1])

    return ' '.join(res)


print(reverse_words("Let's take LeetCode contest"))























# def reverse_words(sentence):
#     sentence = sentence.split(' ')
#     i = 0
#     for i in range(len(sentence)):
#         sentence[i] = sentence[i][::-1]
#         i += 1


#     return ' '.join(sentence)

# print(reverse_words("Let's take LeetCode contest"))
