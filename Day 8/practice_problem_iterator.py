class Sentence:

    def __init__(self, string: str):
        self.string = string
        self.index = 0
        self.words = self.string.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration

        i = self.index
        self.index += 1
        return self.words[i]


def sentence_gen(sentence: str):
    for s in sentence.split():
        yield s


my_sentence = Sentence("A big brown hound")

for w in list(my_sentence):
    print(w)


for w in sentence_gen("A big brown hound"):
    print(w)
