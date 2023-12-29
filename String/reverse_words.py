def reverseWords(s):
        s = s.split()
        res = []
        for c in s:
            res.append(c[:: -1])

        return " ".join(res)

print(reverseWords("Let's take LeetCode contest"))