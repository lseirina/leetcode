class My_range:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

my_range = My_range(1, 6)

for i in my_range:
    print(i)


class Sentence:
    def __init__(self, instence):
        self.instence = instence
        self.words = self.instence.split()
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word

my_sentence = Sentence('This is a test')

for word in my_sentence:
    print(word)


