# print(reverseWords("Let's take LeetCode contest"))
# output: s'teL ekat edoCteeL tsetnoc


def reverse_words(sentence):
    sentence = sentence.split(' ')
    i = 0
    for i in range(len(sentence)):
        sentence[i] = sentence[i][::-1]
        i += 1


    return ' '.join(sentence)

print(reverse_words("Let's take LeetCode contest"))





















def reverseWords(s):
        s = s.split()
        res = []
        for c in s:
            res.append(c[:: -1])

        return " ".join(res)

print(reverseWords("Let's take LeetCode contest"))