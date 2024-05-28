# print(isAcronym(["alice","bob","charlie"], "abc")) True

def my_decorator(func):
    def wrapper(*args, **kwargs):
        resultat = func(*args, **kwargs)
        resultat = False
        return resultat
    return wrapper


def confirm_acronym(words, acronym):
    res = []
    for word in words:
        res.append(word[0])
    if ''.join(res) == acronym:
        return True
    return False


print(confirm_acronym(["alice","bob","charlie"], "abc"))


def test_confirm_acronym():
    assert confirm_acronym(["alice","bob","charlie"], "abc") == True
    print('Tests passed')

test_confirm_acronym()























def isAcronym(words, s):
        res = []
        for word in words:
            res.append(word[0])

        if ''.join(res) == s:
            return True

        return False

print(isAcronym(["alice","bob","charlie"], "abc"))