# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"

def sortSentence(s):
    s = s.split()
    #res = [''] * len(s)
    res = []
    for c in s:
        num = int(c[-1])
        res[num-1] = c[:-1]

    return ' '.join(res)

print(sortSentence("is2 sentence4 This1 a3"))

