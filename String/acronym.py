def isAcronym(words, s):
        res = []
        for word in words:
            res.append(word[0])

        if ''.join(res) == s:
            return True

        return False

print(isAcronym(["alice","bob","charlie"], "abc"))